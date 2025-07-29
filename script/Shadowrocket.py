
def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"DOMAIN-SUFFIX,{line.strip()},Reject"
        domain.append(domain_lines)
    return domain

def format_ip(List):
    ip = []
    for line in List:
        ip_lines = f"IP-CIDR,{line.strip()},Reject"
        ip.append(ip_lines)
    return ip

def build(rule):
    list = format_ip(rule.ip_list) + format_domain(rule.domain_list)
    return {'list': list, 'suffix': '.conf', 'comment': '#', 'total': len(conf)}
