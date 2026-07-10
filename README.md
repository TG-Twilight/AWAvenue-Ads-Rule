<div align="center">

**中文** · [English](/assets/README_en-US.md) · [更新日志](/assets/README_Update.md) · [官网 · CF](https://awavenue.top) · [官网 · EO](https://doc.awads.cc)

<br/>

# AWAvenue 秋风广告规则

<img src="https://img.jsdelivr.com/raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/assets/assets.png" alt="AWAvenue" width="720">

<p><b>干掉所有无良广告<br>Eliminate All Malicious Ads</b></p>

<br/>

<img src="https://img.shields.io/github/stars/TG-Twilight/AWAvenue-Ads-Rule?style=for-the-badge&colorA=FFEBEB&colorB=FFD9DC&logo=github&logoColor=pink" alt="Stars">
<a href="https://t.me/AWAvenueAdsRule"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=%E9%A2%91%E9%81%93&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueAdsRule" alt="Telegram Channel"></a>
<a href="https://t.me/AWAvenueAdsChat"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=%E7%BE%A4%E8%81%8A&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueAdsChat" alt="Telegram Group"></a>
<a href="https://afdian.com/a/AdsRule" target="_blank"><img src="https://img.shields.io/badge/%E8%B5%9E%E5%8A%A9%E6%88%91-ffd700?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white&labelColor=ff9800" alt="赞助我"></a>

<br/>

<p>
  <a href="https://www.star-history.com/tg-twilight/awavenue-ads-rule">
    <img src="https://api.star-history.com/badge?repo=TG-Twilight/AWAvenue-Ads-Rule&theme=dark" alt="Star History Rank">
  </a>
</p>

</div>

---

## 关于

众多优秀广告规则的上游、开源社区中最棒的广告过滤器列表之一——在广告拦截、隐私保护与流量节省之间做到很好的平衡。

与其它动辄成千上万条的规则相比，秋风广告规则有着：

| 特点 | 说明 |
|:----:|------|
| 体积可控 | 极致体积控制，加载更快 |
| 命中率高 | 针对常见广告 SDK 与场景优化 |
| 硬件友好 | 路由器 / 低配设备也能轻松跑 |
| 部署简单 | 一次订阅，多端受益 |

订阅后你通常会明显感觉到：

- 烦人的「摇一摇」广告消失
- 订阅号列表、文中 / 文末广告流无法加载
- 自动播放的广告视频绝迹
- 电视盒子 / 智能电视开机广告消失
- 手机剩余空间多了一点（拦截广告资源下发）

相较于逐个 App 配置去广告，网络层过滤成本更低、覆盖更广（例如路由器部署），在无感过滤的同时尽量不影响正常使用。

> 截止 2025 年 7 月，可拦截提瓦特大陆现有九成以上的广告 SDK 内容。

> [!IMPORTANT]
> 提交 Issue / 进群反馈前，请先阅读 [常见问题](https://awavenue.top/Knowledge.html#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98-%E4%B8%8E%E7%AD%94%E7%96%91)，很多疑问已有说明。

---

## 工作原理

从**网络层**拦截应用中各类广告 SDK 与服务器的通信，阻止广告正常加载。

这与李x跳等无障碍点击类工具原理完全不同——**不支持**此类工具导入。

若订阅后仍见广告展示，或出现误杀，欢迎反馈。

---

## 订阅规则

适用于 **AdGuard Home / AdGuard / AdGuard DNS** 等支持 Adblock 语法的工具：

| 线路 | 链接 |
|:----:|------|
| GitHub Raw | [订阅地址](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt) |
| 天命 CFCDN | [订阅地址](https://github.boki.moe/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt) |
| jsDelivr (gcore) | [订阅地址](https://gcore.jsdelivr.net/gh/TG-Twilight/AWAvenue-Ads-Rule@main/AWAvenue-Ads-Rule.txt) |
| ghproxy | [订阅地址](https://ghfast.top/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt) |

其他格式与更多加速线路见 → [官方网站 · 订阅规则](https://awavenue.top/Sub.html)

---

## 支持的工具

兼容绝大多数广告拦截 / 代理工具，例如：

| 类型 | 工具 |
|------|------|
| Adblock 语法 | [AdGuard (iOS/Android) / Home / DNS](https://awavenue.top/Sub.html#adguard-ios-android-home-dns-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5) 等（不含 AdGuard for Chrome） |
| Hosts | [AdAway、大圣净化](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5) 等 |
| OpenWrt 等 | [Mosdns](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=%E6%8E%A5%EF%BC%88.list%E6%A0%BC%E5%BC%8F%EF%BC%89-,Mosdns%20V5%20%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5,-AdClose%20rule%E6%A0%BC%E5%BC%8F)、[Dnsmasq](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=Dnsmasq%E6%A0%BC%E5%BC%8F%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%88.conf%E6%A0%BC%E5%BC%8F%EF%BC%89)、[广告屏蔽大师 Plus+、DNS 去广告](https://awavenue.top/Sub.html#hosts-%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5) |
| 代理客户端 | [Clash Meta](https://awavenue.top/Sub.html#clash-%E8%A7%84%E5%88%99%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5)、[Quantumult X](https://awavenue.top/Sub.html#clash-%E8%A7%84%E5%88%99%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5:~:text=QuantumultX%20%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%88.list%E6%A0%BC%E5%BC%8F%EF%BC%89)、Shadowrocket、Surge、Surfboard 等 |
| 路由系统 | RouterOS（含 `240.0.0.1` / `0.0.0.0` 格式） |

<details>
<summary><b>推荐的广告过滤工具</b></summary>

<br/>

- [**AdGuard Home**](https://github.com/AdguardTeam/AdGuardHome) — 装在路由器，较理想的过滤位置；秋风规则已进 AdGuard 官方列表，可在「从列表中选择」直接订阅  
- [**AdGuard**](https://adguard.com/) — Android / Windows / Mac / iOS  
- [**AdAway**](https://adaway.org/) — 基于 hosts 的 Android 开源拦截器  
- [**AdGuard DNS**](https://adguard-dns.io/en/welcome.html) — 自定义 DNS；规则已在 AdGuard DNS Filters 中  
- [**AdGuard Home For Magisk**](https://github.com/twoone-3/AdGuardHomeForMagisk) — Magisk 版 AGH  
- [**AdClose**](https://github.com/zjyzip/AdClose) — Xposed 模块，hook 常见广告，内置秋风规则（感谢 @zjyzip）  
- [**geosite (@elysias123)**](https://github.com/elysias123/geosite) — 适用于 V2Ray / Xray / mihomo / hysteria / Trojan-Go / leaf 等，含秋风分类  

</details>

---

## 如何使用

请先阅读官方教程 → [**使用指南**](https://awavenue.top/Knowledge.html)

个人项目，随缘维护；欢迎 Issue 与 PR。有问题可到 [秋風がく山道](https://t.me/AWAvenueAdsChat) 礼貌询问。

---

## 赞助商

### [XTCloud — 畅游世界，高速互联](https://xtyun.co/#/register?code=M1w4rjdl)

<div align="center">

<table align="center" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td>
      <a href="https://www.cloudflare.com/" target="_blank" title="Cloudflare提供快速、安全且可靠的全球网络与安全服务。">
        <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/CLOUDFLARE/card-cloudflare.svg" alt="Cloudflare" width="360" height="110" title="Cloudflare提供快速、安全且可靠的全球网络与安全服务。">
      </a>
    </td>
    <td>
      <a href="https://1password.com/" target="_blank" title="1Password提供安全、易用且支持多端同步的密码管理服务。">
        <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/1Password/card-1password.svg" alt="1Password" width="360" height="110" title="1Password提供安全、易用且支持多端同步的密码管理服务。">
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://zmto.com/" target="_blank" title="ZMTO提供安全、可靠且可扩展的云基础设施与 VPS 托管服务。">
        <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/zmto/card-zmto.svg" alt="ZMTO" width="360" height="110" title="ZMTO提供安全、可靠且可扩展的云基础设施与 VPS 托管服务。">
      </a>
    </td>
    <td>
      <a href="https://termius.com/" target="_blank" title="Termius提供安全、可靠且支持协作的 SSH 客户端。">
        <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/assets/logo/Termius/card-termius.svg" alt="Termius" width="360" height="110" title="Termius提供安全、可靠且支持协作的 SSH 客户端。">
      </a>
    </td>
  </tr>
</table>

</div>

---

<details>
<summary><b>Star History</b>（随缘看，经常寄）</summary>

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

<sub>访问统计自 2024 年 6 月起记录 · 偶尔(其实是经常)会寄</sub>

<br/>

[GitHub](https://github.com/TG-Twilight/AWAvenue-Ads-Rule)
·
[频道](https://t.me/AWAvenueAdsRule)
·
[群组](https://t.me/AWAvenueAdsChat)
·
[秋风塬上](https://awads.cc/)

</div>
