from http.client import responses

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


def hollys_store(result) :
    for page in range(1,51) :
        # 할리스 매장 정보 url
        url=f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}";
        response = urllib.request.urlopen(url)
        htmlData = response.read()
        soup = BeautifulSoup(htmlData,"html.parser")
        #print(soup)
        tbody = soup.select_one("tbody")
        # print(tbody)
        for row in tbody.select("tr") :
            # print(row)
            tds = row.select("td")
            store_sido = tds[0].string; #print(store_sido)
            store_name = tds[1].string; #print(store_name)
            store_address = tds[3].string; #print(store_address)
            store_phone = tds[5].string; #print(store_phone)
            store = [store_name,store_sido,store_address,store_phone]
            result.append(store) #리스트 안에 리스트 요소 추가 ,  2차원 리스트 # [ [],  [],  [], [] ]
    print(result)


def main() :
    result = []  # 할리스 매장 정보 리스트를 여러개 저장하는 리스트 변수, 2차원 리스트
    print(">>>>>>>>>>>>>>> 할리스 매장 크롤링중 >>>>>>>>>>>>>>>>>>>")
    hollys_store(result)
    # py 리스트 객체를 DataFrame 객체로 변환
    tb1 = pd.DataFrame(result,columns=('store', 'sido-gu', 'address', 'phone'))
    # DataFrame 객체를 csv 객체로 생성
    tb1.to_csv('hollys.csv',encoding="cp949",mode="w",index=False)

if __name__ == '__main__' :
    main()


