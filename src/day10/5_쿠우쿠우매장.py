import urllib.request
from email.message import tspecials

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
        for row in tbody.select("tr") :
            tds = row.select("td")
            # print(row.findAll(class_="td-num hidden-md hidden-sm"))
            address = row.findAll(class_="hidden-xs td-width")
            print(address.)

            # print(tds)

            # store_num = row.find("td"); print(store_num)
            # store = [store_num]
            # result.append(store)



if __name__ == '__main__' :
    main()












