#!/usr/bin/env python3
#encoding=utf-8

#Author : Wallace Huang
#Time   : 2016-9-28 16:38:47
#License: MIT

import os,sys,urllib.request,re,time

keyword = input("Please input a key word: ")
url1='https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + str(keyword)
#url_param = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + keyword
mailpattern = re.compile('[^\._:>\\-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+')
imgPattren = re.compile('<img class=*？ src="*.jpg"?')

#Get HTML context


def getHtml(url):
    print('Request url is:  '+url)
    file = urllib.request.urlopen(url)
    html = file.read()
    html = html.decode('utf8')
    return html

#GET the Regular matching data back, return List(...)
def getData(html,reg):
    reg = re.compile(reg)
    list = re.findall(reg,html)
    return list

html=getHtml(url1)

#res=getData(html,imgPattren)

print(html)


