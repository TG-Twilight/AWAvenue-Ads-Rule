import json

# https://sing-box.sagernet.org/zh/configuration/rule-set/headless-rule/#_1
def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"{line.strip()}"
        domain.append(domain_lines)
    return domain

def format_keyword(List):
    keyword = []
    for line in List:
        keyword_lines = f"{line.strip()}"
        keyword.append(keyword_lines)
    return keyword

def format_suffix(List):
    suffix = []
    for line in List:
        suffix_lines = f"{line.strip()}"
        suffix.append(suffix_lines)
    return suffix

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"{line.strip()}"
        regex.append(regex_lines)
    return regex

def format_ip(List):
    ip = []
    for line in List:
        ip_lines = f"{line.strip()}"
        ip.append(ip_lines)
    return ip

def build(rule):
    domain_list = format_domain(rule.domain_list)
    keyword_list = format_keyword(rule.keyword_list)
    suffix_list = format_suffix(rule.suffix_list)
    ip_list = format_ip(rule.ip_list + rule.ip6_list)
    regex_list = format_regex(rule.regex_list)

    rule = {
        "version": 3,
        "rules": [
            {
                "ip_cidr": ip_list,
                "domain": domain_list,
                "domain_keyword": keyword_list,
                "domain_suffix": suffix_list,
                "domain_regex": regex_list
            }
        ]
    }
    
    json_data = [json.dumps(rule, indent=2)]
    total = len(ip_list) + len(domain_list) + len(keyword_list) + len(suffix_list) + len(regex_list)
    return {'list': json_data, 'suffix': '.json', 'comment': '', 'total': total}