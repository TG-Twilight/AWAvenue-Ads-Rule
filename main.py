import os
import sys
import json
import importlib
import subprocess
from datetime import datetime

SCRIPT_PATH = os.path.join(os.getcwd(), "script")
RULE_PATH = os.path.join(os.getcwd(), "rule")
OUT_PATH = os.getcwd() + "/out"
domain_file=RULE_PATH + "/domain.txt"
regex_file=RULE_PATH + "/domain_regex.txt"
ip_file=RULE_PATH + "/ip.txt"
ip6_file=RULE_PATH + "/ip6.txt"
current_time = datetime.now()
format_time = current_time.strftime("%Y-%m-%d")
process = subprocess.Popen('git tag | tail -1', stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()
tag = output.decode().strip()

if not os.path.exists(OUT_PATH):
    print(f"{OUT_PATH} 目录不存在!")
    sys.exit(1)

class RuleList:
    def __init__(self, domain_file, regex_file, ip_file, ip6_file):
        with open(domain_file, 'r') as file:
            lines = file.read().splitlines()
            self.domain_list = sorted(set(lines))
        with open(regex_file, 'r') as file:
            lines = file.read().splitlines()
            self.regex_list = sorted(set(lines))
        with open(ip_file, 'r') as file:
            lines = file.read().splitlines()
            self.ip_list = sorted(set(lines))
        with open(ip6_file, 'r') as file:
            lines = file.read().splitlines()
            self.ip6_list = sorted(set(lines))


rule = RuleList(domain_file, regex_file, ip_file, ip6_file)

def WriteFile(name, text, suffix, comment):
    try:
        with open(OUT_PATH + "/AWAvenue-Ads-Rule-" + name + suffix, 'w', encoding="utf-8") as file:
            file.write(f"{comment}Title: AWAvenue 秋风广告规则（AWAvenue-Ads-Rule）\n\n{comment}版本号: {tag}\n{comment}上次更新日期: {format_time}\n\n{comment}项目地址：https://github.com/TG-Twilight/AWAvenue-Ads-Rule\n\n{comment}如果需要在其它规则中混合此规则，请在您的规则显眼处注明本规则的出处，谢谢！\n{comment}加入Telegram群组 秋風がく山道 (@AWAvenueAdsChat) 与编写者交流，期待着您的到来！\n{comment}群组链接：https://t.me/AWAvenueAdsChat\n{comment}订阅Telegram频道 AWAvenue Ads Rule (@AWAvenueAdsRule) 获取最新公告，期待着您的订阅！\n{comment}频道链接：https://t.me/AWAvenueAdsRule\n\n{comment}This project is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.\n\n{comment}AD:\n{comment}倾城极速 - 畅游世界，高速互联！官网：https://panel.qqcjs.top 官网2：https://n3b53vrt.wcnmdmht.biz\n\n\n")
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
                module_list, module_suffix, module_comment = module.build(rule)
                WriteFile(module_name, module_list, module_suffix, module_comment)
            except Exception as e:
                print(f"转换插件:{module_name}执行失败: {e}")


if __name__ == "__main__":
    RunScript()
