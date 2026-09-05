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

> اگه باز نشد، یه بار توی تنظیمات ریپو فعالش کن:
> `Settings → Pages → Deploy from a branch → main → /docs → Save`

<a id="direct"></a>
## 🔗 لینک مستقیم همه ساب‌ها

لینک mihomo کشور موردنظرت رو کپی کن و به‌عنوان Subscription توی برنامت اضافه کن 👇 بقیه فرمت‌ها (clash / base64 / raw) توی باکس‌های بازشونده پایین هستن 📦

<!-- DIRECT-LINKS-START -->
**🇦🇱 آلبانی (`AL`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-AL.yaml
```

**🇦🇹 اتریش (`AT`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-AT.yaml
```

**🇦🇺 استرالیا (`AU`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-AU.yaml
```

**🇧🇷 برزیل (`BR`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-BR.yaml
```

**🇨🇦 کانادا (`CA`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-CA.yaml
```

**🇩🇪 آلمان (`DE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-DE.yaml
```

**🇩🇰 دانمارک (`DK`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-DK.yaml
```

**🇪🇨 اکوادور (`EC`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-EC.yaml
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

**🇬🇷 یونان (`GR`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-GR.yaml
```

**🇭🇰 هنگ‌کنگ (`HK`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-HK.yaml
```

**🇮🇪 ایرلند (`IE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-IE.yaml
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

**🇰🇿 قزاقستان (`KZ`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-KZ.yaml
```

**🇱🇹 لیتوانی (`LT`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-LT.yaml
```

**🇱🇻 لتونی (`LV`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-LV.yaml
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

**🇵🇸 فلسطین (`PS`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-PS.yaml
```

**🇵🇹 پرتغال (`PT`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-PT.yaml
```

**🇷🇴 رومانی (`RO`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-RO.yaml
```

**🇷🇺 روسیه (`RU`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-RU.yaml
```

**🇸🇪 سوئد (`SE`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-SE.yaml
```

**🇸🇬 سنگاپور (`SG`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-SG.yaml
```

**🇹🇼 تایوان (`TW`)**

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/mihomo/mihomo-TW.yaml
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
<summary>🟠 لینک‌های clash کامل (34 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-AL.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-AT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-AU.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-BR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-CA.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-DE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-DK.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-EC.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-ES.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-FI.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-FR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-GB.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-GR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-HK.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-IE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-IT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-JP.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-KR.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-KZ.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-LT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-LV.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-MY.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-NL.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-OT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-PL.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-PS.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-PT.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-RO.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-RU.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-SE.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-SG.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-TW.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-US.yaml
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/clash/clash-ZA.yaml
```

</details>

<details>
<summary>🔵 لینک‌های base64 (23 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-AT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-AU.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-CA.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-DE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-FI.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-FR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-GB.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-HK.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-IT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-JP.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-KR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-KZ.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-LT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-MY.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-NL.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-OT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-PL.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-RU.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-SE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-SG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-TW.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-US.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/base64/base64-ZA.txt
```

</details>

<details>
<summary>⚪ لینک‌های raw (23 کشور)</summary>

```
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-AT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-AU.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-CA.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-DE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-FI.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-FR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-GB.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-HK.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-IT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-JP.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-KR.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-KZ.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-LT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-MY.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-NL.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-OT.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-PL.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-RU.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-SE.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-SG.txt
https://raw.githubusercontent.com/ChiakoRh/WSK/main/subs/raw/raw-TW.txt
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
| 🇦🇱 | `AL` | [mihomo-AL.yaml](subs/mihomo/mihomo-AL.yaml) | [clash-AL.yaml](subs/clash/clash-AL.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇦🇹 | `AT` | [mihomo-AT.yaml](subs/mihomo/mihomo-AT.yaml) | [clash-AT.yaml](subs/clash/clash-AT.yaml) | [base64-AT.txt](subs/base64/base64-AT.txt) | [raw-AT.txt](subs/raw/raw-AT.txt) | 2 / 2 |
| 🇦🇺 | `AU` | [mihomo-AU.yaml](subs/mihomo/mihomo-AU.yaml) | [clash-AU.yaml](subs/clash/clash-AU.yaml) | [base64-AU.txt](subs/base64/base64-AU.txt) | [raw-AU.txt](subs/raw/raw-AU.txt) | 5 / 5 |
| 🇧🇷 | `BR` | [mihomo-BR.yaml](subs/mihomo/mihomo-BR.yaml) | [clash-BR.yaml](subs/clash/clash-BR.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇨🇦 | `CA` | [mihomo-CA.yaml](subs/mihomo/mihomo-CA.yaml) | [clash-CA.yaml](subs/clash/clash-CA.yaml) | [base64-CA.txt](subs/base64/base64-CA.txt) | [raw-CA.txt](subs/raw/raw-CA.txt) | 7 / 7 |
| 🇩🇪 | `DE` | [mihomo-DE.yaml](subs/mihomo/mihomo-DE.yaml) | [clash-DE.yaml](subs/clash/clash-DE.yaml) | [base64-DE.txt](subs/base64/base64-DE.txt) | [raw-DE.txt](subs/raw/raw-DE.txt) | 35 / 30 |
| 🇩🇰 | `DK` | [mihomo-DK.yaml](subs/mihomo/mihomo-DK.yaml) | [clash-DK.yaml](subs/clash/clash-DK.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇪🇨 | `EC` | [mihomo-EC.yaml](subs/mihomo/mihomo-EC.yaml) | [clash-EC.yaml](subs/clash/clash-EC.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇪🇸 | `ES` | [mihomo-ES.yaml](subs/mihomo/mihomo-ES.yaml) | [clash-ES.yaml](subs/clash/clash-ES.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇫🇮 | `FI` | [mihomo-FI.yaml](subs/mihomo/mihomo-FI.yaml) | [clash-FI.yaml](subs/clash/clash-FI.yaml) | [base64-FI.txt](subs/base64/base64-FI.txt) | [raw-FI.txt](subs/raw/raw-FI.txt) | 5 / 5 |
| 🇫🇷 | `FR` | [mihomo-FR.yaml](subs/mihomo/mihomo-FR.yaml) | [clash-FR.yaml](subs/clash/clash-FR.yaml) | [base64-FR.txt](subs/base64/base64-FR.txt) | [raw-FR.txt](subs/raw/raw-FR.txt) | 5 / 5 |
| 🇬🇧 | `GB` | [mihomo-GB.yaml](subs/mihomo/mihomo-GB.yaml) | [clash-GB.yaml](subs/clash/clash-GB.yaml) | [base64-GB.txt](subs/base64/base64-GB.txt) | [raw-GB.txt](subs/raw/raw-GB.txt) | 51 / 47 |
| 🇬🇷 | `GR` | [mihomo-GR.yaml](subs/mihomo/mihomo-GR.yaml) | [clash-GR.yaml](subs/clash/clash-GR.yaml) | — (فقط mihomo) | — | 2 / 0 |
| 🇭🇰 | `HK` | [mihomo-HK.yaml](subs/mihomo/mihomo-HK.yaml) | [clash-HK.yaml](subs/clash/clash-HK.yaml) | [base64-HK.txt](subs/base64/base64-HK.txt) | [raw-HK.txt](subs/raw/raw-HK.txt) | 2 / 2 |
| 🇮🇪 | `IE` | [mihomo-IE.yaml](subs/mihomo/mihomo-IE.yaml) | [clash-IE.yaml](subs/clash/clash-IE.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇮🇹 | `IT` | [mihomo-IT.yaml](subs/mihomo/mihomo-IT.yaml) | [clash-IT.yaml](subs/clash/clash-IT.yaml) | [base64-IT.txt](subs/base64/base64-IT.txt) | [raw-IT.txt](subs/raw/raw-IT.txt) | 7 / 6 |
| 🇯🇵 | `JP` | [mihomo-JP.yaml](subs/mihomo/mihomo-JP.yaml) | [clash-JP.yaml](subs/clash/clash-JP.yaml) | [base64-JP.txt](subs/base64/base64-JP.txt) | [raw-JP.txt](subs/raw/raw-JP.txt) | 73 / 72 |
| 🇰🇷 | `KR` | [mihomo-KR.yaml](subs/mihomo/mihomo-KR.yaml) | [clash-KR.yaml](subs/clash/clash-KR.yaml) | [base64-KR.txt](subs/base64/base64-KR.txt) | [raw-KR.txt](subs/raw/raw-KR.txt) | 7 / 7 |
| 🇰🇿 | `KZ` | [mihomo-KZ.yaml](subs/mihomo/mihomo-KZ.yaml) | [clash-KZ.yaml](subs/clash/clash-KZ.yaml) | [base64-KZ.txt](subs/base64/base64-KZ.txt) | [raw-KZ.txt](subs/raw/raw-KZ.txt) | 3 / 3 |
| 🇱🇹 | `LT` | [mihomo-LT.yaml](subs/mihomo/mihomo-LT.yaml) | [clash-LT.yaml](subs/clash/clash-LT.yaml) | [base64-LT.txt](subs/base64/base64-LT.txt) | [raw-LT.txt](subs/raw/raw-LT.txt) | 1 / 1 |
| 🇱🇻 | `LV` | [mihomo-LV.yaml](subs/mihomo/mihomo-LV.yaml) | [clash-LV.yaml](subs/clash/clash-LV.yaml) | — (فقط mihomo) | — | 2 / 0 |
| 🇲🇾 | `MY` | [mihomo-MY.yaml](subs/mihomo/mihomo-MY.yaml) | [clash-MY.yaml](subs/clash/clash-MY.yaml) | [base64-MY.txt](subs/base64/base64-MY.txt) | [raw-MY.txt](subs/raw/raw-MY.txt) | 5 / 5 |
| 🇳🇱 | `NL` | [mihomo-NL.yaml](subs/mihomo/mihomo-NL.yaml) | [clash-NL.yaml](subs/clash/clash-NL.yaml) | [base64-NL.txt](subs/base64/base64-NL.txt) | [raw-NL.txt](subs/raw/raw-NL.txt) | 37 / 28 |
| ❓ | `OT` | [mihomo-OT.yaml](subs/mihomo/mihomo-OT.yaml) | [clash-OT.yaml](subs/clash/clash-OT.yaml) | [base64-OT.txt](subs/base64/base64-OT.txt) | [raw-OT.txt](subs/raw/raw-OT.txt) | 3 / 7 |
| 🇵🇱 | `PL` | [mihomo-PL.yaml](subs/mihomo/mihomo-PL.yaml) | [clash-PL.yaml](subs/clash/clash-PL.yaml) | [base64-PL.txt](subs/base64/base64-PL.txt) | [raw-PL.txt](subs/raw/raw-PL.txt) | 3 / 2 |
| 🇵🇸 | `PS` | [mihomo-PS.yaml](subs/mihomo/mihomo-PS.yaml) | [clash-PS.yaml](subs/clash/clash-PS.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇵🇹 | `PT` | [mihomo-PT.yaml](subs/mihomo/mihomo-PT.yaml) | [clash-PT.yaml](subs/clash/clash-PT.yaml) | — (فقط mihomo) | — | 1 / 0 |
| 🇷🇴 | `RO` | [mihomo-RO.yaml](subs/mihomo/mihomo-RO.yaml) | [clash-RO.yaml](subs/clash/clash-RO.yaml) | — (فقط mihomo) | — | 11 / 0 |
| 🇷🇺 | `RU` | [mihomo-RU.yaml](subs/mihomo/mihomo-RU.yaml) | [clash-RU.yaml](subs/clash/clash-RU.yaml) | [base64-RU.txt](subs/base64/base64-RU.txt) | [raw-RU.txt](subs/raw/raw-RU.txt) | 5 / 5 |
| 🇸🇪 | `SE` | [mihomo-SE.yaml](subs/mihomo/mihomo-SE.yaml) | [clash-SE.yaml](subs/clash/clash-SE.yaml) | [base64-SE.txt](subs/base64/base64-SE.txt) | [raw-SE.txt](subs/raw/raw-SE.txt) | 3 / 1 |
| 🇸🇬 | `SG` | [mihomo-SG.yaml](subs/mihomo/mihomo-SG.yaml) | [clash-SG.yaml](subs/clash/clash-SG.yaml) | [base64-SG.txt](subs/base64/base64-SG.txt) | [raw-SG.txt](subs/raw/raw-SG.txt) | 80 / 80 |
| 🇹🇼 | `TW` | [mihomo-TW.yaml](subs/mihomo/mihomo-TW.yaml) | [clash-TW.yaml](subs/clash/clash-TW.yaml) | [base64-TW.txt](subs/base64/base64-TW.txt) | [raw-TW.txt](subs/raw/raw-TW.txt) | 2 / 2 |
| 🇺🇸 | `US` | [mihomo-US.yaml](subs/mihomo/mihomo-US.yaml) | [clash-US.yaml](subs/clash/clash-US.yaml) | [base64-US.txt](subs/base64/base64-US.txt) | [raw-US.txt](subs/raw/raw-US.txt) | 44 / 23 |
| 🇿🇦 | `ZA` | [mihomo-ZA.yaml](subs/mihomo/mihomo-ZA.yaml) | [clash-ZA.yaml](subs/clash/clash-ZA.yaml) | [base64-ZA.txt](subs/base64/base64-ZA.txt) | [raw-ZA.txt](subs/raw/raw-ZA.txt) | 1 / 1 |
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
