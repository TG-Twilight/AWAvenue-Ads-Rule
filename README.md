<div align="left">
<a href="/README.md">中文</a>&nbsp;|&nbsp;
<a href="/README_en-US.md">English</a> 
</div>



<h1 align="center">-AWAvenue 秋风广告规则 -</h1>

<p align="center">
   <img src="https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Adblock-Rule/main/AWAvenue%20%E7%A7%8B%E9%A3%8E%E5%B9%BF%E5%91%8A%E8%A7%84%E5%88%99%EF%BC%88AWAvenue-Adblock-Rule%EF%BC%89.png">
</p>
<p align="center">
 <img src="https://img.shields.io/github/stars/TG-Twilight/AWAvenue-Adblock-Rule?style=for-the-badge&colorA=FFEBEB&colorB=FFD9DC&logo=github&logoColor=black">
  <a href="https://t.me/AWAvenue">
    <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=%E9%A2%91%E9%81%93&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenue" alt="Telegram">
  </a>
  <a href="https://t.me/AWAvenueCheat">
    <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&colorA=DAE9FC&colorB=056DE8&label=%E7%BE%A4%E8%81%8A&logo=telegram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3DAWAvenueCheat" alt="Telegram">
  </a>
</p>


<p align="center"><b>干掉所有无良广告<br>Eliminate All Malicious Ads</b></p>

使用Adblock语法，从网络层面对抗Android应用中的各种广告SDK，阻止其加载。

Use Adblock syntax to fight against various advertising SDKs in Android apps from the network level.

## 订阅规则 | Subscription Rules

- [Github订阅地址](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Adblock-Rule/main/AWAvenue-Adblock-Rule.txt)
- [ghproxy反代订阅地址-1](https://ghproxy.net/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Adblock-Rule/main/AWAvenue-Adblock-Rule.txt)
- [ghproxy反代订阅地址-2](https://ghproxy.com/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Adblock-Rule/main/AWAvenue-Adblock-Rule.txt)

激进版（AWAvenue-Adblock-Rule-Strict）
- [Github订阅地址](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Adblock-Rule/main/AWAvenue-Adblock-Rule-Strict.txt)
- [ghproxy反代订阅地址-1](https://ghproxy.net/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Adblock-Rule/main/AWAvenue-Adblock-Rule-Strict.txt)
- [ghproxy反代订阅地址-2](https://ghproxy.com/https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Adblock-Rule/main/AWAvenue-Adblock-Rule-Strict.txt)


项目维护者 [Zutzo](https://github.com/zutzo)、[Flower(RikkaTi)](https://t.me/Reese_Rikkati)

同时，感谢 [杰哥](https://t.me/JessTeesdale) 、[Aries](https://t.me/NoAries) 提供的反代订阅


## 关于此广告规则 | About
**十分厌恶**某些广告sdk的**侵入式**展示，这非常影响使我的用体验。及考虑到长辈们也在使用Android设备，在他们面对无良广告时，大多毫无还手之力。他们的与子女沟通联系的设备被灌满垃圾；他们自由掌控设备的权利被肆意践踏……最后不得不换回老年机……
**为了保护他们自由、舒适、流畅的使用Android设备权利不受无良广告商之践踏，及让我自己使用时尽可能不被无良广告恶心**，故制作此规则，以期与无良广告sdk能有一搏之力。

#### 特别强调 此项目目前为个人维护项目，随缘更新，可以issues(个人更推荐你[进群](https://t.me/AWAvenueCheat)，更多时候我在那里，Pr前请到群里打个招呼)，但请别对我指手画脚，谢谢。
#### 如果您有想屏蔽的广告sdk而本规则无法屏蔽的，也欢迎加入群聊反馈！期待着您的加入!


## 如何使用 | How to use
如同众多广告规则的导入流程一样，此广告规则使用[Adblock语法](https://github.com/AdguardTeam/AdGuardHome/wiki/Hosts-Blocklists)编写，故在理论上，但凡是支持Adblock语法\从网络层面工作的广告拦截工具均可将其导入并使用。（你也可以复制规则然后再粘贴进广告拦截工具的自定义拦截规则区域内，但那比你直接导入会麻烦许多）

### 关于配合各种Clash进行过滤工作的额外设置
以 Shell Clash 为例，
Clash功能设置 —— DNS运行模式 —— Redir host

Clash进阶设置 —— 配置内置DNS服务 —— 修改基础DNS 改为本地最优的DNS地址（可设置多个，英文逗号分隔，不知道填什么？推荐：1.1.1.1、8.8.8.8、223.5.5.5）

Clash进阶设置 —— 配置内置DNS服务 —— Dnsmasq转发 更改为开启状态

AdGuard Home —— 设置 —— DNS设置 —— 上游DNS服务器 填写：127.0.0.1:1053(Shell Clash默认的DNS端口)


### 更新日志：

0.2.0-beta：针对 穿x甲巨量、Txxxxxt Advertising Open Platform、快x广告开放平台、京x入侵式购物广告、Kiwi广告、Ali Ads等广告sdk的流氓部分 进行了有效的屏蔽。同时，支持拦截微信订阅号文章列表及文章内容页中 插入式/文末的视频/图片广告（拦截图片广告的图片加载和自动视频广告的视频自动下载、播放）

0.3.0-beta：新增 Apple Ads、UMENG、Google Analysis、Google Ads、DoubleClick、XiaoMi Ads 拦截

0.4.1-beta：新增 部分baidu adsdk、QQ Music的广告屏蔽

0.4.2-beta：新增拦截 Fluurry统计、酷狗统计与广告、小米跟踪、百度跟踪、QQ Bugly，补充拦截 Umeng

0.5.0-beta：新增拦截 云猿广告sdk ，屏蔽部分微信小程序广告

0.5.5-beta：新增拦截(测试，不生效属正常) 酷安 提到的好物、什么值得买、去除热搜、随机应用推荐、评论区下某广告，更新穿山甲sdk拦截等

0.6.0-beta：新增一些叫不上名的拦截~~0.6.0更新时忘了写，更新0.7.0也想不起来了~~

0.7.5-beta：新增 ADSCOPE广告sdk、ADHUB广告sdk、猫眼广告sdk、360 ads sdk ，更新部分 vivo 与 并夕夕、JD购物广告、zijie Aads sdk 等拦截，经过测试，作业精灵 可无广告正常使用

0.8.0-beta：新增 谷歌广告（CN）、OPPO应用商店开屏广告、优量汇、小红书等

0.8.9-beta：新增拦截 ADSCOPE 的“beizi”广告，新增拦截 章鱼广告 ，新增拦截 一些 heytap(obbo)广告域名，修复了对于百度图片链接的误杀，同时为规则添加了“title”

0.9.2-beta：新增拦截 米游社日志 酷狗音乐统计 Adjust GamePass，加强拦截 字节跳动

0.9.5-beta：新增拦截 银联广告 推必安

## 推荐的广告过滤工具 | Recommended Tools
- [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome)    *路由器安装，这是广告过滤工具较为理想的工作位置*

- [AdGuard Home For Magisk](https://t.me/AWAvenue/357)   *AdGuard Home的Magisk版本，由[酷安@top大佬制作](https://www.coolapk.com/u/1373784)*

- [Adblock Plus](https://adblockplus.org/)    *强大的、适用于浏览器的广告过滤插件*

- [uBlock Origin](https://ublockorigin.com/)    *另一款开源而强大的浏览器广告过滤插件*

- [AdGuard](https://adguard.com/)    *多端使用，支持Android、Windows、Mac、iOS*


---

> [@Github](https://github.com/TG-Twilight/AWAvenue-Adblock-Rule) · [@Telegram Channel](https://t.me/AWAvenue) · [@Telegram Group](https://t.me/AWAvenueCheat) 
