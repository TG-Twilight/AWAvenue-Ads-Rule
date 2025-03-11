import os

SCRIPT_PATH = os.path.join(os.getcwd(), "script") # 插件文件夹
RULE_PATH = os.path.join(os.getcwd(), "rule") # 规则文件夹
OUT_PATH = os.getcwd() + "/out" # 输出文件夹
domain_file=RULE_PATH + "/domain.txt" # 规则文件
regex_file=RULE_PATH + "/domain_regex.txt" # 正则规则文件
ip_file=RULE_PATH + "/ip.txt" # IP规则文件
ip6_file=RULE_PATH + "/ip6.txt" # IPv6规则文件

if not os.path.exists(OUT_PATH) or not os.path.exists(OUT_PATH):
    print("插件或者规则目录不存在!")
    exit(1)
if not os.path.exists(OUT_PATH):
    os.makedirs(OUT_PATH)

class RuleList:
    # 初始化规则列表
     def __init__(self, domain_file, regex_file, ip_file, ip6_file):
        with open(domain_file, 'r') as file:
            self.domain_list = sorted(set(line.strip() for line in file))
        with open(regex_file, 'r') as file:
            self.regex_list = sorted(set(line.strip() for line in file))
        with open(ip_file, 'r') as file:
           self.ip_list = sorted(set(line.strip() for line in file))
        with open(ip6_file, 'r') as file:
            self.ip6_list = sorted(set(line.strip() for line in file))
rule = RuleList(domain_file, regex_file, ip_file, ip6_file)