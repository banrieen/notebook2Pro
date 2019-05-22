import requests
from bs4 import BeautifulSoup

target = 'https://cuiqingcai.com/5484.html'
req = requests.get(url=target)
print(req.text)
txt = req.text

bf = BeautifulSoup(txt)
texts = bf.find_all('article', class_ = 'article-content')
print(texts)