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
**🇦🇪 AE (`AE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-AE.yaml
```

**🇦🇹 اتریش (`AT`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-AT.yaml
```

**🇧🇪 BE (`BE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-BE.yaml
```

**🇧🇬 BG (`BG`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-BG.yaml
```

**🇧🇷 برزیل (`BR`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-BR.yaml
```

**🇨🇦 کانادا (`CA`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-CA.yaml
```

**🇨🇭 CH (`CH`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-CH.yaml
```

**🇩🇪 آلمان (`DE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-DE.yaml
```

**🇪🇬 EG (`EG`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-EG.yaml
```

**🇪🇸 اسپانیا (`ES`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-ES.yaml
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

**🇮🇳 IN (`IN`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-IN.yaml
```

**🇮🇹 ایتالیا (`IT`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-IT.yaml
```

**🇯🇲 JM (`JM`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-JM.yaml
```

**🇯🇵 ژاپن (`JP`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-JP.yaml
```

**🇰🇷 کره جنوبی (`KR`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-KR.yaml
```

**🇰🇿 قزاقستان (`KZ`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-KZ.yaml
```

**🇱🇹 لیتوانی (`LT`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-LT.yaml
```

**🇱🇺 LU (`LU`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-LU.yaml
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

**🇵🇱 لهستان (`PL`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-PL.yaml
```

**🇷🇴 رومانی (`RO`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-RO.yaml
```

**🇷🇸 RS (`RS`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-RS.yaml
```

**🇸🇪 سوئد (`SE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-SE.yaml
```

**🇸🇬 سنگاپور (`SG`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-SG.yaml
```

**🇹🇷 TR (`TR`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-TR.yaml
```

**🇺🇸 آمریکا (`US`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-US.yaml
```

<details>
<summary>🟠 لینک‌های clash کامل (31 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-AE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-AT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-BE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-BG.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-BR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-CA.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-CH.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-DE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-EG.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-ES.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-FI.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-FR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-GB.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-IN.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-IT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-JM.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-JP.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-KR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-KZ.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-LT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-LU.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-MY.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-NL.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-OT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-PL.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-RO.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-RS.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-SE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-SG.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-TR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-US.yaml
```

</details>

<details>
<summary>🔵 لینک‌های base64 (26 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-AE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-AT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-BE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-BG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-BR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-CA.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-CH.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-DE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-EG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-FI.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-FR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-GB.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-IN.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-IT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-JM.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-JP.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-KZ.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-LT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-LU.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-MY.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-NL.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-OT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-SE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-SG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-TR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-US.txt
```

</details>

<details>
<summary>⚪ لینک‌های raw (26 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-AE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-AT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-BE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-BG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-BR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-CA.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-CH.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-DE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-EG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-FI.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-FR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-GB.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-IN.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-IT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-JM.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-JP.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-KZ.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-LT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-LU.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-MY.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-NL.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-OT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-SE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-SG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-TR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-US.txt
```

</details>
<!-- DIRECT-LINKS-END -->

<a id="countries"></a>
## 🌍 لیست کشورها (خودکار آپدیت میشه)

<!-- COUNTRY-TABLE-START -->
| 🏳️ | کشور | mihomo (WhiteVPN/Clash) | clash کامل | base64 (v2rayNG) | raw | پروکسی / لینک |
|---|---|---|---|---|---|---|
| 🇦🇪 | `AE` | [mihomo-AE.yaml](subs/mihomo/mihomo-AE.yaml) | [clash-AE.yaml](subs/clash/clash-AE.yaml) | [base64-AE.txt](subs/base64/base64-AE.txt) | [raw-AE.txt](subs/raw/raw-AE.txt) | 1 / 1 |
| 🇦🇹 | `AT` | [mihomo-AT.yaml](subs/mihomo/mihomo-AT.yaml) | [clash-AT.yaml](subs/clash/clash-AT.yaml) | [base64-AT.txt](subs/base64/base64-AT.txt) | [raw-AT.txt](subs/raw/raw-AT.txt) | 2 / 2 |
| 🇧🇪 | `BE` | [mihomo-BE.yaml](subs/mihomo/mihomo-BE.yaml) | [clash-BE.yaml](subs/clash/clash-BE.yaml) | [base64-BE.txt](subs/base64/base64-BE.txt) | [raw-BE.txt](subs/raw/raw-BE.txt) | 1 / 1 |
| 🇧🇬 | `BG` | [mihomo-BG.yaml](subs/mihomo/mihomo-BG.yaml) | [clash-BG.yaml](subs/clash/clash-BG.yaml) | [base64-BG.txt](subs/base64/base64-BG.txt) | [raw-BG.txt](subs/raw/raw-BG.txt) | 2 / 1 |
| 🇧🇷 | `BR` | [mihomo-BR.yaml](subs/mihomo/mihomo-BR.yaml) | [clash-BR.yaml](subs/clash/clash-BR.yaml) | [base64-BR.txt](subs/base64/base64-BR.txt) | [raw-BR.txt](subs/raw/raw-BR.txt) | 1 / 1 |
| 🇨🇦 | `CA` | [mihomo-CA.yaml](subs/mihomo/mihomo-CA.yaml) | [clash-CA.yaml](subs/clash/clash-CA.yaml) | [base64-CA.txt](subs/base64/base64-CA.txt) | [raw-CA.txt](subs/raw/raw-CA.txt) | 6 / 6 |
| 🇨🇭 | `CH` | [mihomo-CH.yaml](subs/mihomo/mihomo-CH.yaml) | [clash-CH.yaml](subs/clash/clash-CH.yaml) | [base64-CH.txt](subs/base64/base64-CH.txt) | [raw-CH.txt](subs/raw/raw-CH.txt) | 11 / 11 |
| 🇩🇪 | `DE` | [mihomo-DE.yaml](subs/mihomo/mihomo-DE.yaml) | [clash-DE.yaml](subs/clash/clash-DE.yaml) | [base64-DE.txt](subs/base64/base64-DE.txt) | [raw-DE.txt](subs/raw/raw-DE.txt) | 99 / 98 |
| 🇪🇬 | `EG` | [mihomo-EG.yaml](subs/mihomo/mihomo-EG.yaml) | [clash-EG.yaml](subs/clash/clash-EG.yaml) | [base64-EG.txt](subs/base64/base64-EG.txt) | [raw-EG.txt](subs/raw/raw-EG.txt) | 1 / 1 |
| 🇪🇸 | `ES` | [mihomo-ES.yaml](subs/mihomo/mihomo-ES.yaml) | [clash-ES.yaml](subs/clash/clash-ES.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇫🇮 | `FI` | [mihomo-FI.yaml](subs/mihomo/mihomo-FI.yaml) | [clash-FI.yaml](subs/clash/clash-FI.yaml) | [base64-FI.txt](subs/base64/base64-FI.txt) | [raw-FI.txt](subs/raw/raw-FI.txt) | 4 / 4 |
| 🇫🇷 | `FR` | [mihomo-FR.yaml](subs/mihomo/mihomo-FR.yaml) | [clash-FR.yaml](subs/clash/clash-FR.yaml) | [base64-FR.txt](subs/base64/base64-FR.txt) | [raw-FR.txt](subs/raw/raw-FR.txt) | 3 / 3 |
| 🇬🇧 | `GB` | [mihomo-GB.yaml](subs/mihomo/mihomo-GB.yaml) | [clash-GB.yaml](subs/clash/clash-GB.yaml) | [base64-GB.txt](subs/base64/base64-GB.txt) | [raw-GB.txt](subs/raw/raw-GB.txt) | 15 / 14 |
| 🇮🇳 | `IN` | [mihomo-IN.yaml](subs/mihomo/mihomo-IN.yaml) | [clash-IN.yaml](subs/clash/clash-IN.yaml) | [base64-IN.txt](subs/base64/base64-IN.txt) | [raw-IN.txt](subs/raw/raw-IN.txt) | 3 / 3 |
| 🇮🇹 | `IT` | [mihomo-IT.yaml](subs/mihomo/mihomo-IT.yaml) | [clash-IT.yaml](subs/clash/clash-IT.yaml) | [base64-IT.txt](subs/base64/base64-IT.txt) | [raw-IT.txt](subs/raw/raw-IT.txt) | 6 / 6 |
| 🇯🇲 | `JM` | [mihomo-JM.yaml](subs/mihomo/mihomo-JM.yaml) | [clash-JM.yaml](subs/clash/clash-JM.yaml) | [base64-JM.txt](subs/base64/base64-JM.txt) | [raw-JM.txt](subs/raw/raw-JM.txt) | 1 / 1 |
| 🇯🇵 | `JP` | [mihomo-JP.yaml](subs/mihomo/mihomo-JP.yaml) | [clash-JP.yaml](subs/clash/clash-JP.yaml) | [base64-JP.txt](subs/base64/base64-JP.txt) | [raw-JP.txt](subs/raw/raw-JP.txt) | 60 / 57 |
| 🇰🇷 | `KR` | [mihomo-KR.yaml](subs/mihomo/mihomo-KR.yaml) | [clash-KR.yaml](subs/clash/clash-KR.yaml) | — (فقط mihomo) | — | 3 / 0 |
| 🇰🇿 | `KZ` | [mihomo-KZ.yaml](subs/mihomo/mihomo-KZ.yaml) | [clash-KZ.yaml](subs/clash/clash-KZ.yaml) | [base64-KZ.txt](subs/base64/base64-KZ.txt) | [raw-KZ.txt](subs/raw/raw-KZ.txt) | 4 / 4 |
| 🇱🇹 | `LT` | [mihomo-LT.yaml](subs/mihomo/mihomo-LT.yaml) | [clash-LT.yaml](subs/clash/clash-LT.yaml) | [base64-LT.txt](subs/base64/base64-LT.txt) | [raw-LT.txt](subs/raw/raw-LT.txt) | 2 / 2 |
| 🇱🇺 | `LU` | [mihomo-LU.yaml](subs/mihomo/mihomo-LU.yaml) | [clash-LU.yaml](subs/clash/clash-LU.yaml) | [base64-LU.txt](subs/base64/base64-LU.txt) | [raw-LU.txt](subs/raw/raw-LU.txt) | 2 / 2 |
| 🇲🇾 | `MY` | [mihomo-MY.yaml](subs/mihomo/mihomo-MY.yaml) | [clash-MY.yaml](subs/clash/clash-MY.yaml) | [base64-MY.txt](subs/base64/base64-MY.txt) | [raw-MY.txt](subs/raw/raw-MY.txt) | 6 / 3 |
| 🇳🇱 | `NL` | [mihomo-NL.yaml](subs/mihomo/mihomo-NL.yaml) | [clash-NL.yaml](subs/clash/clash-NL.yaml) | [base64-NL.txt](subs/base64/base64-NL.txt) | [raw-NL.txt](subs/raw/raw-NL.txt) | 24 / 16 |
| ❓ | `OT` | [mihomo-OT.yaml](subs/mihomo/mihomo-OT.yaml) | [clash-OT.yaml](subs/clash/clash-OT.yaml) | [base64-OT.txt](subs/base64/base64-OT.txt) | [raw-OT.txt](subs/raw/raw-OT.txt) | 0 / 10 |
| 🇵🇱 | `PL` | [mihomo-PL.yaml](subs/mihomo/mihomo-PL.yaml) | [clash-PL.yaml](subs/clash/clash-PL.yaml) | — (فقط mihomo) | — | 2 / 0 |
| 🇷🇴 | `RO` | [mihomo-RO.yaml](subs/mihomo/mihomo-RO.yaml) | [clash-RO.yaml](subs/clash/clash-RO.yaml) | — (فقط mihomo) | — | 11 / 0 |
| 🇷🇸 | `RS` | [mihomo-RS.yaml](subs/mihomo/mihomo-RS.yaml) | [clash-RS.yaml](subs/clash/clash-RS.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇸🇪 | `SE` | [mihomo-SE.yaml](subs/mihomo/mihomo-SE.yaml) | [clash-SE.yaml](subs/clash/clash-SE.yaml) | [base64-SE.txt](subs/base64/base64-SE.txt) | [raw-SE.txt](subs/raw/raw-SE.txt) | 1 / 1 |
| 🇸🇬 | `SG` | [mihomo-SG.yaml](subs/mihomo/mihomo-SG.yaml) | [clash-SG.yaml](subs/clash/clash-SG.yaml) | [base64-SG.txt](subs/base64/base64-SG.txt) | [raw-SG.txt](subs/raw/raw-SG.txt) | 19 / 19 |
| 🇹🇷 | `TR` | [mihomo-TR.yaml](subs/mihomo/mihomo-TR.yaml) | [clash-TR.yaml](subs/clash/clash-TR.yaml) | [base64-TR.txt](subs/base64/base64-TR.txt) | [raw-TR.txt](subs/raw/raw-TR.txt) | 1 / 1 |
| 🇺🇸 | `US` | [mihomo-US.yaml](subs/mihomo/mihomo-US.yaml) | [clash-US.yaml](subs/clash/clash-US.yaml) | [base64-US.txt](subs/base64/base64-US.txt) | [raw-US.txt](subs/raw/raw-US.txt) | 47 / 23 |
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
