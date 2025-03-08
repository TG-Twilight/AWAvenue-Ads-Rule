import os
import importlib
import subprocess

SCRIPT_PATH = os.path.join(os.getcwd(), "script") # 插件文件夹
RULE_PATH = os.path.join(os.getcwd(), "rule") # 规则文件夹
OUT_PATH = os.getcwd() + "/out" # 输出文件夹
domain_file=RULE_PATH + "/domain.txt" # 规则文件
regex_file=RULE_PATH + "/domain_regex.txt" # 正则规则文件
ip_file=RULE_PATH + "/ip.txt" # IP规则文件
ip6_file=RULE_PATH + "/ip6.txt" # IPv6规则文件

def get_latest_git_tag(): # 获取最新的git tag
    process = subprocess.Popen('git tag', stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    tags = output.decode().strip().split('\n')
    if tags:
        return tags[-1]
    else:
        return None

def WriteFile(name, text, suffix, comment, module_total): # 写入文件
    try:
        with open(OUT_PATH + "/AWAvenue-Ads-Rule-" + name + suffix, 'w', encoding="utf-8") as file:
        
            if comment != "":
                title = f"""{comment}Title: AWAvenue Ads Rule
{comment}--------------------------------------
{comment}Total lines: {module_total}
{comment}Version: {get_latest_git_tag()}
{comment}Updated content: {subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).strip().decode('utf-8')}

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
    for filename in os.listdir(SCRIPT_PATH): # 遍历script目录下的所有文件
        if filename.endswith(".py"):
            plugins_name = filename[:-3]
            full_plugins_name = f"script.{plugins_name}" # 拼接完整的插件名

            try: 
                plugins = importlib.import_module(full_plugins_name).build(rule) # 传入规则列表(RuleList)类的实例
                print(f"{plugins_name}转换成功")

                # 判断插件是否有list、total、suffix、comment四个属性
                if len(plugins) == 4:
                    WriteFile(plugins_name, plugins['list'], plugins['suffix'], plugins['comment'], str(plugins['total']))
                else:
                    print(f"转换插件:{plugins_name}执行失败: 缺少必要属性")
                
            except Exception as e:
                print(f"转换插件:{plugins_name}执行失败: {e}")


if __name__ == "__main__":
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
    
    RunScript()
