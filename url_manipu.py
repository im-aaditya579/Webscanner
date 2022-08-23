import json
import requests
from bs4 import BeautifulSoup


try:
    def geturlmanip(url):
        links = []
        urlf = "http://www." + url
        website = requests.get(urlf)
        website_text = website.text
        soup = BeautifulSoup(website_text)

        for link in soup.find_all('a'):
            links.append(link.get('href'))

        links.append(len(links))
        res = json.dumps(links)
        return res
except:
    print("ERROR IN URL MANIPULATION")

#print(geturlmanip("google.com"))
