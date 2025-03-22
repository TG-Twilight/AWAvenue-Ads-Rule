import os
import dns.resolver


SCRIPT_PATH = os.path.join(os.getcwd(), "script") # 插件文件夹
RULE_PATH = os.path.join(os.getcwd(), "rule") # 规则文件夹
OUT_PATH = os.getcwd() + "/out" # 输出文件夹
domain_file=RULE_PATH + "/domain.txt" # 规则文件
regex_file=RULE_PATH + "/domain_regex.txt" # 正则规则文件
ip_file=RULE_PATH + "/ip.txt" # IP规则文件
ip6_file=RULE_PATH + "/ip6.txt" # IPv6规则文件


def check_domain(domain):
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '1.1.1.1', '223.5.5.5', '9.9.9.9', '94.140.14.140']
        resolver.timeout = 1
        resolver.lifetime = 5

        A = resolver.resolve(domain, "A", raise_on_no_answer=False)
        AAAA = resolver.resolve(domain, "AAAA", raise_on_no_answer=False)
        # 返回包含 A 和 AAAA 记录的字典
        return {"A": bool(A.rrset), "AAAA": bool(AAAA.rrset)}
    except dns.resolver.NXDOMAIN:
        print(f"未查询到 {domain} 的解析记录")
        return {"A": False, "AAAA": False}
    except Exception as e:
        print(f"查询 {domain} 时发生错误: {e}")
        return {"A": False, "AAAA": False}