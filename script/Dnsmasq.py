# https://wiki.archlinuxcn.org/wiki/Dnsmasq#%E5%9F%9F%E5%90%8D%E9%98%BB%E6%AD%A2%E5%88%97%E8%A1%A8
def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"address=/{line.strip()}/#"
        domain.append(domain_lines)
    return domain


def build(rule):
    # address=/domain/# 本身即匹配该域名及其全部子域, 故 suffix 规则用同一语法表达
    list = format_domain(sorted(set(rule.domain_list) | set(rule.suffix_list)))
    return {'list': list, 'suffix': '.conf', 'comment': '#', 'total': len(list)}
