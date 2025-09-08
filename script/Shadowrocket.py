
def format_comments():
    now = datetime.now()
    comments = ["#!name=AWAvenue Ads Rule",
                f'#!desc=Update time: {now.strftime("%Y-%m-%d %H:%M:%S")} UTC+8\\nHomepage: https://github.com/TG-Twilight/AWAvenue-Ads-Rule',
                "#!category=广告拦截",
                "#!author=TG-Twilight[https://github.com/TG-Twilight]",
                "#!icon=https://avatars.githubusercontent.com/u/121682528?s=144",
                "#!homepage=https://awavenue.top",
                "", ""]
    return comments

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"DOMAIN-SUFFIX,{line.strip()},Reject"
        domain.append(domain_lines)
    return domain

def format_ip(List):
    ip = []
    for line in List:
        ip_lines = f"IP-CIDR,{line.strip()},Reject"
        ip.append(ip_lines)
    return ip

def build(rule):
    list = format_comments() + format_ip(rule.ip_list) + format_domain(rule.domain_list)
    return {'list': list, 'suffix': '.conf', 'comment': '#', 'total': len(list)}
