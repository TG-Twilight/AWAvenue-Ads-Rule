## 插件开发文档

插件入口函数为`build(rule)`

插件返回的list格式参考:

`Adguard.py`:

```python
["||xxx.com^","||xxx.cc^"], ".txt", "!", xxx
```

> 处理后的域名列表(list), 文件后缀名(string), 注释符号(string), 规则数量(int|string)

API:
- rule.domain_list(获取域名列表)
- rule.domain_v6_list(获取支持ipv6域名列表)
- rule.regex_list(获取正则表达式的域名列表)
- rule.ip_list(获取ip列表)
- rule.ip6_list(获取ipv6列表)

> 所有变量均为列表 也可以导入config.py获取
输出文件名=插件名