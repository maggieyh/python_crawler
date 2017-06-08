import requests
from lxml import html
from bs4 import BeautifulSoup
# name = raw_input()
name = "movie"
r = requests.get('https://www.ptt.cc/bbs/{0}/index1.html'.format(name))
# print(r.status_code)
if(r.status_code != requests.codes.ok):
    print("None")
else:
#     print(r.text)
    tml = BeautifulSoup(r.text)
    for i in tml.find_all("div", class_ = "r-ent"):
        url ="https://www.ptt.cc/{0}".format(i.find("a")["href"])
        tmp = requests.get(url)
        sp = BeautifulSoup(tmp.text).find_all("span", class_ = "article-meta-value")
        for j in sp:
            print(j.text)
        print(BeautifulSoup(tmp.text).find("div", id = ))
        print('-------------------------')
       
# text = r.text
# j = r.json
# print(r.headers)
