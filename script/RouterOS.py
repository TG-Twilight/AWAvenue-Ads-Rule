import json

def format_domain(domain_file):
  domain = []
  with open(domain_file, 'r') as file:
    lines = file.readlines()

  for line in lines:
    domain_line = f"ip dns static add address=240.0.0.1 name={line.strip()}"
    domain.append(domain_line)

  return domain

def build(domain_file, regex_file):
  return  format_domain(domain_file)

if __name__ == '__main__':
  domain_file = 'rule/domain.txt'
  regex_file = 'rule/domain_regex.txt'
  mikrotik_ros= build(domain_file, regex_file)

  with open('mikrotik_ros.rsc', 'w') as file:
    file.write('\n'.join(mikrotik_ros))

  print('生成 mikrotik_ros.rsc 文件成功！')
