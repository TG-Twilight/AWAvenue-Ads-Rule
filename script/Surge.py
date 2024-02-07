def format_domain(domain_file):
    domain = []
    with open(domain_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        domain_lines = f".{line.strip()}"
        domain.append(domain_lines)
    return domain

def build(domain_file, regex_file):
    surge_list = format_domain(domain_file)
    return surge_list