import re
import os
import config
import importlib
import subprocess
import concurrent.futures
from datetime import datetime



def get_latest_git_tag(): # 获取最新的git tag
    process = subprocess.Popen('git tag', stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    tags = output.decode().strip().split('\n')
    if tags:
        return tags[-1]
    else:
        return None


class RuleList:
    def __init__(self, domain_file, regex_file, ip_file, ip6_file):
        self.domain_list, self.domainv6_list = self.domain_file(domain_file)
        self.regex_list = self.regex_file(regex_file)
        self.ip_list = self.ip_file(ip_file)
        self.ip6_list = self.ip6_file(ip6_file)
    

    ## 以下内容由deepseek提供技术支持(bushi

    def domain_file(self, filename):
        with open(filename, 'r') as file:
            domains = {line.strip() for line in file}
        
        valid_domains = set()
        valid_domains_v6 = set()
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            future_to_domain = {executor.submit(config.check_domain, domain): domain for domain in domains}
            for future in concurrent.futures.as_completed(future_to_domain):
                domain = future_to_domain[future]
                result = future.result()
                if result["A"] or result["AAAA"]:
                    valid_domains.add(domain)
                if result["AAAA"]:
                    valid_domains_v6.add(domain)
        return sorted(valid_domains), sorted(valid_domains_v6)
    
    def regex_file(self, filename):
        with open(filename, 'r') as file:
            return sorted({line.strip() for line in file})
    
    def ip_file(self, filename):
        ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        ips = set()
        with open(filename, 'r') as file:
            for line in file:
                ip = line.strip()
                if ipv4_pattern.match(ip):
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
                if ipv6_pattern.match(ip):
                    ips.add(ip)
        return sorted(ips)



def WriteFile(name, text, suffix, comment, module_total): # 写入文件
    try:
        with open(config.OUT_PATH + "/AWAvenue-Ads-Rule-" + name + suffix, 'w', encoding="utf-8") as file:
        
            if comment != "":
                now = datetime.now()
                title = f"""{comment}Title: AWAvenue Ads Rule
{comment}--------------------------------------
{comment}Total lines: {module_total}
{comment}Version: {get_latest_git_tag()}
{comment}Update time: {now.strftime("%Y-%m-%d %H:%M:%S")} UTC+8
{comment}Update content: {subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).strip().decode('utf-8')}

{comment}Homepage: https://github.com/TG-Twilight/AWAvenue-Ads-Rule
{comment}License: https://github.com/TG-Twilight/AWAvenue-Ads-Rule/blob/main/LICENSE


"""
            else:
                title = ""
            file.write(title)
            for line in text:
                file.write(line + "\n")
    except Exception as e:
        print(f"写入插件:{name}执行失败: {e}")


def RunScript():
    rule = RuleList(config.domain_file, config.regex_file, config.ip_file, config.ip6_file)
    config.rule = rule
    
    for filename in os.listdir(config.SCRIPT_PATH): # 遍历script目录下的所有文件
        if filename.endswith(".py"):
            plugins_name = filename[:-3]
            full_plugins_name = f"script.{plugins_name}" # 拼接完整的插件名

            try: 
                plugins = importlib.import_module(full_plugins_name).build(rule=rule) # 传入规则列表(config.RuleList)类的实例
                
                if plugins['list'] == True:
                    print(f"{plugins_name}转换成功")
                    return
                # 判断插件是否有list、total、suffix、comment四个属性
                if len(plugins) == 4:
                    WriteFile(plugins_name, plugins['list'], plugins['suffix'], plugins['comment'], str(plugins['total']))
                    print(f"{plugins_name}转换成功")
                else:
                    print(f"转换插件:{plugins_name}执行失败: 缺少必要属性")
                
            except Exception as e:
                print(f"转换插件:{plugins_name}执行失败: {e}")


if __name__ == "__main__":

    if not os.path.exists(config.RULE_PATH) or not os.path.exists(config.SCRIPT_PATH):
        print("插件或者规则目录不存在!")
        exit(1)
    if not os.path.exists(config.OUT_PATH):
        os.makedirs(config.OUT_PATH)
    RunScript()
