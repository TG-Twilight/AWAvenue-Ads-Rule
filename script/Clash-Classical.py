# https://wiki.metacubex.one/config/rules/#_1
# https://wiki.metacubex.one/config/rule-providers/content/#classical

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"  - DOMAIN,{line.strip()}"
        domain.append(domain_lines)
    return domain

def format_suffix(List):
    suffix = []
    for line in List:
        suffix_lines = f"  - DOMAIN-SUFFIX,{line.strip()}"
        suffix.append(suffix_lines)
    return suffix

def format_keyword(List):
    keyword = []
    for line in List:
        keyword_lines = f"  - DOMAIN-KEYWORD,{line.strip()}"
        keyword.append(keyword_lines)
    return keyword

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"  - DOMAIN-REGEX,^{line.strip()}$"
        regex.append(regex_lines)
    return regex

def format_ip(List):
    ip = []
    for line in List:
        ip_lines = f"  - IP-CIDR,{line.strip()},no-resolve"
        ip.append(ip_lines)
    return ip

def format_ip6(List):
    ip6 = []
    for line in List:
        ip6_lines = f"  - IP-CIDR,{line.strip()},no-resolve"
        ip6.append(ip6_lines)
    return ip6

def build(rule):
    list = format_ip(rule.ip_list) + format_ip6(rule.ip6_list) + format_domain(rule.domain_list) + format_suffix(rule.suffix_list) + format_keyword(rule.keyword_list) + format_regex(rule.regex_list)
    return {'list': ["payload:"] + list, 'suffix': '.yaml', 'comment': '#', 'total': len(list)}
