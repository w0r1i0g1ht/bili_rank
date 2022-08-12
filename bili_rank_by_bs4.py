#!/usr/bin/python
# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.bilibili.com/v/popular/rank/all"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
              "Accept": "application / json, text / plain, * / *",
              "Accept - Encoding": "gzip, deflate, br",
              "Connection": "keep - alive"
              }
    page = requests.get(url=url, headers=header)
    page = BeautifulSoup(page.text,"html.parser")
    lis = page.find_all("li",attrs={"class":"rank-item"})
    for li in lis:
        rank = li.get("data-rank")
        address = li.find("div",attrs={"class":"info"}).find("a").get("href")
        title = li.find("div",attrs={"class":"info"}).find("a").text
        up = li.find("div",attrs={"class":"detail"}).find("span").text
        play = li.find("div",attrs={"class":"detail-state"}).find_all("span")[0].text
        like = li.find("div", attrs={"class": "detail-state"}).find_all("span")[1].text
        print("排名",rank)
        print("网址", "https:" + address)
        print("标题",title)
        print("up主",up.strip())
        print("播放量",play.strip())
        print("弹幕",like.strip())
        print("")
    pass


if __name__ == '__main__':
    main()
