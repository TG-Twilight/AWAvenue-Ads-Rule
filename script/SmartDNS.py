# https://pymumu.github.io/smartdns/config/domain-rule/

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"address /-.{line.strip()}/#"
        domain.append(domain_lines)
    return domain

def format_suffix(List):
    suffix = []
    for line in List:
        suffix_lines = f"address /{line.strip()}/#"
        suffix.append(suffix_lines)
    return suffix

def build(rule):
    list = format_domain(rule.domain_list) + format_suffix(rule.suffix_list)
    return {'list': list, 'suffix': '.conf', 'comment': '#', 'total': len(list)}
