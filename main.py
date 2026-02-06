import os
import config
import importlib
import subprocess
from datetime import datetime


def get_latest_git_tag(): # 获取最新的git tag
    process = subprocess.Popen('git tag', stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    tags = output.decode().strip().split('\n')
    
    if tags:
        return tags[-1]
    else:
        return None

def title(comment, module_total, now, commits):
    return f"""{comment}Title: AWAvenue Ads Rule
{comment}--------------------------------------
{comment}Total lines: {module_total}
{comment}Version: {get_latest_git_tag()}
{comment}Update time: {now.strftime("%Y-%m-%d %H:%M:%S")} UTC+8
{comment}Update content: {commits}

{comment}Homepage: https://github.com/TG-Twilight/AWAvenue-Ads-Rule
{comment}License: https://github.com/TG-Twilight/AWAvenue-Ads-Rule/blob/main/LICENSE


"""

def WriteFile(name, text, suffix, comment, module_total, out_path): # 写入文件
    try:
        with open(out_path + "/AWAvenue-Ads-Rule-" + name + suffix, 'w', encoding="utf-8") as file:
        
            if comment != "":
                now = datetime.now()
                commits = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip().replace('\n', '\\n')
                title_text = title(comment, module_total, now, commits)
            else:
                title_text = ""
            file.write(title_text)

            for line in text:
                file.write(line + "\n")
    except Exception as e:
        print(f"写入插件:{name}执行失败: {e}")


def RunScript(rule, out_path):
    rel_out = os.path.relpath(out_path, config.OUT_PATH)
    rule_label = "anti-ad" if rel_out in (".", os.curdir) else rel_out
        
    for filename in os.listdir(config.SCRIPT_PATH): # 遍历script目录下的所有文件
        if not filename.endswith(".py"):
            continue
        plugins_name = filename[:-3]
        full_plugins_name = f"script.{plugins_name}" # 拼接完整的插件名

        try:
            plugins = importlib.import_module(full_plugins_name).build(rule=rule) # 传入规则列表(config.RuleList)类的实例

            # 判断插件是否有list、total、suffix、comment四个属性
            if len(plugins) != 4:
                print(f"规则:{rule_label} 目标:{plugins_name} 执行:失败(缺少必要属性)")
                continue

            total = int(plugins['total'])
            if total <= 0:
                print(f"规则:{rule_label} 目标:{plugins_name} 共计{total}条规则 执行:跳过")
                continue

            WriteFile(plugins_name, plugins['list'], plugins['suffix'], plugins['comment'], str(plugins['total']), out_path)
            print(f"规则:{rule_label} 目标:{plugins_name} 共计{total}条规则 执行:完成")

        except Exception as e:
            print(f"规则:{rule_label} 目标:{plugins_name} 执行:失败({e})")


if __name__ == "__main__":
    subdirs = [d for d in getattr(config, "RULE_SUBDIRS", []) if d]
    required_paths = [config.RULE_PATH, config.SCRIPT_PATH]
    required_paths.extend(os.path.join(config.RULE_PATH, d) for d in subdirs)
    missing_paths = [p for p in required_paths if not os.path.exists(p)]

    if missing_paths:
        print("目录不存在:\n" + "\n".join(missing_paths))
        exit(1)

    targets = [(None, config.OUT_PATH)] + [(d, os.path.join(config.OUT_PATH, d)) for d in subdirs]

    for subdir, out_path in targets:
        os.makedirs(out_path, exist_ok=True)
        
        rule = config.RuleList() if subdir is None else config.RuleList(subdirs=[subdir])
        RunScript(rule, out_path)
