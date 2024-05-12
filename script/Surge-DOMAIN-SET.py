def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f".{line.strip()}"
        domain.append(domain_lines)
    return domain

def build(rule):
    surge_list = format_domain(rule.domain_list)
    return surge_list, ".list", "#"