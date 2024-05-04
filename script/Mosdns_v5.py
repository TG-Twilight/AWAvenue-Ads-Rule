import json

def format_domain(domain_file):
    domain = [""]
    with open(domain_file, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        domain_lines = f"domain:{line.strip()}"
        domain.append(domain_lines)
    return domain


def build(domain_file, regex_file):
    return format_domain(domain_file)
