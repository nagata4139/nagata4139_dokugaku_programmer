# P239

#<!--This is a comment in HTML.
#save this file as index.html-->
#<!-- http://tinyurl.com/h3bjuov -->

#<html lang="en">
#<head>
#   <meta charset="UTF-8">
#   <title>My Website</title>
#</head>
#<body>
#    Hello, World!
#    <a href="https://google.com">here</a>
#</body>
#</html>

# P240
# http://tinyurl.com/z4fzfzf

#$ sudo pip3 install beautifulsoup4==4.6.0

# P241
#> pip install beautifulsoup4==4.6.0

# http://tinyurl.com/jmgyar8

import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self,site):
        self.site = site

    def scrape(self):
        pass

# http://tinyurl.com/h5eywoa

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()

# P242
# http://tinyurl.com/hvjulxh

    def scrape(self):
        r = urllib.request.urlopens(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

# P243
# http://tinyurl.com/j55s7hm

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site = site

    def scrape(self):
        r = urllib.request\
            .urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()