import urllib.request
import re
import json
import ast

def proxy_list_fetch():
    with urllib.request.urlopen("https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list") as response:
        proxy_list_parse(response.read())

def proxy_list_parse(string):
    string = string.decode("utf-8")
    lines = string.split("\n")
    proxiess = []
    for line in lines:
        if(line):
            proxiess.append(json.loads(line))
    return proxiess
