#!/usr/bin/python
# -*- coding:UTF-8 -*-
import requests
import re

def main():
    url = 'https://www.bilibili.com/v/popular/rank/all'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
              "Accept": "application / json, text / plain, * / *",
              "Accept - Encoding": "gzip, deflate, br",
              "Connection": "keep - alive"
              }
    page = requests.get(url=url,headers=header)
    page.encoding = "utf-8"
    page = page.text
    obj = re.compile(r'<li data-id=.*?data-rank="(?P<rank>.*?)".*?<a href="(?P<url>.*?)".*?class="title">(?P<title>.*?)</a>'
                     r'.*?alt="up">(?P<up>.*?)</span>.*?alt="play">(?P<play>.*?)</span>.*?alt="like">(?P<like>.*?)</span>',re.S)
    result = obj.finditer(page)
    for it in result:
        print("排名",it.group("rank"))
        print("网址","https:"+it.group("url"))
        print("标题",it.group("title"))
        print("up主",it.group("up").strip())
        print("播放量",it.group("play").strip())
        print("弹幕",it.group("like").strip())
        print("")
    pass


if __name__ == '__main__':
    main()
