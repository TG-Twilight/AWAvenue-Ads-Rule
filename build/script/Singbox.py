import json

def format_domain(domain_file):
    domain = []
    with open(domain_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        domain_lines = f"{line.strip()}"
        domain.append(domain_lines)
    return domain

def format_suffix(domain_file):
    suffix = []
    
    with open(domain_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        suffix_lines = f".{line.strip()}"
        suffix.append(suffix_lines)
    return suffix

def build(domain_file, regex_file):
    domain_list = format_domain(domain_file)
    domain_suffix_list = format_suffix(domain_file)
    rule = {
        "version": 1,
        "rules": [
            {
                "domain": domain_list,
                "domain_regex": [],
                "domain_suffix": domain_suffix_list
            }
        ]
    }
    
    json_data = json.dumps(rule, indent=2)
    return [json_data]