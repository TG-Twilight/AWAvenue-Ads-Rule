## 如何贡献规则?

fork本分支，修改本目录的文件（前提是你有一定量的适合本规则的广告域名，我们并不乐意处理仅提交一个域名的Pr）。

否则我们**强烈建议**你在 issue 直接提出：xxxxxxx是xxxxx的广告域名/是被错误拦截的，建议拦截/放行，并且附上必要的图片之类。


## build

此分支将构建[rule](./rule)中的基础规则

转换插件文档见[script](./script)

添加规则文档见[rule](./rule)

# 使用方法
```shell
python main.py
```

## 须知

> 一行一个 不会匹配子域名


`domain.txt` 文件为域名列表

`domain_regex.txt` 匹配域名正则表达式(并不是所有插件都会调用此规则)

`domain_suffix.txt` 匹配域名后缀(并不是所有插件都会调用此规则)

`domain_keyword.txt` 匹配域名的关键字(并不是所有插件都会调用此规则)

`ip.txt` 文件为ipv4列表(并不是所有插件都会调用此规则)

`ip6.txt` 文件为ipv6列表(并不是所有插件都会调用此规则)
