import socket
import requests
import json
import re

# 得到ip方式一：
response = requests.get('http://10.9.1.3')
ip = re.search(r"v46ip='\d+.\d+.\d+.\d+'", response.text).group().split('=')[1].strip('\'')
print("本机ip："+ip)

# # 得到ip方式二：
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('8.8.8.8', 80))
# ip = s.getsockname()[0]
# s.close()
# print("本机ip："+ip)

try:
    with open("config.json", encoding='utf-8') as f:
        config = json.load(f)
except IOError as err:
    print("配置文件错误")
    print("File error:"+str(err))
else:
    ISP={'中国移动': '@zgyd', '中国电信': '@ctc'}
    headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://10.9.1.3/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    params = (
        ('c', 'Portal'),
        ('a', 'login'),
        ('callback', 'dr1003'),
        ('login_method', '1'),
        ('user_account', ',b,'+config["学号"]+ISP[config["运营商"]]),
        ('user_password', config["密码"]),
        ('wlan_user_ip', ip), 
        ('wlan_user_ipv6', ''),
        ('wlan_user_mac', '000000000000'),
        ('wlan_ac_ip', ''),
        ('wlan_ac_name', ''),
        ('jsVersion', '3.3.3'),
        )
    response = requests.get('http://10.9.1.3:801/eportal/', headers=headers, params=params, verify=False)
    print(response)
