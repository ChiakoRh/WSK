# 📡 WSK — ساب تفکیک‌شده بر اساس کشور از روی WhiteDNS

سورس اصلی: https://github.com/iampedii/whitedns-sub (`mihomo.yaml` + `base64.txt`)
که ساب داخلی برنامه https://github.com/WhiteDNS/WhiteVPN هست.

این ریپو هر ۱ ساعت با گیت‌هاب اکشن ⏰ (`update.yml`) از ساب اصلی می‌خونه
و برای هر کشور یه ساب جدا می‌سازه، تا بشه تو برنامه‌های دیگه (v2rayNG، NekoBox، Clash، Streisand...)
هر کشور رو جدا وارد کرد — چیزی که WhiteVPN داخل خودش داره ولی بقیه برنامه‌ها ندارن.

## 🧭 فهرست

- [📂 فرمت‌ها](#formats)
- [🌐 سایت (کپی راحت لینک‌ها)](#site)
- [🔗 لینک مستقیم ساب‌ها](#direct)
- [🌍 لیست کشورها](#countries)
- [⚙️ اجرای دستی](#manual)
- [🙏 تشکر از سازنده اصلی](#thanks)

<a id="formats"></a>
## 📂 فرمت‌ها (برای هر کشور `CC`)

| فرمت | فایل | به چه دردی می‌خوره |
|---|---|---|
| 🟣 mihomo proxies-only | `subs/mihomo/mihomo-CC.yaml` | WhiteVPN، Mihomo، Clash (مثل فایل اصلی) |
| 🟠 clash کامل | `subs/clash/clash-CC.yaml` | Clash/Mihomo/Streisand — با proxy-group آماده |
| 🔵 base64 | `subs/base64/base64-CC.txt` | v2rayNG، NekoBox، FoXray (فرمت استاندارد ساب) |
| ⚪ raw | `subs/raw/raw-CC.txt` | لینک‌ها به صورت متنی، برای کپی دستی |

<a id="site"></a>
## 🌐 سایت (کپی راحت لینک‌ها)

به‌جای گشتن توی ریدمی، از سایت استفاده کن — جستجوی کشور، تب ۴ فرمت، دکمه کپی، فارسی/انگلیسی 👇

**https://chiakorh.github.io/WSK/**

<a id="direct"></a>
## 🔗 لینک مستقیم همه ساب‌ها

لینک mihomo کشور موردنظرت رو کپی کن و به‌عنوان Subscription توی برنامت اضافه کن 👇 بقیه فرمت‌ها (clash / base64 / raw) توی باکس‌های بازشونده پایین هستن 📦

<!-- DIRECT-LINKS-START -->
**🇦🇺 استرالیا (`AU`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-AU.yaml
```

**🇧🇪 BE (`BE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-BE.yaml
```

**🇨🇿 CZ (`CZ`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-CZ.yaml
```

**🇩🇪 آلمان (`DE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-DE.yaml
```

**🇫🇮 فنلاند (`FI`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-FI.yaml
```

**🇫🇷 فرانسه (`FR`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-FR.yaml
```

**🇬🇧 انگلیس (`GB`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-GB.yaml
```

**🇮🇹 ایتالیا (`IT`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-IT.yaml
```

**🇯🇵 ژاپن (`JP`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-JP.yaml
```

**🇰🇷 کره جنوبی (`KR`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-KR.yaml
```

**🇲🇾 مالزی (`MY`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-MY.yaml
```

**🇳🇱 هلند (`NL`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-NL.yaml
```

**❓ سایر (`OT`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-OT.yaml
```

**🇸🇪 سوئد (`SE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-SE.yaml
```

**🇸🇬 سنگاپور (`SG`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-SG.yaml
```

**🇺🇦 UA (`UA`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-UA.yaml
```

**🇺🇸 آمریکا (`US`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-US.yaml
```

**🇿🇦 آفریقای جنوبی (`ZA`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-ZA.yaml
```

<details>
<summary>🟠 لینک‌های clash کامل (18 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-AU.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-BE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-CZ.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-DE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-FI.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-FR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-GB.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-IT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-JP.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-KR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-MY.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-NL.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-OT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-SE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-SG.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-UA.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-US.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-ZA.yaml
```

</details>

<details>
<summary>🔵 لینک‌های base64 (15 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-AU.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-DE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-FI.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-FR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-GB.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-IT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-JP.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-KR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-NL.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-OT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-SE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-SG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-UA.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-US.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-ZA.txt
```

</details>

<details>
<summary>⚪ لینک‌های raw (15 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-AU.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-DE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-FI.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-FR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-GB.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-IT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-JP.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-KR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-NL.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-OT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-SE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-SG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-UA.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-US.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-ZA.txt
```

</details>
<!-- DIRECT-LINKS-END -->

<a id="countries"></a>
## 🌍 لیست کشورها (خودکار آپدیت میشه)

<!-- COUNTRY-TABLE-START -->
| 🏳️ | کشور | mihomo (WhiteVPN/Clash) | clash کامل | base64 (v2rayNG) | raw | پروکسی / لینک |
|---|---|---|---|---|---|---|
| 🇦🇺 | `AU` | [mihomo-AU.yaml](subs/mihomo/mihomo-AU.yaml) | [clash-AU.yaml](subs/clash/clash-AU.yaml) | [base64-AU.txt](subs/base64/base64-AU.txt) | [raw-AU.txt](subs/raw/raw-AU.txt) | 5 / 5 |
| 🇧🇪 | `BE` | [mihomo-BE.yaml](subs/mihomo/mihomo-BE.yaml) | [clash-BE.yaml](subs/clash/clash-BE.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇨🇿 | `CZ` | [mihomo-CZ.yaml](subs/mihomo/mihomo-CZ.yaml) | [clash-CZ.yaml](subs/clash/clash-CZ.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇩🇪 | `DE` | [mihomo-DE.yaml](subs/mihomo/mihomo-DE.yaml) | [clash-DE.yaml](subs/clash/clash-DE.yaml) | [base64-DE.txt](subs/base64/base64-DE.txt) | [raw-DE.txt](subs/raw/raw-DE.txt) | 16 / 12 |
| 🇫🇮 | `FI` | [mihomo-FI.yaml](subs/mihomo/mihomo-FI.yaml) | [clash-FI.yaml](subs/clash/clash-FI.yaml) | [base64-FI.txt](subs/base64/base64-FI.txt) | [raw-FI.txt](subs/raw/raw-FI.txt) | 3 / 2 |
| 🇫🇷 | `FR` | [mihomo-FR.yaml](subs/mihomo/mihomo-FR.yaml) | [clash-FR.yaml](subs/clash/clash-FR.yaml) | [base64-FR.txt](subs/base64/base64-FR.txt) | [raw-FR.txt](subs/raw/raw-FR.txt) | 15 / 6 |
| 🇬🇧 | `GB` | [mihomo-GB.yaml](subs/mihomo/mihomo-GB.yaml) | [clash-GB.yaml](subs/clash/clash-GB.yaml) | [base64-GB.txt](subs/base64/base64-GB.txt) | [raw-GB.txt](subs/raw/raw-GB.txt) | 17 / 14 |
| 🇮🇹 | `IT` | [mihomo-IT.yaml](subs/mihomo/mihomo-IT.yaml) | [clash-IT.yaml](subs/clash/clash-IT.yaml) | [base64-IT.txt](subs/base64/base64-IT.txt) | [raw-IT.txt](subs/raw/raw-IT.txt) | 2 / 2 |
| 🇯🇵 | `JP` | [mihomo-JP.yaml](subs/mihomo/mihomo-JP.yaml) | [clash-JP.yaml](subs/clash/clash-JP.yaml) | [base64-JP.txt](subs/base64/base64-JP.txt) | [raw-JP.txt](subs/raw/raw-JP.txt) | 14 / 9 |
| 🇰🇷 | `KR` | [mihomo-KR.yaml](subs/mihomo/mihomo-KR.yaml) | [clash-KR.yaml](subs/clash/clash-KR.yaml) | [base64-KR.txt](subs/base64/base64-KR.txt) | [raw-KR.txt](subs/raw/raw-KR.txt) | 8 / 4 |
| 🇲🇾 | `MY` | [mihomo-MY.yaml](subs/mihomo/mihomo-MY.yaml) | [clash-MY.yaml](subs/clash/clash-MY.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇳🇱 | `NL` | [mihomo-NL.yaml](subs/mihomo/mihomo-NL.yaml) | [clash-NL.yaml](subs/clash/clash-NL.yaml) | [base64-NL.txt](subs/base64/base64-NL.txt) | [raw-NL.txt](subs/raw/raw-NL.txt) | 22 / 15 |
| ❓ | `OT` | [mihomo-OT.yaml](subs/mihomo/mihomo-OT.yaml) | [clash-OT.yaml](subs/clash/clash-OT.yaml) | [base64-OT.txt](subs/base64/base64-OT.txt) | [raw-OT.txt](subs/raw/raw-OT.txt) | 1 / 32 |
| 🇸🇪 | `SE` | [mihomo-SE.yaml](subs/mihomo/mihomo-SE.yaml) | [clash-SE.yaml](subs/clash/clash-SE.yaml) | [base64-SE.txt](subs/base64/base64-SE.txt) | [raw-SE.txt](subs/raw/raw-SE.txt) | 3 / 3 |
| 🇸🇬 | `SG` | [mihomo-SG.yaml](subs/mihomo/mihomo-SG.yaml) | [clash-SG.yaml](subs/clash/clash-SG.yaml) | [base64-SG.txt](subs/base64/base64-SG.txt) | [raw-SG.txt](subs/raw/raw-SG.txt) | 9 / 7 |
| 🇺🇦 | `UA` | [mihomo-UA.yaml](subs/mihomo/mihomo-UA.yaml) | [clash-UA.yaml](subs/clash/clash-UA.yaml) | [base64-UA.txt](subs/base64/base64-UA.txt) | [raw-UA.txt](subs/raw/raw-UA.txt) | 1 / 1 |
| 🇺🇸 | `US` | [mihomo-US.yaml](subs/mihomo/mihomo-US.yaml) | [clash-US.yaml](subs/clash/clash-US.yaml) | [base64-US.txt](subs/base64/base64-US.txt) | [raw-US.txt](subs/raw/raw-US.txt) | 43 / 41 |
| 🇿🇦 | `ZA` | [mihomo-ZA.yaml](subs/mihomo/mihomo-ZA.yaml) | [clash-ZA.yaml](subs/clash/clash-ZA.yaml) | [base64-ZA.txt](subs/base64/base64-ZA.txt) | [raw-ZA.txt](subs/raw/raw-ZA.txt) | 2 / 2 |
<!-- COUNTRY-TABLE-END -->

<a id="manual"></a>
## ⚙️ اجرای دستی

```bash
pip install pyyaml
python split.py
```

<a id="thanks"></a>
## تشکر از سازنده اصلی 🙏

همه‌ی اعتبار این ساب‌ها برای سازنده‌ی اصلیه. این ریپو فقط ساب اصلی رو بر اساس کشور تفکیک می‌کنه و هیچ سروری از خودش نداره.

- **Pedi ([iampedii](https://github.com/iampedii))** — سازنده‌ی ساب اصلی: [iampedii/whitedns-sub](https://github.com/iampedii/whitedns-sub)
- تیم/سازمان **[WhiteDNS](https://github.com/WhiteDNS)** — سازنده‌ی WhiteVPN و ابزارهای WhiteDNS

اگه از این ساب‌ها استفاده می‌کنی، لطفاً به ریپوهای اصلی ستاره بده ⭐

### 🚀 پروژه‌های WhiteDNS / iampedii

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
