#!/usr/bin/env python3
"""Split WhiteDNS upstream sub (mihomo.yaml + base64.txt) into per-country subs.

Source:
  https://github.com/iampedii/whitedns-sub  (mihomo.yaml, base64.txt)

Outputs (in subs/):
  mihomo-<CC>.yaml   - Mihomo/Clash proxies-only, usable in WhiteVPN, Clash, Mihomo, NekoBox...
  raw-<CC>.txt       - plain share-links (vless/vmess/trojan/ss/hysteria2...), usable in v2rayNG etc.
  base64-<CC>.txt    - base64-encoded share-links (standard sub format)
  index.json         - counts + update time

Country detection: from proxy `name` field, e.g.
  "🇩🇪 | @WhiteDNS | DE360|39.8MB/s|DNSOK|GPT⁺-DE" -> DE
  "❓ | @WhiteDNS | OT187|..." -> OT (Other/Unknown)

Run:  python split.py
Requires: pyyaml (pip install pyyaml)
"""
import base64
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

UPSTREAM_MIHOMO = "https://raw.githubusercontent.com/iampedii/whitedns-sub/main/mihomo.yaml"
UPSTREAM_BASE64 = "https://raw.githubusercontent.com/iampedii/whitedns-sub/main/base64.txt"

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "subs"

# Minimal full-clash template so the yaml also works in apps that
# require proxy-groups (ClashMeta/Mihomo/Streisand/NekoBox).
# We keep mihomo-<CC>.yaml as proxies-only (like upstream, for WhiteVPN),
# and also emit clash-<CC>.yaml as a ready-to-use full config.
CLASH_TEMPLATE = """port: 7890
socks-port: 7891
allow-lan: true
mode: rule
log-level: info
external-controller: 127.0.0.1:9090
dns:
  enable: true
  ipv6: false
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  nameserver:
    - https://1.1.1.1/dns-query
    - https://8.8.8.8/dns-query
"""


def extract_country(name: str) -> str:
    if not name:
        return "OT"
    # 1) "| DE360|" , "| NL606|" , "| OT187|"
    m = re.search(r"\|\s*([A-Z]{2})\d+\s*\|?", name)
    if m:
        return m.group(1)
    # 2) suffix "GPT+-DE" (covers GPT⁺-DE, GPT+-DE, GPT-DE)
    m = re.search(r"GPT.?-([A-Z]{2})\s*$", name)
    if m:
        return m.group(1)
    # 3) standalone "| DE |"
    m = re.search(r"\|\s*([A-Z]{2})\s*\|", name)
    if m:
        return m.group(1)
    return "OT"


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "WSK-splitter/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def b64_decode_loose(s: str) -> str:
    s = "".join(s.split())
    s += "=" * (-len(s) % 4)
    return base64.b64decode(s).decode("utf-8", errors="replace")


def main() -> None:
    print(f"[1/4] fetching {UPSTREAM_MIHOMO}")
    mihomo_text = fetch_text(UPSTREAM_MIHOMO)
    data = yaml.safe_load(mihomo_text)
    proxies = data.get("proxies") or []
    print(f"      proxies: {len(proxies)}")

    print(f"[2/4] fetching {UPSTREAM_BASE64}")
    b64_text = fetch_text(UPSTREAM_BASE64).strip()
    links = b64_decode_loose(b64_text).strip().splitlines()
    links = [l.strip() for l in links if l.strip()]
    print(f"      links: {len(links)}")

    # group mihomo proxies by country
    by_country_proxies: dict[str, list] = {}
    for p in proxies:
        cc = extract_country(str(p.get("name", "")))
        by_country_proxies.setdefault(cc, []).append(p)

    # group share-links by country (fragment after # holds the name)
    by_country_links: dict[str, list[str]] = {}
    for link in links:
        frag = link.split("#", 1)[1] if "#" in link else link
        cc = extract_country(unquote(frag))
        by_country_links.setdefault(cc, []).append(link)

    countries = sorted(set(by_country_proxies) | set(by_country_links))
    print(f"[3/4] countries found ({len(countries)}): {' '.join(countries)}")

    OUT.mkdir(parents=True, exist_ok=True)
    # clean old generated files (keep index.json regeneration simple)
    for f in OUT.glob("mihomo-*.yaml"):
        f.unlink()
    for f in OUT.glob("clash-*.yaml"):
        f.unlink()
    for f in OUT.glob("raw-*.txt"):
        f.unlink()
    for f in OUT.glob("base64-*.txt"):
        f.unlink()

    index = {"updated_at": datetime.now(timezone.utc).isoformat(), "upstream": UPSTREAM_MIHOMO, "countries": {}}

    for cc in countries:
        plist = by_country_proxies.get(cc, [])
        llist = by_country_links.get(cc, [])

        # 1) proxies-only yaml (same shape as upstream -> works in WhiteVPN)
        with open(OUT / f"mihomo-{cc}.yaml", "w", encoding="utf-8") as f:
            yaml.safe_dump({"proxies": plist}, f, allow_unicode=True, sort_keys=False)

        # 2) full clash yaml (works in Clash/Mihomo/Streisand/NekoBox that need proxy-groups)
        names = [str(p.get("name", f"{cc}-{i}")) for i, p in enumerate(plist)]
        # yaml-dump proxy names safely
        group_block = {
            "proxy-groups": [
                {"name": f"{cc}-Auto", "type": "url-test", "proxies": names, "url": "http://www.gstatic.com/generate_204", "interval": 300}
            ],
            "rules": ["MATCH," + f"{cc}-Auto"],
        }
        with open(OUT / f"clash-{cc}.yaml", "w", encoding="utf-8") as f:
            f.write(CLASH_TEMPLATE)
            yaml.safe_dump({"proxies": plist}, f, allow_unicode=True, sort_keys=False)
            yaml.safe_dump(group_block, f, allow_unicode=True, sort_keys=False)

        # 3) raw + base64 share-links (works in v2rayNG, NekoBox, FoXray, Streisand...)
        raw = "\n".join(llist) + ("\n" if llist else "")
        with open(OUT / f"raw-{cc}.txt", "w", encoding="utf-8") as f:
            f.write(raw)
        with open(OUT / f"base64-{cc}.txt", "w", encoding="utf-8") as f:
            f.write(base64.b64encode(raw.encode()).decode() if raw.strip() else "")

        index["countries"][cc] = {"mihomo_proxies": len(plist), "links": len(llist)}
        print(f"      {cc}: {len(plist)} proxies / {len(llist)} links")

    with open(OUT / "index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    # regenerate README country table
    readme = ROOT / "README.md"
    if readme.exists():
        table = ["| کشور | mihomo (WhiteVPN/Clash) | clash کامل | base64 (v2rayNG) | raw | پروکسی / لینک |",
                 "|---|---|---|---|---|---|"]
        for cc in countries:
            n = index["countries"][cc]
            cnt = f"{n['mihomo_proxies']} / {n['links']}"
            b64cell = f"[base64-{cc}.txt](subs/base64-{cc}.txt)" if n["links"] > 0 else "— (فقط mihomo)"
            rawcell = f"[raw-{cc}.txt](subs/raw-{cc}.txt)" if n["links"] > 0 else "—"
            table.append(
                f"| `{cc}` "
                f"| [mihomo-{cc}.yaml](subs/mihomo-{cc}.yaml) "
                f"| [clash-{cc}.yaml](subs/clash-{cc}.yaml) "
                f"| {b64cell} "
                f"| {rawcell} "
                f"| {cnt} |"
            )
        text = readme.read_text(encoding="utf-8")
        start, end = "<!-- COUNTRY-TABLE-START -->", "<!-- COUNTRY-TABLE-END -->"
        block = start + "\n" + "\n".join(table) + "\n" + end
        if start in text and end in text:
            text = re.sub(re.escape(start) + r".*?" + re.escape(end), block, text, flags=re.DOTALL)
            readme.write_text(text, encoding="utf-8")
            print("[4/4] README table updated")
        else:
            print("[4/4] README markers not found, skipped")
    print("DONE.")


if __name__ == "__main__":
    main()
