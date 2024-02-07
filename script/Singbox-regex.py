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

def format_regex(regex_file):
    regex = []
    
    with open(regex_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        regex_lines = f"{line.strip()}"
        regex.append(regex_lines)
    return regex

def build(domain_file, regex_file):
    domain_list = format_domain(domain_file)
    domain_regex_list = format_regex(regex_file)
    domain_suffix_list = format_suffix(domain_file)
    rule = {
        "version": 1,
        "rules": [
            {
                "domain": domain_list,
                "domain_regex": domain_regex_list,
                "domain_suffix": domain_suffix_list
            }
        ]
    }
    
    json_data = json.dumps(rule, indent=2)
    return [json_data]