from datetime import datetime


def format_comments():
    now = datetime.now()
    comments = ["#!name=AWAvenue Ads Rule",
                f'#!desc=Update time: {now.strftime("%Y-%m-%d %H:%M:%S")} UTC+8\\nHomepage: https://github.com/TG-Twilight/AWAvenue-Ads-Rule',
                "#!category=广告拦截",
                "#!author=TG-Twilight[https://github.com/TG-Twilight]",
                "#!icon=https://avatars.githubusercontent.com/u/121682528?s=144",
                "#!homepage=https://awavenue.top",
                "", "[Rule]"]
    return comments

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"DOMAIN,{line.strip()},REJECT,extended-matching,pre-matching"
        domain.append(domain_lines)
    return domain

def format_suffix(List):
    suffix = []
    for line in List:
        suffix_lines = f"DOMAIN-SUFFIX,{line.strip()},REJECT,extended-matching,pre-matching"
        suffix.append(suffix_lines)
    return suffix

def format_keyword(List):
    keyword = []
    for line in List:
        keyword_lines = f"DOMAIN-KEYWORD,{line.strip()},REJECT,extended-matching,pre-matching"
        keyword.append(keyword_lines)
    return keyword

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"DOMAIN-REGEX,{line.strip()},REJECT,extended-matching,pre-matching"
        regex.append(regex_lines)
    return regex

def format_ip(List):
    ip = []
    for line in List:
        ip_lines = f"IP-CIDR,{line.strip()},REJECT,pre-matching"
        ip.append(ip_lines)
    return ip

def build(rule):
    list = format_comments() + format_ip(rule.ip_list) + format_domain(rule.domain_list) + format_regex(rule.regex_list)
    return {'list': list, 'suffix': '.sgmodule', 'comment': '', 'total': len(list)}
