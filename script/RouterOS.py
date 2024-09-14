import json

def format_domain(List):
    domain = []
    for line in List:
        domain_line = f"ip dns static add address=240.0.0.1 name={line.strip()}"
        domain.append(domain_line)
    return domain

def build(rule):
    return {'list': format_domain(rule.regex_list), 'suffix': '.txt', 'comment': '!', 'total': len(rule.regex_list)}
