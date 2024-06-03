
def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"  - DOMAIN,{line.strip()}"
        domain.append(domain_lines)
    return domain

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"  - DOMAIN-REGEX,'{line.strip()}'"
        regex.append(regex_lines)
    return regex

def format_ip(List):
    ip = []
    for line in List:
        ip_lines = f"  - IP-CIDR,{line.strip()}"
        ip.append(ip_lines)
    return ip

def build(rule):
    clash_list = ["payload:"] + format_ip(rule.ip_list) + format_domain(rule.domain_list) + format_regex(rule.regex_list)
    return clash_list, ".yaml", "#"