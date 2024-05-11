import json

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"{line.strip()}"
        domain.append(domain_lines)
    return domain


def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"{line.strip()}"
        regex.append(regex_lines)
    return regex

def build(rule):
    domain_list = format_domain(rule.domain_list)
    regex_list = format_regex(rule.regex_list)
    List = {
        "version": 1,
        "rules": [
            {
                "domain": domain_list,
                "domain_regex": regex_list,
                "domain_suffix": []
            }
        ]
    }
    
    json_data = json.dumps(List, indent=2)
    return [json_data], ".json"