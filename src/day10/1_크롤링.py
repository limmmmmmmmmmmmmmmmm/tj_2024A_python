from bs4 import BeautifulSoup

html = '''
    <h1 id="title">한빛출판네트워크</h1>
    <div class="top">
        <ul class="menu">
            <li><a href="http://wwww.hanbit.co.kr/member/login.html"class="login">로그인</a>
            </li>
        </ul>
        <ul class="brand">
            <li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li>
            <li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li>
        </ul>
    </div>'''

soup = BeautifulSoup(html,'html.parser')
print(soup)
print(soup.prettify()) #html 문서 형태로 출력해주는 함수

print(soup.h1)
print(soup.div)
print(soup.ul)
print(soup.li)
print(soup.a)

print(soup.findAll("ul"))
print(soup.findAll("li"))
print(soup.findAll("a"))

#.attrs : 지정한 마크업의 속성 목록을 딕셔너리 변형
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>attrs")
print(soup.findAll('a')[0].attrs)
print(soup.findAll('a')[0]["href"])
print(soup.findAll('a')[0]["class"])
print(soup.find(id="title")) # 아이디 title 찾기

li_list = soup.select("div > ul.brand>li")
for li in li_list : 
    print(li.string)
