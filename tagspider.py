from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import json

pstart, pend = 0, 10
url = "http://g.e-hentai.org/?page="

for i in reversed(range(pstart, pend)):  # reverse to avoid duplicate albums
    mainsoup = BeautifulSoup(urllib.request.urlopen(url + str(i), timeout=4.0).read(),
                             'html.parser')
    print("Page: " + str(i))

    albums = []
    for tgs in mainsoup.find_all("div", {"class": "it5"}):
        albums.append(tgs.a.get("href"))

    tags = set()  # set
    for album in albums:
        alsoup = BeautifulSoup(urllib.request.urlopen(album).read(), 'html.parser')
        print("Album: " + alsoup.title.string)
        for tag in alsoup.find_all("div", {"class": ["gt", "gtl"]}):
            if "male" in tag.get("id"):
                tags.add(tag.string)

print("\n" + str(tags))

outfile = open(datetime.now().strftime("%Y_%m_%d_%H_%M_%S.txt"), 'w')
outfile.write(json.dumps(list(tags)))
outfile.close()
