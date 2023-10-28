import requests
from bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor


url = "http://www.ip3366.net/free/?stype=1&page=2"
response = requests.get(url)
html_content = response.content.decode('gbk')

soup = BeautifulSoup(html_content, 'html.parser')

ip_pattern = re.compile(r'<td>([\d.]+)</td>')
port_pattern = re.compile(r'<td>(\d+)</td>')

ip_list = []
port_list = []

for td in soup.find_all('td'):
    td_str = str(td)
    ip_match = re.search(ip_pattern, td_str)
    port_match = re.search(port_pattern, td_str)

    if ip_match:
        ip_value = (ip_match.group(1))
        if 5 < len(ip_value) <= 17:
            ip_list.append(ip_value)


    if port_match:
        port_value = port_match.group(1)
        if len(port_value) <= 4:
            port_list.append(port_value)


# def getip():
#     for ip, port in zip(ip_list, port_list):
#         b = ip + ':' + port
#         get_ip = []
#         for i in b:
#             print(get_ip)



def getip():
    get_ip = []
    for ip, port in zip(ip_list, port_list):
        b = ip + ':' + port
        get_ip.append(b)

    return get_ip

getip()

result = getip()
print(result)

