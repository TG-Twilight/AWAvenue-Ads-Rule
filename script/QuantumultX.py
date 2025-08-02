
def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"DOMAIN,{line.strip()},reject"
        domain.append(domain_lines)
    return domain

def format_suffix(List):
    suffix = []
    for line in List:
        suffix_lines = f"DOMAIN-SUFFIX,{line.strip()},reject"
        suffix.append(suffix_lines)
    return suffix

def format_keyword(List):
    keyword = []
    for line in List:
        keyword_lines = f"DOMAIN-KEYWORD,{line.strip()},reject"
        keyword.append(keyword_lines)
    return keyword

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"DOMAIN-REGEX,{line.strip()},reject".replace("$","").replace("^","").replace("*","").replace("\\.",".")
        regex.append(regex_lines)
    return regex

def format_ip(List):
    ip = []
    for line in List:
        ip_lines = f"IP-CIDR,{line.strip()},reject"
        ip.append(ip_lines)
    return ip

def build(rule):
    list = format_ip(rule.ip_list) + format_domain(rule.domain_list) + format_suffix(rule.suffix_list) + format_keyword(rule.keyword_list) + format_regex(rule.regex_list)
    return {'list': list, 'suffix': '.list', 'comment': '#', 'total': len(list)}