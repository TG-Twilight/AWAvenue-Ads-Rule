import os
import sys
import json
import importlib
import subprocess
import datetime

SCRIPT_PATH = os.path.join(os.getcwd(), "script")
RULE_PATH = os.path.join(os.getcwd(), "rule")
OUT_PATH = os.getcwd() + "/out"
domain_file=RULE_PATH + "/domain.txt"
regex_file=RULE_PATH + "/domain_regex.txt"
ip_file=RULE_PATH + "/ip.txt"
ip6_file=RULE_PATH + "/ip6.txt"
current_time = datetime.datetime.now(datetime.timezone.utc)
format_time = current_time.isoformat()


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

def get_latest_git_tag():
    process = subprocess.Popen('git tag', stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    tags = output.decode().strip().split('\n')
    if tags:
        return tags[-1]
    else:
        return None

def WriteFile(name, text, suffix, comment, module_total):
    try:
        with open(OUT_PATH + "/AWAvenue-Ads-Rule-" + name + suffix, 'w', encoding="utf-8") as file:
            title = f"""{comment}Title: AWAvenue Ads Rule
{comment}Last modified: {format_time}
{comment}--------------------------------------
{comment}Total lines: {module_total}
{comment}Version: {get_latest_git_tag()}

{comment}Homepage: https://github.com/TG-Twilight/AWAvenue-Ads-Rule
{comment}License: https://github.com/TG-Twilight/AWAvenue-Ads-Rule/blob/main/LICENSE


"""
            file.write(title)
            for line in text:
                file.write(line + "\n")
    except Exception as e:
        print(f"写入插件:{name}执行失败: {e}")

def RunScript():
    for filename in os.listdir(SCRIPT_PATH):
        if filename.endswith(".py"):
            plugins_name = filename[:-3]
            full_plugins_name = f"script.{plugins_name}"
            try:
                plugins = importlib.import_module(full_plugins_name).build(rule)
                if plugins['list'] and plugins['total'] and plugins['suffix'] and plugins['comment']:
                    WriteFile(plugins_name, plugins['list'], plugins['suffix'], plugins['comment'], str(plugins['total']))
                else:
                    print(f"转换插件:{plugins_name}执行失败: 无数据")
                
            except Exception as e:
                print(f"转换插件:{plugins_name}执行失败: {e}")


if __name__ == "__main__":
    RunScript()
