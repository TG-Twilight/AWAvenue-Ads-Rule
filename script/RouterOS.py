import json

def format_domain(List, Listv6):
    domain = []
    for line in List:
        domain_line = f"ip dns static add address=240.0.0.1 name={line.strip()}"
        domain.append(domain_line)
    
    for line in Listv6:
        domain_line = f"ip dns static add address=:: name={line.strip()}"
        domain.append(domain_line)
    return domain

def build(rule):
    return {'list': format_domain(rule.domain_list, rule.domainv6_list), 'suffix': '.txt', 'comment': '!', 'total': len(rule.regex_list)}
