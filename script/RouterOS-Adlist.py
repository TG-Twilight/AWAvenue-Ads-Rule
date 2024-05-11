import json

def format_domain(List):
    domain = ["0.0.0.0 localhost", "::1 localhost", "", ""]
    for line in List:
        domain_lines = f"0.0.0.0 {line.strip()}"
        domain.append(domain_lines)
    return domain


def build(rule):
    return format_domain(rule.domain_list), ".txt"