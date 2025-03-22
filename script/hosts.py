
def format_domain(List, Listv6):
    domain = ["127.0.0.1 localhost", "::1 localhost", "", ""]
    for line in List:
        domain_lines = f"0.0.0.0 {line.strip()}"
        domain.append(domain_lines)
    
    for line in Listv6:
        domain_lines = f":: {line.strip()}"
        domain.append(domain_lines)
    return domain


def build(rule):
    return {'list': format_domain(rule.domain_list, rule.domainv6_list), 'suffix': '.txt', 'comment': '!', 'total': len(rule.domain_list)}