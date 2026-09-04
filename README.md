# WSK — ساب تفکیک‌شده بر اساس کشور از روی WhiteDNS

سورس اصلی: https://github.com/iampedii/whitedns-sub (`mihomo.yaml` + `base64.txt`)
که ساب داخلی برنامه https://github.com/WhiteDNS/WhiteVPN هست.

این ریپو هر ۳۰ دقیقه با گیت‌هاب اکشن (`update.yml`) از ساب اصلی می‌خونه
و برای هر کشور یه ساب جدا می‌سازه، تا بشه تو برنامه‌های دیگه (v2rayNG، NekoBox، Clash، Streisand...)
هر کشور رو جدا وارد کرد — چیزی که WhiteVPN داخل خودش داره ولی بقیه برنامه‌ها ندارن.

## فرمت‌ها (برای هر کشور `CC`)

| فرمت | فایل | به چه دردی می‌خوره |
|---|---|---|
| mihomo proxies-only | `subs/mihomo-CC.yaml` | WhiteVPN، Mihomo، Clash (مثل فایل اصلی) |
| clash کامل | `subs/clash-CC.yaml` | Clash/Mihomo/Streisand — با proxy-group آماده |
| base64 | `subs/base64-CC.txt` | v2rayNG، NekoBox، FoXray (فرمت استاندارد ساب) |
| raw | `subs/raw-CC.txt` | لینک‌ها به صورت متنی، برای کپی دستی |

لینک مستقیم:
`https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo-DE.yaml`

## لیست کشورها (خودکار آپدیت میشه)

<!-- COUNTRY-TABLE-START -->
| کشور | mihomo (WhiteVPN/Clash) | clash کامل | base64 (v2rayNG) | raw | پروکسی / لینک |
|---|---|---|---|---|---|
| `AL` | [mihomo-AL.yaml](subs/mihomo-AL.yaml) | [clash-AL.yaml](subs/clash-AL.yaml) | — (فقط mihomo) | — | 1 / 0 |
| `AT` | [mihomo-AT.yaml](subs/mihomo-AT.yaml) | [clash-AT.yaml](subs/clash-AT.yaml) | [base64-AT.txt](subs/base64-AT.txt) | [raw-AT.txt](subs/raw-AT.txt) | 2 / 2 |
| `AU` | [mihomo-AU.yaml](subs/mihomo-AU.yaml) | [clash-AU.yaml](subs/clash-AU.yaml) | [base64-AU.txt](subs/base64-AU.txt) | [raw-AU.txt](subs/raw-AU.txt) | 5 / 5 |
| `BR` | [mihomo-BR.yaml](subs/mihomo-BR.yaml) | [clash-BR.yaml](subs/clash-BR.yaml) | — (فقط mihomo) | — | 1 / 0 |
| `CA` | [mihomo-CA.yaml](subs/mihomo-CA.yaml) | [clash-CA.yaml](subs/clash-CA.yaml) | [base64-CA.txt](subs/base64-CA.txt) | [raw-CA.txt](subs/raw-CA.txt) | 7 / 7 |
| `DE` | [mihomo-DE.yaml](subs/mihomo-DE.yaml) | [clash-DE.yaml](subs/clash-DE.yaml) | [base64-DE.txt](subs/base64-DE.txt) | [raw-DE.txt](subs/raw-DE.txt) | 35 / 30 |
| `DK` | [mihomo-DK.yaml](subs/mihomo-DK.yaml) | [clash-DK.yaml](subs/clash-DK.yaml) | — (فقط mihomo) | — | 1 / 0 |
| `EC` | [mihomo-EC.yaml](subs/mihomo-EC.yaml) | [clash-EC.yaml](subs/clash-EC.yaml) | — (فقط mihomo) | — | 1 / 0 |
| `ES` | [mihomo-ES.yaml](subs/mihomo-ES.yaml) | [clash-ES.yaml](subs/clash-ES.yaml) | — (فقط mihomo) | — | 1 / 0 |
| `FI` | [mihomo-FI.yaml](subs/mihomo-FI.yaml) | [clash-FI.yaml](subs/clash-FI.yaml) | [base64-FI.txt](subs/base64-FI.txt) | [raw-FI.txt](subs/raw-FI.txt) | 5 / 5 |
| `FR` | [mihomo-FR.yaml](subs/mihomo-FR.yaml) | [clash-FR.yaml](subs/clash-FR.yaml) | [base64-FR.txt](subs/base64-FR.txt) | [raw-FR.txt](subs/raw-FR.txt) | 5 / 5 |
| `GB` | [mihomo-GB.yaml](subs/mihomo-GB.yaml) | [clash-GB.yaml](subs/clash-GB.yaml) | [base64-GB.txt](subs/base64-GB.txt) | [raw-GB.txt](subs/raw-GB.txt) | 51 / 47 |
| `GR` | [mihomo-GR.yaml](subs/mihomo-GR.yaml) | [clash-GR.yaml](subs/clash-GR.yaml) | — (فقط mihomo) | — | 2 / 0 |
| `HK` | [mihomo-HK.yaml](subs/mihomo-HK.yaml) | [clash-HK.yaml](subs/clash-HK.yaml) | [base64-HK.txt](subs/base64-HK.txt) | [raw-HK.txt](subs/raw-HK.txt) | 2 / 2 |
| `IE` | [mihomo-IE.yaml](subs/mihomo-IE.yaml) | [clash-IE.yaml](subs/clash-IE.yaml) | — (فقط mihomo) | — | 1 / 0 |
| `IT` | [mihomo-IT.yaml](subs/mihomo-IT.yaml) | [clash-IT.yaml](subs/clash-IT.yaml) | [base64-IT.txt](subs/base64-IT.txt) | [raw-IT.txt](subs/raw-IT.txt) | 7 / 6 |
| `JP` | [mihomo-JP.yaml](subs/mihomo-JP.yaml) | [clash-JP.yaml](subs/clash-JP.yaml) | [base64-JP.txt](subs/base64-JP.txt) | [raw-JP.txt](subs/raw-JP.txt) | 73 / 72 |
| `KR` | [mihomo-KR.yaml](subs/mihomo-KR.yaml) | [clash-KR.yaml](subs/clash-KR.yaml) | [base64-KR.txt](subs/base64-KR.txt) | [raw-KR.txt](subs/raw-KR.txt) | 7 / 7 |
| `KZ` | [mihomo-KZ.yaml](subs/mihomo-KZ.yaml) | [clash-KZ.yaml](subs/clash-KZ.yaml) | [base64-KZ.txt](subs/base64-KZ.txt) | [raw-KZ.txt](subs/raw-KZ.txt) | 3 / 3 |
| `LT` | [mihomo-LT.yaml](subs/mihomo-LT.yaml) | [clash-LT.yaml](subs/clash-LT.yaml) | [base64-LT.txt](subs/base64-LT.txt) | [raw-LT.txt](subs/raw-LT.txt) | 1 / 1 |
| `LV` | [mihomo-LV.yaml](subs/mihomo-LV.yaml) | [clash-LV.yaml](subs/clash-LV.yaml) | — (فقط mihomo) | — | 2 / 0 |
| `MY` | [mihomo-MY.yaml](subs/mihomo-MY.yaml) | [clash-MY.yaml](subs/clash-MY.yaml) | [base64-MY.txt](subs/base64-MY.txt) | [raw-MY.txt](subs/raw-MY.txt) | 5 / 5 |
| `NL` | [mihomo-NL.yaml](subs/mihomo-NL.yaml) | [clash-NL.yaml](subs/clash-NL.yaml) | [base64-NL.txt](subs/base64-NL.txt) | [raw-NL.txt](subs/raw-NL.txt) | 37 / 28 |
| `OT` | [mihomo-OT.yaml](subs/mihomo-OT.yaml) | [clash-OT.yaml](subs/clash-OT.yaml) | [base64-OT.txt](subs/base64-OT.txt) | [raw-OT.txt](subs/raw-OT.txt) | 3 / 7 |
| `PL` | [mihomo-PL.yaml](subs/mihomo-PL.yaml) | [clash-PL.yaml](subs/clash-PL.yaml) | [base64-PL.txt](subs/base64-PL.txt) | [raw-PL.txt](subs/raw-PL.txt) | 3 / 2 |
| `PS` | [mihomo-PS.yaml](subs/mihomo-PS.yaml) | [clash-PS.yaml](subs/clash-PS.yaml) | — (فقط mihomo) | — | 1 / 0 |
| `PT` | [mihomo-PT.yaml](subs/mihomo-PT.yaml) | [clash-PT.yaml](subs/clash-PT.yaml) | — (فقط mihomo) | — | 1 / 0 |
| `RO` | [mihomo-RO.yaml](subs/mihomo-RO.yaml) | [clash-RO.yaml](subs/clash-RO.yaml) | — (فقط mihomo) | — | 11 / 0 |
| `RU` | [mihomo-RU.yaml](subs/mihomo-RU.yaml) | [clash-RU.yaml](subs/clash-RU.yaml) | [base64-RU.txt](subs/base64-RU.txt) | [raw-RU.txt](subs/raw-RU.txt) | 5 / 5 |
| `SE` | [mihomo-SE.yaml](subs/mihomo-SE.yaml) | [clash-SE.yaml](subs/clash-SE.yaml) | [base64-SE.txt](subs/base64-SE.txt) | [raw-SE.txt](subs/raw-SE.txt) | 3 / 1 |
| `SG` | [mihomo-SG.yaml](subs/mihomo-SG.yaml) | [clash-SG.yaml](subs/clash-SG.yaml) | [base64-SG.txt](subs/base64-SG.txt) | [raw-SG.txt](subs/raw-SG.txt) | 80 / 80 |
| `TW` | [mihomo-TW.yaml](subs/mihomo-TW.yaml) | [clash-TW.yaml](subs/clash-TW.yaml) | [base64-TW.txt](subs/base64-TW.txt) | [raw-TW.txt](subs/raw-TW.txt) | 2 / 2 |
| `US` | [mihomo-US.yaml](subs/mihomo-US.yaml) | [clash-US.yaml](subs/clash-US.yaml) | [base64-US.txt](subs/base64-US.txt) | [raw-US.txt](subs/raw-US.txt) | 44 / 23 |
| `ZA` | [mihomo-ZA.yaml](subs/mihomo-ZA.yaml) | [clash-ZA.yaml](subs/clash-ZA.yaml) | [base64-ZA.txt](subs/base64-ZA.txt) | [raw-ZA.txt](subs/raw-ZA.txt) | 1 / 1 |
<!-- COUNTRY-TABLE-END -->

## اجرای دستی

```bash
pip install pyyaml
python split.py
```

## تشکر از سازنده اصلی 🙏

همه‌ی اعتبار این ساب‌ها برای سازنده‌ی اصلیه. این ریپو فقط ساب اصلی رو بر اساس کشور تفکیک می‌کنه و هیچ سروری از خودش نداره.

- **Pedi ([iampedii](https://github.com/iampedii))** — سازنده‌ی ساب اصلی: [iampedii/whitedns-sub](https://github.com/iampedii/whitedns-sub)
- تیم/سازمان **[WhiteDNS](https://github.com/WhiteDNS)** — سازنده‌ی WhiteVPN و ابزارهای WhiteDNS

اگه از این ساب‌ها استفاده می‌کنی، لطفاً به ریپوهای اصلی ستاره بده ⭐

### پروژه‌های WhiteDNS / iampedii

| پروژه | توضیح | لینک |
|---|---|---|
| WhiteVPN (Android) | VPN client مدرن اندروید با Mihomo — همین ساب، ساب داخلی این برنامه‌ست | https://github.com/WhiteDNS/WhiteVPN |
| WhiteVPN-Desktop | نسخه دسکتاپ WhiteVPN با همون موتور mihomo | https://github.com/WhiteDNS/WhiteVPN-Desktop |
| WhiteDNS-Android | DNS tunneling client اندروید (VPN و proxy) | https://github.com/WhiteDNS/WhiteDNS-Android |
| WhiteDNS-Wizard | ابزار CLI/TUI برای ساخت VPN با 3x-ui/Xray روی SSH | https://github.com/WhiteDNS/WhiteDNS-Wizard |
| WhiteDNS-Desktop | کلاینت دسکتاپ WhiteDNS | https://github.com/WhiteDNS/WhiteDNS-Desktop |
| WhiteAesther / Mobile | کلاینت‌های Aether (موتور ارتباط رمزنگاری‌شده) | https://github.com/WhiteDNS/WhiteAesther |
| CottenDNS | ابزار DNS تیم WhiteDNS | https://github.com/WhiteDNS/CottenDNS |
| WhiteDNS-cleanip-finder | پیدا کردن IP تمیز | https://github.com/WhiteDNS/WhiteDNS-cleanip-finder |
| IP-Range-Scout-Android | اسکن رنج IP برای DNS resolver | https://github.com/WhiteDNS/IP-Range-Scout-Android |
| range-scout | گرفتن رنج IP اپراتورها از RIPEstat و اسکن DNS | https://github.com/iampedii/range-scout |
| whitedns-sub (ساب اصلی) | ساب Mihomo/Clash/base64 که این ریپو ازش تفکیک می‌کنه | https://github.com/iampedii/whitedns-sub |

کانال تلگرام: [@whitedns](https://t.me/whitedns) — گروه: [@whitedns_group](https://t.me/whitedns_group)
