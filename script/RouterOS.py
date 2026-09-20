import json

def format_domain(List):
    domain = []
    for line in List:
        domain_line = f"ip dns static add address=240.0.0.1 name={line.strip()}"
        domain.append(domain_line)
        domain_line = f"ip dns static add address=:: name={line.strip()}"
        domain.append(domain_line)
    return domain

def build(rule):
    # 静态 DNS 条目为精确匹配, suffix 规则只能补出主域名本身; 通配需 regexp= 写法, 因其 CPU 开销大暂不采用
    list = format_domain(sorted(set(rule.domain_list) | set(rule.suffix_list)))
    return {'list': list, 'suffix': '.txt', 'comment': '!', 'total': len(list)}
