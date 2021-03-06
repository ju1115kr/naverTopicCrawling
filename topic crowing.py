# -*- coding:utf-8 -*-

import lxml
import requests
from bs4 import BeautifulSoup as bs

#response = requests.get('http://125.209.234.143/keyword/realtimeList.naver?where=main')
response = requests.get('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
#response.encoding = 'cp949'
response.encoding = 'utf-8'

dom = bs(response.text, 'html.parser')
result = dom.find_all('ul')

rank_inner = dom.find_all('div', {'class':'rank_inner v2'})
date = rank_inner[0].strong.contents[0]
time=rank_inner[0].strong.contents[1].contents[0]

print()
print(date, time)
print()

for res in result:
	if res['class'][0] == 'rank_list':
		numbers = 1
		keywords = res.find_all('span')
		for key in keywords:
			print(numbers, key.contents[0])
			if numbers==1: first=key.contents[0]
			numbers = numbers+1
		break

#print(first)
##########################################

#news_url = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&ie=utf8&query='+first)
#news_dom = bs(news_url.text, 'html.parser')
#print(news_dom)
