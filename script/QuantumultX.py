
def format_domain(domain_file):
    domain = []
    with open(domain_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        domain_lines = f"DOMAIN,{line.strip()},reject"
        domain.append(domain_lines)
    return domain

def format_regex(regex_file):
    regex = []
    
    with open(regex_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        regex_lines = f"DOMAIN-KEYWORD,{line.strip()},reject".replace("$","").replace("^","").replace("*","")
        regex.append(regex_lines)
    return regex

def build(domain_file, regex_file):
    return format_domain(domain_file) + format_regex(regex_file)