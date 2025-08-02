def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f".{line.strip()}"
        domain.append(domain_lines)
    return domain

def build(rule):
    list = format_domain(rule.domain_list) + format_domain(rule.suffix_list)
    return {'list': list, 'suffix': '.list', 'comment': '#', 'total': len(list)}