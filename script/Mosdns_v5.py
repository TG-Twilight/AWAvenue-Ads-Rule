import json

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"domain:{line.strip()}"
        domain.append(domain_lines)
    return domain


def build(rule):
    return format_domain(rule.domain_list), ".txt", "#", len(rule.domain_list)
