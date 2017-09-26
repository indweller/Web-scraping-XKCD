import requests
import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

n1 = int(input())
n2 = int(input())
add = input()

for n in range(n1,n2 + 1):
    url = "https://xkcd.com/" + str(n) + "/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    links = soup.find_all("div", id = "comic")
    for l in links:
        s = "https:" + l.find_all("img")[0].get("src")
        fn = add + "/" + str(n) + " - "  + soup.find_all("div", id = "ctitle")[0].text + ".temp"
        urlretrieve(s, fn)
