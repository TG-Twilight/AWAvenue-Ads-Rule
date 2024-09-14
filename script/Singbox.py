import json

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"{line.strip()}"
        domain.append(domain_lines)
    return domain

def build(rule):
    domain_list = format_domain(rule.domain_list)
    rule = {
        "version": 1,
        "rules": [
            {
                "domain": domain_list,
                "domain_regex": [],
                "domain_suffix": []
            }
        ]
    }
    
    json_data = [json.dumps(rule, indent=2)]
    return {'list': json_data, 'suffix': '.json', 'comment': '//', 'total': len(json_data)}