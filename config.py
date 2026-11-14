import os
import sys
import ipaddress

SCRIPT_PATH = os.path.join(os.getcwd(), "script") # 插件文件夹
RULE_PATH = os.path.join(os.getcwd(), "rule") # 规则文件夹
OUT_PATH = os.getcwd() + "/out" # 输出文件夹

RULE_SUBDIRS = ["", "privacy", "unwelcome"] # 规则子目录列表

# 构建变体: (文件名标签, 参与合并的规则子目录)
# "" 为默认完整规则(广告+隐私+不受欢迎), 其余三种为细分订阅
VARIANTS = [
    ("", RULE_SUBDIRS),
    ("-Only.Ads", [""]),
    ("-No.Privacy", ["", "unwelcome"]),
    ("-No.Unwelcome", ["", "privacy"]),
]

def _rule_file_paths(filename, subdirs=None):
    paths = []
    for subdir in (RULE_SUBDIRS if subdirs is None else subdirs):
        base = RULE_PATH if subdir == "" else os.path.join(RULE_PATH, subdir)
        paths.append(os.path.join(base, filename))
    return paths

class RuleList:
    def __init__(self, subdirs=None):
        self.domain_list = self.domain_file(_rule_file_paths("domain.txt", subdirs))
        self.regex_list = self.regex_file(_rule_file_paths("domain_regex.txt", subdirs))
        self.suffix_list = self.suffix_file(_rule_file_paths("domain_suffix.txt", subdirs))
        self.keyword_list = self.keyword_file(_rule_file_paths("domain_keyword.txt", subdirs))
        self.ip_list = self.ip_file(_rule_file_paths("ip.txt", subdirs))
        self.ip6_list = self.ip6_file(_rule_file_paths("ip6.txt", subdirs))

    ## 以下内容由deepseek提供技术支持(bushi

    def _read_lines(self, filenames):
        items = set()
        for filename in filenames:
            if not os.path.exists(filename):
                continue
            with open(filename, 'r') as file:
                items.update({line.strip() for line in file if line.strip()})
        return sorted(items)

    def domain_file(self, filenames):
        return self._read_lines(filenames)

    def suffix_file(self, filenames):
        return self._read_lines(filenames)

    def keyword_file(self, filenames):
        return self._read_lines(filenames)
    
    def regex_file(self, filenames):
        return self._read_lines(filenames)

    def _ip_networks(self, filenames, network_cls):
        # 同时接受纯 IP 与 CIDR(如 1.2.3.4 / 1.2.3.4/32)，统一输出 CIDR 写法供插件生成 IP-CIDR 规则
        ips = set()
        for filename in filenames:
            if not os.path.exists(filename):
                continue
            with open(filename, 'r') as file:
                for line in file:
                    ip = line.strip()
                    if not ip:
                        continue
                    try:
                        ips.add(str(network_cls(ip)))
                    except ValueError:
                        print(f"[警告] 跳过无效 IP 规则: {ip} ({filename})", file=sys.stderr)
        return sorted(ips)

    def ip_file(self, filenames):
        return self._ip_networks(filenames, ipaddress.IPv4Network)

    def ip6_file(self, filenames):
        return self._ip_networks(filenames, ipaddress.IPv6Network)