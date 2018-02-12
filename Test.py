# encoding=utf-8

import requests
import Header as H

def getHTML(url):
    r = requests.get(url, headers=H.head)
    return r.text

result = ''
page = getHTML('http://sc.stock.cnfol.com/ggzixun/')

print(page)