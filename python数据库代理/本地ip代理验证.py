import  requests
from concurrent.futures import ThreadPoolExecutor
import spiderproxy



file = r"C:\Users\21016.LAPTOP-KGP1GRG0\Desktop\ip.txt"
proxy_list = []
with open(file) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    proxy_list.extend(lines)
f.close()

# a = spiderproxy.getip()
# print(type(a))



executor = ThreadPoolExecutor()

#添加验证,默认为flase,验证过的值为true

def requestmethon():
    global use_proxy_list
    use_proxy_list = []
    validated_proxy_dict = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    for i, proxy in enumerate(proxy_list):
        # if validated_proxy_dict.get(proxy, True):
        #     print(f"代理 {proxy} 已经被验证过")
        #     continue
        proxy_dict = {'http': 'http://' + proxy}
        try:
            test = requests.get("https://www.baidu.com/", headers=headers, proxies=proxy_dict, timeout=1)
            if test.status_code == 200:
                use_proxy_list.append(proxy_dict['http'])
                print(f"代理 {proxy_dict['http']} 可用")
        except:
            print(f"代理 {proxy_dict['http']} 不可用")
    return use_proxy_list



requestmethon()

executor.submit(requestmethon,use_proxy_list)

print("可以的代理数量为",len(use_proxy_list))
print("可用代理列表：", use_proxy_list)


#result = requestmethon()
#需要哪个调用哪个的值

for ip in use_proxy_list:
    with open("test.txt",'a') as f:
        f.write(ip + '\n')
f.close()








