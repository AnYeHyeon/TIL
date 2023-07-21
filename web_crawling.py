# 기사 웹 크롤링하기

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://news.naver.com/")

bsObject = BeautifulSoup(html, "html.parser")

for link in bsObject.fineall('a'):
    print(link.text.strip(), link.get('href'))