## 插件开发文档

插件入口函数为`build()`

参考[Clash.py](./Clash.py)

插件返回的list格式参考下面的模板

`Adguard.py`:

```python
["||xxx.com^","||xxx.cc^"]
```
> 后缀名以及注释符请在build.json中添加 如果不存在则不执行此插件

提供的变量:


## domain_file
> 获取 rule目录的 domain.txt 路径

## regex_file
>获取 rule目录的 domain_regex.txt 路径