
def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"0.0.0.0 {line.strip()}"
        domain.append(domain_lines)
        domain_lines = f":: {line.strip()}"
        domain.append(domain_lines)
    
    return domain


def build(rule):
    list = format_domain(rule.domain_list)
    return {'list': ["127.0.0.1 localhost", "::1 localhost", "", ""] + list, 'suffix': '.txt', 'comment': '!', 'total': len(list)}