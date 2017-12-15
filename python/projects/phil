#!/usr/bin/env python3
import urllib.request
url = input("wikipedia url > ")
while True:
    site = urllib.request.urlopen(url)
    html = str(site.read()).lower()
    print(url) 
    url = url.lower()
    title = '<b>'
    titlewords = url.split('/wiki/')[1].split('_')
    for x in range(0, (len(titlewords) - 1)):
        title += titlewords[x] + ' '
    title += titlewords[-1] + '</b>'
    linkid = 1
    firstlink = html.split(title)[1].split('<a href="')[linkid].split('"')[0]
    while firstlink.split(firstlink[9])[0] == "cite_note":
        linkid += 2
    firstlink = html.split(title)[1].split('<a href="')[linkid].split('"')[0]
    url = "https://en.wikipedia.org" + firstlink
