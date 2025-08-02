# https://wiki.archlinuxcn.org/wiki/Dnsmasq#%E5%9F%9F%E5%90%8D%E9%98%BB%E6%AD%A2%E5%88%97%E8%A1%A8
def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"address=/{line.strip()}/#"
        domain.append(domain_lines)
    return domain


def build(rule):
    list = format_domain(rule.domain_list)
    return {'list': list, 'suffix': '.conf', 'comment': '#', 'total': len(list)}
