from http.client import responses
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

import urllib

url = "http://quotes.toscrape.com"
response = urllib.request.urlopen(url)
htmlData = response.read()
print(htmlData)
soup = BeautifulSoup(htmlData,"html.parser")
print(soup.prettify())

li_list = soup.select("div.tags > a.tag")
for li in li_list :
    print(li)

li2_list = soup.select("span > small.author")
for li in li2_list :
    print(li)

quoteDivs = soup.select(".quote")
print(quoteDivs)
for quote in  quoteDivs :
    print(quote.select_one(".text").string)
    print(quote.select_one(".author").string)

# https://v.daum.net/v/20240827074833139 크롤링 하기
url = "https://v.daum.net/v/20240827074833139"
response = urllib.request.urlopen(url)
htmlData = response.read()
soup = BeautifulSoup(htmlData,"html.parser")
# print(soup)

# 파싱하기
ps = soup.select("p")
# print(ps)
for p in ps :
    #본문 제목
    print(p.text)

print(soup.select_one(".tit_view").string)
print(soup.select_one(".tit_view").text)

url = "https://search.naver.com/search.naver?query="+urllib.parse.quote("부평구날씨") # URL에 한글이 있을경우
response = urllib.request.urlopen(url)
htmlData = response.read()
soup = BeautifulSoup(htmlData,"html.parser")
print(soup)
print(soup.select_one(".temperature_text"))
print(soup.select_one(".temperature_text").text)
print( soup.select_one('.summary_list').select('.sort')[1].text )


