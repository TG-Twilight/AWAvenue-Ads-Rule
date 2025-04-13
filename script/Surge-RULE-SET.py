def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"DOMAIN,{line.strip()}"
        domain.append(domain_lines)
    return domain

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"DOMAIN-KEYWORD,{line.strip()}"
        regex.append(regex_lines)
    return regex

def format_ip(List):
    ip = []
    for line in List:
        ip_lines = f"IP-CIDR,{line.strip()}"
        ip.append(ip_lines)
    return ip

def build(rule):
    list = format_ip(rule.ip_list) + format_domain(rule.domain_list) + format_regex(rule.regex_list)
    return {'list': list, 'suffix': '.list', 'comment': '#', 'total': len(list)}