import json

def format_domain(domain_file):
    domain = ["127.0.0.1 localhost", "::1 localhost", "", ""]
    with open(domain_file, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        domain_lines = f"127.0.0.1 {line.strip()}"
        domain.append(domain_lines)
    return domain


def build(domain_file, regex_file):
    return format_domain(domain_file)