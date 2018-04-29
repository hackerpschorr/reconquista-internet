import urllib.request
import re
import random
import json
import ast

def proxy_list_fetch():
    with urllib.request.urlopen("https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list") as response:
        return proxy_list_parse(response.read())

def proxy_list_parse(string):
    string = string.decode("utf-8")
    lines = string.split("\n")
    proxiess = []
    for line in lines:
        if(line):
            decoded = json.loads(line)
            if (decoded['anonymity'] != 'transparent'):
                proxiess.append(decoded)
    return proxiess

def get_random_proxy():
    proxies = proxy_list_fetch()
    randmax = len(proxies) - 1
    proxy = proxies[random.randint(0,randmax)]
    return proxy['host'] + ":" + str(proxy['port'])