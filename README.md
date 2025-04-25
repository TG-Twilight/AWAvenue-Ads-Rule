<div align="left">
<a href="/README.md">中文</a>&nbsp;|&nbsp;
<a href="/assets/README_en-US.md">English</a> &nbsp;|&nbsp;
<a href="/assets/README_Update.md">更新日志</a> &nbsp;|&nbsp;
<a href="https://awavenue.top/">官方网站</a> 
</div>


<h1 align="center">-AWAvenue 秋风广告规则 -</h1>

<p align="center">
   <img src="https://img.jsdelivr.com/raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/assets/assets.png">
</p>
<p align="center">
 <img src="https://img.shields.io/github/stars/TG-Twilight/AWAvenue-Ads-Rule?style=for-the-badge&colorA=FFEBEB&colorB=FFD9DC&logo=github&logoColor=black">
  <a href="https://t.me/AWAvenueAdsRule">
    <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=%E9%A2%91%E9%81%93&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueAdsRule" alt="Telegram">
  </a>
  <a href="https://t.me/AWAvenueAdsChat">
    <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=%E7%BE%A4%E8%81%8A&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueAdsChat" alt="Telegram">
  </a>
</p>


<p align="center"><b>干掉所有无良广告<br>Eliminate All Malicious Ads</b></p>

## 🍁关于此广告规则 | About

众多优秀广告规则的上游、开源社区中最棒的广告过滤器列表之一，实现了最佳的广告拦截、隐私保护和流量节省。支持各种常见的网络层广告拦截工具和代理工具等¹，与其它动辄成千上万条的广告规则相比，秋风广告规则有着极致的体积控制、超高的命中率和极低的硬件要求。

订阅本规则后，您明显可以感受到烦人的摇一摇广告不见了，订阅号列表和文中文末的广告流无法加载，自动播放的广告视频直接绝迹，电视盒子/智能电视的开机广告消失，同时手机的剩余空间也多了一些（因为阻止了广告文件的下发）

相较于其它去广告的手段，这种从网络层面过滤的方式成本低、使用方便快捷、受益范围广(例如路由器部署)，您无需对每个有需求的app进行单独设置，在无感过滤的同时不影响您正常使用原有的app。

*截止2025年6月，我们可以拦截提瓦特大陆现有九成以上的广告sdk内容。*

### *如果您对本规则的内容有意见或建议，在提交issue/进群反馈前，请您务必查看我们的[常见问题](https://awavenue.top/Knowledge.html#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98-%E4%B8%8E%E7%AD%94%E7%96%91)部分，这些内容也许可以解决您的一些疑问。*

---

## 🍁工作原理 | Work Principle

从网络层面对抗(拦截)应用中的各种流氓广告SDK与服务器交互，阻止其正常加载，从而达到去广告的目的。<br />

---

## 🍁订阅规则 | Subscription Rules

适用于AdGuard Home、AdGuard、AdGuard DNS 等支持Adblock语法广告过滤工具的规则：

- [Github Raw订阅地址](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt)
- [天命CFCDN订阅地址](https://github.boki.moe/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt)
- [jsDelivr(gcore)订阅地址](https://gcore.jsdelivr.net/gh/TG-Twilight/AWAvenue-Ads-Rule@main/AWAvenue-Ads-Rule.txt)
- [ghproxy订阅地址](https://ghfast.top/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt)

其他格式和更多加速订阅链接见[官方网站-订阅规则](https://awavenue.top/Sub.html)

---

## 🍁支持的工具 | Supported Tools

我们兼容现有的绝大多数广告拦截工具/代理工具，例如：

[AdGuard (iOS/Android)/Home/DNS](https://awavenue.top/Sub.html#adguard-ios-android-home-dns-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5) 等大部分支持adblock语法的工具，不含AdGuard for Chrome；

[AdAway、大圣净化](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5)等支持hosts格式的工具；

[Mosdns](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=%E6%8E%A5%EF%BC%88.list%E6%A0%BC%E5%BC%8F%EF%BC%89-,Mosdns%20V5%20%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5,-AdClose%20rule%E6%A0%BC%E5%BC%8F)、[Dnsmasq](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=Dnsmasq%E6%A0%BC%E5%BC%8F%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%88.conf%E6%A0%BC%E5%BC%8F%EF%BC%89)、[广告屏蔽大师Plus+、DNS去广告](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5)等专为 OpenWrt 上一系列工具适配的规则；

[ClashMeta](https://awavenue.top/Sub.html#clash-%E8%A7%84%E5%88%99%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5)、[QuantumultX(.list)](https://awavenue.top/Sub.html#clash-%E8%A7%84%E5%88%99%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=QuantumultX%20%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%88.list%E6%A0%BC%E5%BC%8F%EF%BC%89)、ShadowRocket、Surge、Surfboard、Singbox等主流代理工具，

同时，专门为 RouterOS 的路由器适配了广告规则。  *（含240.0.0.1/0.0.0.0格式）*

 *若您在订阅本广告规则后，发现应用内流氓广告sdk仍在正常展示广告/出现误杀，欢迎反馈！*

---

## 🍁如何使用 | How to use

请务必查阅我们的[官方教程](https://awavenue.top/Knowledge.html)，若您还有疑问，可以前往我们的官方群组（见下排）进行询问。

个人项目，随缘维护更新，欢迎issues和Pr。   [😀加入秋風がく山道](https://t.me/AWAvenueAdsChat)。

---

<details>
  <summary>推荐的广告过滤工具</summary>

- [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome)    *安装在路由器，广告过滤工具较为理想的工作位置*，目前，秋风广告规则已加入AdGuard官方列表，你可以直接在 “从列表中选择” 订阅！

- [AdGuard](https://adguard.com/)    *多端使用，支持Android、Windows、Mac、iOS*

- [AdAway](https://adaway.org/)    *AdAway 是一款使用 hosts 文件的 Android 开源广告拦截器。*

- [AdGuard DNS](https://adguard-dns.io/en/welcome.html)    *直接使用自定义的DNS服务器，目前，秋风广告规则已加入AdGuard官方列表，你可以直接在AdGuard DNS Filters中订阅！*

- [AdGuard Home For Magisk](https://github.com/twoone-3/AdGuardHomeForMagisk)   *AdGuard Home的Magisk版本*

- [AdClose（Xposed module）](https://github.com/zjyzip/AdClose)    *Xposed模块，可以通过hook拦截常见广告，内置秋风广告规则，感谢@zjyzip*

</details>

---

## 🍁赞助商 | Special sponsors

[倾城极速 - 畅游世界，高速互联](https://www.qcjs.ovh/#/register?code=prbbRzx9)

---

## 🍁贡献者 | Contributors

<p align="left"><a href="https://github.com/TG-Twilight/AWAvenue-Ads-Rule/graphs/contributors"><img src="https://contrib.rocks/image?repo=TG-Twilight/AWAvenue-Ads-Rule&max=50" /></a></p>

---

## Star History

[![Stargazers over time](https://starchart.cc/TG-Twilight/AWAvenue-Ads-Rule.svg?variant=adaptive)](https://starchart.cc/TG-Twilight/AWAvenue-Ads-Rule)

---

### ***保持互联网清洁！***

---

[![https://gafam.info](https://ptrace.gafam.info/unofficial/img/color/lqdn-gafam-poster-zh-color-5x1-2560x.png)](https://gafam.info)

---
![:访问数](https://moe-counter.glitch.me/get/@TG-Twiligh?theme=gelbooru)

2024年6月开始统计，统计偶尔会寄......
---

> [@Github](https://github.com/TG-Twilight/AWAvenue-Ads-Rule) · [@Telegram Channel](https://t.me/AWAvenueAdsRule) · [@Telegram Group](https://t.me/AWAvenueAdsChat) · [Official WebSite](https://awavenue.top/) · [E-Mail](mailto:admin@awads.cc)
