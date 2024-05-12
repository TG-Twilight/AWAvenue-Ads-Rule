import os
import sys
import json
import importlib
from datetime import datetime
global output, domain_file, domain_file, suffix_file, regex_file

SCRIPT_PATH = os.path.join(os.getcwd(), "script")
RULE_PATH = os.path.join(os.getcwd(), "rule")
OUT_PATH = os.getcwd() + "/out"
domain_file=RULE_PATH + "/domain.txt"
regex_file=RULE_PATH + "/domain_regex.txt"
ip_file=RULE_PATH + "/ip.txt"
ip6_file=RULE_PATH + "/ip6.txt"

if not os.path.exists(OUT_PATH):
    print(f"{OUT_PATH} 目录不存在!")
    sys.exit(1)

class RuleList:
    def __init__(self, domain_file, regex_file, ip_file, ip6_file):
        with open(domain_file, 'r') as file:
            self.domain_list = file.readlines()
        with open(regex_file, 'r') as file:
            self.regex_list = file.readlines()
        with open(ip_file, 'r') as file:
            self.ip_list = file.readlines()
        with open(ip6_file, 'r') as file:
            self.ip6_list = file.readlines()

rule = RuleList(domain_file, regex_file, ip_file, ip6_file)

def WriteFile(name, text, suffix):
    try:
        with open(OUT_PATH + "/AWAvenue-Ads-Rule-" + name + suffix, 'w', encoding="utf-8") as file:
            for line in text:
                file.write(line + "\n")
    except Exception as e:
        print(f"写入插件:{module_name}执行失败: {e}")

def RunScript():
    for filename in os.listdir(SCRIPT_PATH):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            full_module_name = f"script.{module_name}"
            try:
                module = importlib.import_module(full_module_name)
                module_list, module_suffix = module.build(rule)
                WriteFile(module_name, module_list, module_suffix)
            except Exception as e:
                print(f"转换插件:{module_name}执行失败: {e}")


if __name__ == "__main__":
    RunScript()
