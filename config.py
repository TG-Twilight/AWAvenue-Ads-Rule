import os
import re

SCRIPT_PATH = os.path.join(os.getcwd(), "script") # 插件文件夹
RULE_PATH = os.path.join(os.getcwd(), "rule") # 规则文件夹
OUT_PATH = os.getcwd() + "/out" # 输出文件夹

RULE_SUBDIRS = ["", "privacy", "unwelcome"] # 规则子目录列表

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

    def ip_file(self, filenames):
        ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        ips = set()
        for filename in filenames:
            if not os.path.exists(filename):
                continue
            with open(filename, 'r') as file:
                for line in file:
                    ip = line.strip()
                    if ip and ipv4_pattern.match(ip):  # 添加空白检查
                        parts = ip.split('.')
                        if all(0 <= int(part) <= 255 for part in parts):
                            ips.add(ip)
        return sorted(ips)
    
    def ip6_file(self, filenames):
        ipv6_pattern = re.compile(r'^([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}$')
        ips = set()
        for filename in filenames:
            if not os.path.exists(filename):
                continue
            with open(filename, 'r') as file:
                for line in file:
                    ip = line.strip()
                    if ip and ipv6_pattern.match(ip):  # 添加空白检查
                        ips.add(ip)
        return sorted(ips)