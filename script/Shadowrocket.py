def format_domain(domain_list):
    domain_lines = []
    for line in domain_list:
        line = line.strip()
        if line:
            domain_lines.append(f"DOMAIN-SUFFIX,{line},Reject")
    return domain_lines

def build(rule):
    domain_rules = format_domain(rule.domain_list)
    return {
        'content': '\n'.join(domain_rules),
        'suffix': '.conf',
        'total': len(domain_rules)
    }
