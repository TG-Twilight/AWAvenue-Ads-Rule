
def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"address=/{line.strip()}/0.0.0.0"
        domain.append(domain_lines)
    return domain


def build(rule):
    return {'list': format_domain(rule.domain_list), 'suffix': '.conf', 'comment': '#', 'total': len(rule.domain_list)}