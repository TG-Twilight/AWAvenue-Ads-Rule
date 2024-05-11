
def format_domain(List):
    domain = ["127.0.0.1 localhost", "::1 localhost", "", ""]
    for line in List:
        domain_lines = f"127.0.0.1 {line.strip()}"
        domain.append(domain_lines)
    return domain


def build(rule):
    return format_domain(rule.domain_list), ".txt"