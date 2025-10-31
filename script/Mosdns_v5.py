import json

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"full:{line.strip()}"
        domain.append(domain_lines)
    return domain

def format_suffix(List):
    suffix = []
    for line in List:
        suffix_lines = f"domain:{line.strip()}"
        suffix.append(suffix_lines)
    return suffix

def format_keyword(List):
    keyword = []
    for line in List:
        keyword_lines = f"keyword:{line.strip()}"
        keyword.append(keyword_lines)
    return keyword

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"regexp:{line.strip()}"
        regex.append(regex_lines)
    return regex

def build(rule):
    list = format_domain(rule.domain_list) + format_suffix(rule.suffix_list) + format_keyword(rule.keyword_list) + format_regex(rule.regex_list)
    return {'list': list, 'suffix': '.txt', 'comment': '#', 'total': len(list)}

