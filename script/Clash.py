# https://wiki.metacubex.one/handbook/syntax/#_8
# https://wiki.metacubex.one/config/rule-providers/content/#domain

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"  - '{line.strip()}'"
        domain.append(domain_lines)
    return domain

def format_suffix(List):
    suffix = []
    for line in List:
        suffix_lines = f"  - '+.{line.strip()}'"
        suffix.append(suffix_lines)
    return suffix


def build(rule):
    list = format_domain(rule.domain_list) + format_suffix(rule.suffix_list)
    return {'list': ["payload:"] + list, 'suffix': '.yaml', 'comment': '#', 'total': len(list)}