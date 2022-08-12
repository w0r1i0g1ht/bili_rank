#!/usr/bin/python
# -*- coding:UTF-8 -*-
from lxml import etree
import requests

def main():
    url = "https://www.bilibili.com/v/popular/rank/all"
    header = {"User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
              "Accept": "application / json, text / plain, * / *",
              "Accept - Encoding": "gzip, deflate, br",
              "Connection": "keep - alive"
    }
    page = requests.get(url=url,headers=header)
    page = page.text
    tree = etree.HTML(page)
    divs = tree.xpath("/html/body/div[3]/div/div[2]/div[2]/ul/li")
    for div in divs:
        rank = div.xpath("./@data-rank")
        address = div.xpath("./div/div[2]/a/@href")
        title = div.xpath("./div/div[2]/a/text()")
        up = div.xpath("./div/div[2]/div/a/span/text()")
        play = div.xpath("./div/div[2]/div/div/span[1]/text()")
        like = div.xpath("./div/div[2]/div/div/span[2]/text()")
        print("排名",rank[0])
        print("网址","https:"+address[0])
        print("标题",title[0])
        print("up主",up[0].strip())
        print("播放量",play[0].strip())
        print("弹幕",like[0].strip())
        print("")
    pass


if __name__ == '__main__':
    main()
