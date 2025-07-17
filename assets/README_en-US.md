<div align="left">
<a href="/README.md">中文</a>&nbsp;|&nbsp;
<a href="/assets/README_en-US.md">English</a> &nbsp;|&nbsp;
<a href="/assets/README_Update.md">Changelog</a> &nbsp;|&nbsp;
<a href="https://doc.awads.cc/?source=GitHub">Official Website [CHINA]</a> &nbsp;|&nbsp;
<a href="https://awavenue.top/?source=GitHub">Official Website [GLOBAL]</a> 
</div>

<h1 align="center">-AWAvenue Ads Rule-</h1>

<p align="center">
   <img src="https://img.jsdelivr.com/raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/assets/assets.png">
</p>
<p align="center">
 <img src="https://img.shields.io/github/stars/TG-Twilight/AWAvenue-Ads-Rule?style=for-the-badge&colorA=FFEBEB&colorB=FFD9DC&logo=github&logoColor=black">
  <a href="https://t.me/AWAvenueAdsRule">
    <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=CHANNEL&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueAdsRule" alt="Telegram">
  </a>
<a href="https://t.me/AWAvenueAdsChat">
  <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=GROUP&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueAdsChat" alt="Telegram">
</a>
</p>

<p align="center"><b>Eliminate All Malicious Ads</b></p>

## 🍁About

Serving as an upstream source for many excellent ad blocking lists, AWAvenue Ads Rule is one of the best open-source ad filter lists in the community. It delivers optimal ad blocking, privacy protection, and bandwidth savings. Compatible with various common network-layer ad blocking tools and proxy tools¹, AWAvenue Ads Rule stands out from lists with thousands of entries by maintaining a minimal size, high hit rate, and extremely low hardware requirements.

After subscribing to this rule, you’ll clearly notice annoying shake ads have disappeared, subscription lists and in-article ad streams fail to load, autoplay video ads vanish, boot ads on TV boxes and smart TVs are gone, and your phone gains extra free space (since ad files are blocked from being downloaded).

Compared to other ad-blocking methods, this network-layer filtering approach is low-cost, convenient, and broadly effective (such as deployment on routers). You don't need to configure each app individually; ads are filtered seamlessly without affecting your normal use of the original apps.

*As of July 2025, we can block over 90% of ad SDK content on Teyvat.*

### *If you have feedback or suggestions about the content of this rule, please be sure to check our [FAQ](https://awavenue.top/Knowledge.html#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98-%E4%B8%8E%E7%AD%94%E7%96%91) before submitting an issue or joining the group chat. These resources may help resolve your questions.*

---

## 🍁Work Principle

Blocks (intercepts) communication between rogue ad SDKs and their servers at the network layer, preventing them from loading ads and thereby achieving ad removal.

---

## 🍁Subscription Rules

Rules compatible with AdGuard Home, AdGuard, AdGuard DNS, and other ad blocking tools supporting Adblock syntax:

- [Github Raw Subscription URL](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt)
- [Tianming CFCDN Subscription URL](https://github.boki.moe/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt)
- [jsDelivr (gcore) Subscription URL](https://gcore.jsdelivr.net/gh/TG-Twilight/AWAvenue-Ads-Rule@main/AWAvenue-Ads-Rule.txt)
- [ghproxy Subscription URL](https://ghfast.top/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt)

Other formats and more accelerated subscription links are available at [Official Website - Subscription Rules](https://awavenue.top/Sub.html)

---

## 🍁Supported Tools

We are compatible with nearly all existing ad blockers and proxy tools, such as:

[AdGuard (iOS/Android)/Home/DNS](https://awavenue.top/Sub.html#adguard-ios-android-home-dns-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5): Most tools supporting Adblock syntax, excluding AdGuard for Chrome;

[AdAway, Dasheng Purification](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5): Tools supporting hosts format;

[Mosdns](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=%E6%8E%A5%EF%BC%88.list%E6%A0%BC%E5%BC%8F%EF%BC%89-,Mosdns%20V5%20%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5,-AdClose%20rule%E6%A0%BC%E5%BC%8F), [Dnsmasq](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=Dnsmasq%E6%A0%BC%E5%BC%8F%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%88.conf%E6%A0%BC%E5%BC%8F%EF%BC%89), [Ad Blocker Master Plus+, DNS Adblock](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5): Rules adapted for various OpenWrt tools;

[ClashMeta](https://awavenue.top/Sub.html#clash-%E8%A7%84%E5%88%99%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5), [QuantumultX (.list)](https://awavenue.top/Sub.html#clash-%E8%A7%84%E5%88%99%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=QuantumultX%20%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%88.list%E6%A0%BC%E5%BC%8F%EF%BC%89), ShadowRocket, Surge, Surfboard, Singbox: Mainstream proxy tools,

Additionally, specially adapted ad rules for RouterOS routers (including both 240.0.0.1/0.0.0.0 formats).

*If you notice that rogue ad SDKs in your apps are still showing ads or encounter false positives after subscribing to this rule, feedback is welcome!*

---

## 🍁How to Use

Please be sure to consult our [official tutorial](https://awavenue.top/Knowledge.html). If you have further questions, feel free to join our official group chat (see below) to ask.

This is a personal project, updated as time permits. Issues and PRs are welcome.   [😀Join 秋風がく山道](https://t.me/AWAvenueAdsChat).

---

<details>
  <summary>Recommended Ad Blocking Tools</summary>

- [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome)    *Install on router, the ideal location for ad filtering tools.* Currently, AWAvenue Ads Rule is included in the official AdGuard list. You can subscribe directly via "Choose from list"!

- [AdGuard](https://adguard.com/)    *Cross-platform support for Android, Windows, Mac, iOS*

- [AdAway](https://adaway.org/)    *AdAway is an open-source Android ad blocker using hosts files.*

- [AdGuard DNS](https://adguard-dns.io/en/welcome.html)    *Use custom DNS servers directly. AWAvenue Ads Rule is now part of the official AdGuard DNS Filters list!*

- [AdGuard Home For Magisk](https://github.com/twoone-3/AdGuardHomeForMagisk)   *Magisk version of AdGuard Home*

- [AdClose (Xposed module)](https://github.com/zjyzip/AdClose)    *An Xposed module that can hook and block common ads, with AWAvenue Ads Rule built-in. Thanks to @zjyzip*

- [geosite (@elysias123 branch)](https://github.com/elysias123/geosite) *Routing rule resources for V2Ray, Xray-core, mihomo, hysteria, Trojan-Go, leaf, now includes AWAvenue Ads Rule category*

</details>

---

## 🍁Special Sponsors

### [XTCloud - Travel the world, high-speed connectivity](https://cloud.xtyun.top/register?code=M1w4rjdl)

<p align="center">
  <a href="https://www.cloudflare.com/" target="_blank">
    <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/CLOUDFLARE/CF_logo_stacked_whitetype.svg" alt="Cloudflare" height="50">
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://edgeone.ai/zh?from=github" target="_blank">
    <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/Tencent/tencentcloud-color.svg" alt="Tencent Cloud" height="50">
  </a>
  <a href="https://zmto.com/" target="_blank">
    <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/zmto/zmto_logo_white.svg" alt="Tencent Cloud" height="50">
  </a>
</p>

---

## Star History

[![Stargazers over time](https://starchart.cc/TG-Twilight/AWAvenue-Ads-Rule.svg?variant=adaptive)](https://starchart.cc/TG-Twilight/AWAvenue-Ads-Rule)

---
<p align="left">
  <img src="https://count.getloli.com/get/@TG-Twiligh?theme=booru-helltaker" alt="Profile Views" width="666"/>
</p>

Statistics since June 2024; statistics are not always available...
---

> [@Github](https://github.com/TG-Twilight/AWAvenue-Ads-Rule) · [Channel](https://t.me/AWAvenueAdsRule) · [Group](https://t.me/AWAvenueAdsChat) · [Twilight's page](https://zyc.su/) · [秋风塬上](https://awads.cc/)
