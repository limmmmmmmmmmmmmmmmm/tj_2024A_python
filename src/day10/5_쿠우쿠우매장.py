import urllib.request

import pandas as pd
from bs4 import BeautifulSoup

def main() :
    result = []  # 할리스 매장 정보 리스트를 여러개 저장하는 리스트 변수, 2차원 리스트
    print(">>>>>>>>>>>>>>> 쿠우쿠우 매장 크롤링중 >>>>>>>>>>>>>>>>>>>")
    qooqoo_store(result)

def qooqoo_store(result) :
    for page in  range(1,7) :
        url = f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
        response = urllib.request.urlopen(url)
        htmlData = response.read()
        soup = BeautifulSoup(htmlData,"html.parser")
        # print(soup)
        tbody = soup.select_one("tbody")
        rows= tbody.select("tr")
        for row in rows :
            cols = row.select("td")
            if len(cols) <=1 : #PC랑 모바일 1개씩인데 모바일은 td가 한개임 # 모바일 제거 함수
                continue #제일 가까운 반복문으로
            #print(cols)
            번호 = cols[0].string.strip(); #print(번호) #td 첫번째 값
            #& nbsp; = 띄어쓰기
            매장이름 = cols[1].select("a")[1].string.strip(); #print(매장) # 매장이름 tr안에 a태그가 2개 # a태그 두번째거 가져오기 위해 select("a")[1] 사용
            연락처 = cols[2].select("a")[0].string.strip(); #print(번호) # a태그 첫번째거 가져오기 위해 select("a")[0] 사용
            주소 = cols[3].select("a")[0].string.strip(); #print(주소) # a태그 첫번째거 가져오기 위해 select("a")[0] 사용
            시간 = cols[4].select("a")[0].string.strip(); #print(시간) # a태그 첫번째거 가져오기 위해 select("a")[0] 사용
            매장 = [번호,매장이름,연락처,주소,시간]
            result.append(매장)
    print(result)



if __name__ == '__main__' :
    main()












