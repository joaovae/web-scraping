# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:29:31 2020

@author: JOAO VICTOR
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.anp.gov.br/dados-estatisticos'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

teste = []
teste2 = []

for i in soup.find_all('ul', class_ = 'interna-faq'):
   for x in i.find_all('a', href=True):
       teste.append(x['href'])
       teste2.append(x.text)

print(teste)
print(teste2)

print(teste[0])

def get_file_anp(link):
    url2 = 'http://www.anp.gov.br{}'.format(link)
    file = requests.get(url2)
    with open(link.split('/')[-1], 'wb') as code:
        code.write(file.content)

get_file_anp(teste[0])
