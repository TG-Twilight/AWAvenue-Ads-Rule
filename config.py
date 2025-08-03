import os
import re

SCRIPT_PATH = os.path.join(os.getcwd(), "script") # 插件文件夹
RULE_PATH = os.path.join(os.getcwd(), "rule") # 规则文件夹
OUT_PATH = os.getcwd() + "/out" # 输出文件夹
domain_file=RULE_PATH + "/domain.txt" # 规则文件
regex_file=RULE_PATH + "/domain_regex.txt" # 正则规则文件
suffix_file=RULE_PATH + "/domain_suffix.txt" # 后缀规则文件
keyword_file=RULE_PATH + "/domain_keyword.txt" # 关键词规则文件
ip_file=RULE_PATH + "/ip.txt" # IP规则文件
ip6_file=RULE_PATH + "/ip6.txt" # IPv6规则文件

class RuleList:
    def __init__(self):
        self.domain_list = self.domain_file(domain_file)
        self.regex_list = self.regex_file(regex_file)
        self.suffix_list = self.suffix_file(suffix_file)
        self.keyword_list = self.keyword_file(keyword_file)
        self.ip_list = self.ip_file(ip_file)
        self.ip6_list = self.ip6_file(ip6_file)

    ## 以下内容由deepseek提供技术支持(bushi

    def domain_file(self, filename):
        with open(filename, 'r') as file:
            return sorted({line.strip() for line in file if line.strip()})

    def suffix_file(self, filename):
        with open(filename, 'r') as file:
            return sorted({line.strip() for line in file if line.strip()})

    def keyword_file(self, filename):
        with open(filename, 'r') as file:
            return sorted({line.strip() for line in file if line.strip()})
    
    def regex_file(self, filename):
        with open(filename, 'r') as file:
            return sorted({line.strip() for line in file if line.strip()})

    def ip_file(self, filename):
        ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        ips = set()
        with open(filename, 'r') as file:
            for line in file:
                ip = line.strip()
                if ip and ipv4_pattern.match(ip):  # 添加空白检查
                    parts = ip.split('.')
                    if all(0 <= int(part) <= 255 for part in parts):
                        ips.add(ip)
        return sorted(ips)
    
    def ip6_file(self, filename):
        ipv6_pattern = re.compile(r'^([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}$')
        ips = set()
        with open(filename, 'r') as file:
            for line in file:
                ip = line.strip()
                if ip and ipv6_pattern.match(ip):  # 添加空白检查
                    ips.add(ip)
        return sorted(ips)