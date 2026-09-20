import json

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"0.0.0.0 {line.strip()}"
        domain.append(domain_lines)
        domain_lines = f":: {line.strip()}"
        domain.append(domain_lines)
    return domain


def build(rule):
    # adlist 为 hosts 格式, 无法表达通配, suffix 规则只能补出主域名本身(子域仍无法覆盖)
    list = format_domain(sorted(set(rule.domain_list) | set(rule.suffix_list)))
    return {'list': ["0.0.0.0 localhost", "::1 localhost", "", ""] + list, 'suffix': '.txt', 'comment': '#', 'total': len(list)}