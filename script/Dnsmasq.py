
def format_domain(List, Listv6):
    domain = []
    for line in List:
        domain_lines = f"address=/{line.strip()}/0.0.0.0"
        domain.append(domain_lines)
    
    for line in Listv6:
        domain_lines = f"address=/{line.strip()}/::"
        domain.append(domain_lines)
    return domain


def build(rule):
    list = format_domain(rule.domain_list, rule.domainv6_list)
    return {'list': list, 'suffix': '.conf', 'comment': '#', 'total': len(list)}