import os
import config
import importlib
import subprocess
from datetime import datetime


rule = config.RuleList()


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
                    print(f"{plugins_name}转换成功 共计 "+ str(plugins['total'])+ " 条规则")
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
