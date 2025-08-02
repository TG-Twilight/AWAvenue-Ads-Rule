# https://help.adblockplus.org/hc/en-us/articles/360062733293-How-to-write-filters

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"||{line.strip()}^"
        domain.append(domain_lines)
    return domain

def format_suffix(List):
    suffix = []
    for line in List:
        suffix_lines = f"||{line.strip()}^"
        suffix.append(suffix_lines)
    return suffix

def format_keyword(List):
    keyword = []
    for line in List:
        keyword_lines = f"*{line.strip()}*"
        keyword.append(keyword_lines)
    return keyword

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"/{line.strip()}/"
        regex.append(regex_lines)
    return regex

def build(rule):
    list = (format_domain(rule.domain_list) + format_suffix(rule.suffix_list) + format_keyword(rule.keyword_list) + format_regex(rule.regex_list))
    return {'list': list, 'suffix': '.txt', 'comment': '!', 'total': len(list)}