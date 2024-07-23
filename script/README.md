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
- rule.regex_list(获取正则表达式的域名列表)
- rule.ip_list(获取ip列表)
- rule.ip6_list(获取ipv6列表)

> 所有变量均为列表 无需读取文件

模板:
```python

def format_domain(List): # 转换域名规则
    domain = []
    for line in List:
        domain_lines = f"  - DOMAIN,{line.strip()}"
        domain.append(domain_lines)
    return domain

def format_regex(List): # 转换正则表达式规则
    regex = []
    for line in List:
        regex_lines = f"  - DOMAIN-REGEX,'{line.strip()}'"
        regex.append(regex_lines)
    return regex

def format_ip(List): # 转换ip列表
    ip = []
    for line in List:
        ip_lines = f"  - IP-CIDR,{line.strip()}"
        ip.append(ip_lines)
    return ip

def build(rule): # 入口函数
    clash_list = ["payload:"] + format_ip(rule.ip_list) + format_domain(rule.domain_list) + format_regex(rule.regex_list) 合并规则
    return clash_list, ".yaml", "#", len(clash_list)
    #

```
> 输出文件名=插件名