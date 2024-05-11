## 插件开发文档

插件入口函数为`build(rule)`

插件返回的list格式参考:

`Adguard.py`:

```python
["||xxx.com^","||xxx.cc^"], ".txt"
```
> **有两个返回值**

API:
- rule.domain_list(获取域名列表)
- rule.regex_list(获取正则表达式的域名列表)
- rule.ip_list(获取ip列表)

> 所有变量均为列表 无需读取文件

模板:
```
# 主函数并且引入rule(对象)
def build(rule):
    list = rule.domain_list + rule.regex_list + rule.ip_list
    return list, ".yaml" # 返回处理后的列表和文件后缀名
```
> 输出文件名=插件名