# coding=utf-8
from flask import Flask, request
import spiderproxy
import  random
import  本地ip代理验证

app = Flask(__name__)


# proxy_list = spiderproxy.result
# print(proxy_list)
#改进,多种来源添加,定义一个函数,全部添加进入proxy_list
#proxy_list = spiderproxy.result


# proxy_list2 = []
# validated_proxy_dict = {}
# for i,proxy in enumerate(本地ip代理验证.use_proxy_list):
#     if validated_proxy_dict.get(proxy, True):
#         print(f"代理 {proxy} 已经被验证过")

#异步加载将代理池的数据添加进行如
#热加载

@app.route('/')
def get_proxy():
    proxy_list2 = 本地ip代理验证.use_proxy_list
    proxy2 = random.choice(proxy_list2)
    return proxy2


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
