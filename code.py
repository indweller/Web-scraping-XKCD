import requests
import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

print("Intial index from the range you wish to download: ")
n1 = int(input())
print("Final index from the range you wish to download: ")
n2 = int(input())
print("Enter the location where you wish to save the comics.")
add = input() 
print("Downloading...")
for n in range(n1,n2 + 1):
    print(n)
    url = "https://xkcd.com/" + str(n) + "/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all("div", id = "comic")
    for l in links:
        s = "https:" + l.find_all("img")[0].get("src")
        fn = add + "/" + str(n) + " - "  + soup.find_all("div", id = "ctitle")[0].text + ".temp"
        urlretrieve(s, fn)
print("Finished.")