# encoding=utf-8

import requests
import Header as H

def getHTML(url):
    r = requests.get(url, headers=H.head)
    return r.text

page = getHTML('http://stock.10jqka.com.cn/gegugg_list/')

print(page)