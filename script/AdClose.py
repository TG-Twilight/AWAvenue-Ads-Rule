import json

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"domain, {line.strip()}"
        domain.append(domain_lines)
    return domain

def format_keyword(List):
    keyword = []
    for line in List:
        keyword_lines = f"keyword, {line.strip()}"
        keyword.append(keyword_lines)
    return keyword


def build(rule):
    # AdClose 的 Domain 类型即匹配该域名的全部相关请求, 故 suffix 规则复用同一前缀
    list = format_domain(sorted(set(rule.domain_list) | set(rule.suffix_list))) + format_keyword(rule.keyword_list)
    return {'list': ["#This rule is only used with AdClose", "", ""] + list, 'suffix': '.rule', 'comment': '#', 'total': len(list)}
