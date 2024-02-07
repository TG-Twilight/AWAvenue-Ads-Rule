def format_domain(domain_file):
    domain = []
    with open(domain_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        domain_lines = f"||{line.strip()}^"
        domain.append(domain_lines)
    return domain


def format_regex(regex_file):
    regex = []
    
    with open(regex_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        regex_lines = f"/{line.strip()}/".replace("\.","\\\.").replace("\*","\.\*")
        regex.append(regex_lines)
    return regex

def build(domain_file, regex_file):
    Adguard_list = format_domain(domain_file) + format_regex(regex_file)
    return Adguard_list