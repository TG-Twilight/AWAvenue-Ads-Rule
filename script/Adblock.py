def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"||{line.strip()}^"
        domain.append(domain_lines)
    return domain


def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"/{line.strip()}/".replace("\.","\\\.").replace("\*","\.\*")
        regex.append(regex_lines)
    return regex

def build(rule):
    Adblock_list = format_domain(rule.domain_list) + format_regex(rule.regex_list)
    return Adblock_list, ".txt", "!"