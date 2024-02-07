import os
import sys
import json
import importlib
from datetime import datetime


try:
    with open("build.json", 'r', encoding="utf-8") as file:
        config = json.loads(file.read())
except Exception as e:
    print(f"读取json失败: {e}")
    sys.exit(1)

global output, domain_file, domain_file, suffix_file, regex_file
current_time = datetime.now()
format_time = current_time.strftime("%Y-%m-%d")
SCRIPT_PATH = os.path.join(os.getcwd(), "script")
RULE_PATH = os.path.join(os.getcwd(), "rule")
OUT_PATH = os.getcwd() + config["out_path"]
domain_file=RULE_PATH + "/" + config["domain_name"]
regex_file=RULE_PATH + "/" + config["regex_name"]

if not os.path.exists(OUT_PATH):
    print(f"{OUT_PATH} 目录不存在!")
    sys.exit(1)

def WriteFile(name, text):
    try:
        for File in config["suffix"]:
            if name == File["name"]:
                with open(OUT_PATH + "/AWAvenue-Ads-Rule-" + name + File["suffix"], 'w', encoding="utf-8") as file:
                    title = [File["comment"] + " " + line for line in config["title"].split('\n')]
                    title = '\n'.join(title)
                    file.write(title.replace("version", config["version"]).replace("format_time", format_time) + "\n\n")
                    for line in text:
                        file.write(line + "\n")
    except Exception as e:
        print(f"读取json失败: {e}")

def RunScript():
    for filename in os.listdir(SCRIPT_PATH):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            full_module_name = f"script.{module_name}"
            try:
                module = importlib.import_module(full_module_name)
                print(f"正在转换:{module_name}")
                module_list = module.build(domain_file, regex_file)
                WriteFile(module_name, module_list)
            except ImportError as e:
                print(f"转换插件:{module_name}执行失败: {e}")


if __name__ == "__main__":
    RunScript()
