<div align="center">

[中文](/README.md) · **English** · [Changelog](/assets/README_Update.md) · [Website · GLOBAL](https://awavenue.top) · [Website · CHINA](https://doc.awads.cc)

<br/>

# AWAvenue Ads Rule

<img src="https://img.jsdelivr.com/raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/assets/assets.png" alt="AWAvenue" width="720">

<p><b>干掉所有无良广告<br>Eliminate All Malicious Ads</b></p>

<br/>

<img src="https://img.shields.io/github/stars/TG-Twilight/AWAvenue-Ads-Rule?style=for-the-badge&colorA=FFEBEB&colorB=FFD9DC&logo=github&logoColor=pink" alt="Stars">
<a href="https://t.me/AWAvenueAdsRule"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=Channel&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueAdsRule" alt="Telegram Channel"></a>
<a href="https://t.me/AWAvenueAdsChat"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=Group&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueAdsChat" alt="Telegram Group"></a>
<a href="https://afdian.com/a/AdsRule" target="_blank"><img src="https://img.shields.io/badge/Sponsor-ffd700?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white&labelColor=ff9800" alt="Sponsor"></a>

<br/>

<p>
  <a href="https://www.star-history.com/tg-twilight/awavenue-ads-rule">
    <img src="https://api.star-history.com/badge?repo=TG-Twilight/AWAvenue-Ads-Rule&theme=dark" alt="Star History Rank">
  </a>
</p>

</div>

---

## About

An upstream source for many excellent ad-blocking lists, and one of the best open-source filter lists in the community — balancing ad blocking, privacy protection, and bandwidth savings.

Compared with lists that balloon to tens of thousands of rules, AWAvenue focuses on:

| Strength | Why it matters |
|:--------:|----------------|
| Compact size | Minimal footprint, faster to load |
| High hit rate | Tuned for common ad SDKs and real-world cases |
| Hardware-friendly | Runs well on routers and low-end devices |
| Easy deploy | Subscribe once, benefit across devices |

After subscribing, you will usually notice:

- Annoying “shake-to-interact” ads disappear
- Subscription feeds and in-/end-of-article ad streams fail to load
- Autoplay video ads are gone
- Boot ads on TV boxes / smart TVs vanish
- A bit more free storage on your phone (ad assets blocked from downloading)

Compared with per-app ad removal, network-layer filtering costs less, covers more (e.g. router deployment), and stays mostly invisible while you use your apps as usual.

> As of July 2025, we can block over 90% of ad SDK traffic on Teyvat.

> [!IMPORTANT]
> Before opening an Issue or asking in the group, please read the [FAQ](https://awavenue.top/Knowledge.html#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98-%E4%B8%8E%E7%AD%94%E7%96%91). Many common questions are already answered there.

---

## How it works

Blocks communication between ad SDKs and their servers at the **network layer**, so ads never load properly.

This is completely different from accessibility-based auto-click tools (e.g. “Li x Tiao” style apps) — **import into those tools is not supported**.

If ads still show after subscribing, or you hit false positives, feedback is welcome.

---

## Subscription

For **AdGuard Home / AdGuard / AdGuard DNS** and other tools that support Adblock syntax:

| Mirror | Link |
|:------:|------|
| GitHub Raw | [Subscribe](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt) |
| Tianming CFCDN | [Subscribe](https://github.boki.moe/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt) |
| jsDelivr (gcore) | [Subscribe](https://gcore.jsdelivr.net/gh/TG-Twilight/AWAvenue-Ads-Rule@main/AWAvenue-Ads-Rule.txt) |
| ghproxy | [Subscribe](https://ghfast.top/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt) |

More formats and mirrors → [Official site · Subscription](https://awavenue.top/Sub.html)

---

## Supported tools

Compatible with most ad blockers and proxy clients, for example:

| Type | Tools |
|------|--------|
| Adblock syntax | [AdGuard (iOS/Android) / Home / DNS](https://awavenue.top/Sub.html#adguard-ios-android-home-dns-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5) and similar (not AdGuard for Chrome) |
| Hosts | [AdAway, Dasheng Purification](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5), etc. |
| OpenWrt & friends | [Mosdns](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=%E6%8E%A5%EF%BC%88.list%E6%A0%BC%E5%BC%8F%EF%BC%89-,Mosdns%20V5%20%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5,-AdClose%20rule%E6%A0%BC%E5%BC%8F), [Dnsmasq](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=Dnsmasq%E6%A0%BC%E5%BC%8F%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%88.conf%E6%A0%BC%E5%BC%8F%EF%BC%89), [Ad Blocker Master Plus+, DNS Adblock](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5) |
| Proxy clients | [Clash Meta](https://awavenue.top/Sub.html#clash-%E8%A7%84%E5%88%99%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5), [Quantumult X](https://awavenue.top/Sub.html#clash-%E8%A7%84%E5%88%99%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=QuantumultX%20%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%88.list%E6%A0%BC%E5%BC%8F%EF%BC%89), Shadowrocket, Surge, Surfboard, etc. |
| Router OS | RouterOS (`240.0.0.1` / `0.0.0.0` formats) |

<details>
<summary><b>Recommended ad-blocking tools</b></summary>

<br/>

- [**AdGuard Home**](https://github.com/AdguardTeam/AdGuardHome) — Ideal on a router; AWAvenue is in the official AdGuard list (“Choose from list”)  
- [**AdGuard**](https://adguard.com/) — Android / Windows / Mac / iOS  
- [**AdAway**](https://adaway.org/) — Open-source Android blocker using hosts  
- [**AdGuard DNS**](https://adguard-dns.io/en/welcome.html) — Custom DNS; rule is in AdGuard DNS Filters  
- [**AdGuard Home For Magisk**](https://github.com/twoone-3/AdGuardHomeForMagisk) — Magisk build of AGH  
- [**AdClose**](https://github.com/zjyzip/AdClose) — Xposed module that hooks common ads; ships with AWAvenue (thanks @zjyzip)  
- [**geosite (@elysias123)**](https://github.com/elysias123/geosite) — For V2Ray / Xray / mihomo / hysteria / Trojan-Go / leaf, etc., with an AWAvenue category  

</details>

---

## How to use

Please start with the official guide → [**Knowledge base**](https://awavenue.top/Knowledge.html)

This is a personal project, maintained as time allows. Issues and PRs are welcome. Questions? Join [秋風がく山道](https://t.me/AWAvenueAdsChat) and ask politely.

---

## Sponsors

### [XTCloud — Travel the world, high-speed connectivity](https://xtyun.co/#/register?code=M1w4rjdl)

<div align="center">

<table align="center" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td>
      <a href="https://www.cloudflare.com/" target="_blank" title="Cloudflare provides fast, secure, and reliable global network and security services.">
        <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/CLOUDFLARE/card-cloudflare.svg" alt="Cloudflare" width="360" height="110" title="Cloudflare provides fast, secure, and reliable global network and security services.">
      </a>
    </td>
    <td>
      <a href="https://1password.com/" target="_blank" title="1Password provides secure, easy-to-use password management with multi-device sync.">
        <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/1Password/card-1password.svg" alt="1Password" width="360" height="110" title="1Password provides secure, easy-to-use password management with multi-device sync.">
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://zmto.com/" target="_blank" title="ZMTO provides secure, reliable, and scalable cloud infrastructure and VPS hosting.">
        <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/zmto/card-zmto.svg" alt="ZMTO" width="360" height="110" title="ZMTO provides secure, reliable, and scalable cloud infrastructure and VPS hosting.">
      </a>
    </td>
    <td>
      <a href="https://termius.com/" target="_blank" title="Termius provides a secure, reliable, and collaborative SSH client.">
        <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/Termius/card-termius.svg" alt="Termius" width="360" height="110" title="Termius provides a secure, reliable, and collaborative SSH client.">
      </a>
    </td>
  </tr>
</table>

</div>

---

<details>
<summary><b>Star History</b> (take a peek if it’s up — often isn’t)</summary>

<br/>

<div align="center">

<a href="https://www.star-history.com/?repos=TG-Twilight%2FAWAvenue-Ads-Rule&type=date&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=TG-Twilight/AWAvenue-Ads-Rule&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=TG-Twilight/AWAvenue-Ads-Rule&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=TG-Twilight/AWAvenue-Ads-Rule&type=date&legend=top-left" />
  </picture>
</a>

</div>

</details>

---

<div align="center">

<img src="https://count.getloli.com/get/@TG-Twiligh?theme=booru-helltaker&darkmode=0" alt="Profile Views" width="520">

<sub>View stats since June 2024 · occasionally (okay, often) down</sub>

<br/>

[GitHub](https://github.com/TG-Twilight/AWAvenue-Ads-Rule)
·
[Channel](https://t.me/AWAvenueAdsRule)
·
[Group](https://t.me/AWAvenueAdsChat)
·
[秋风塬上](https://awads.cc/)

</div>
