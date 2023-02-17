from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# New York Times

nyt_r = requests.get("https://www.nytimes.com/section/automobiles")
nyt_soup = BeautifulSoup(nyt_r.content, 'lxml')

nyt_headings = nyt_soup.find_all('h2')

nyt_headings = nyt_headings[1:24] # removing footers

nyt_news = []

for nyh in nyt_headings:
    nyt_news.append(nyh.text)


#Car and Driver

cad_r = requests.get("https://www.caranddriver.com/news/")
cad_soup = BeautifulSoup(cad_r.content, 'lxml')
cad_headings = cad_soup.findAll("a", {"class": "custom-item-title item-title"})
cad_news = []

for cadh in cad_headings:
    print(cadh.text)
    cad_news.append(cadh.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':nyt_news ,'ht_news':cad_news })