from bs4 import BeautifulSoup
import pandas as pd 
import requests

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}


url = "https://site.com.br"
    
r = requests.get(url, headers=header)

r.content
soup = BeautifulSoup(r.content,'html.parser')
resultado = soup.find('div', class_='recently-updated recently-updated-concise conf-macro output-block').get_text()
tag = resultado.split('\n')
for texto in tag:
    if len(texto)>0:
        print(texto)
    