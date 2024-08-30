from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import json

from numpy.ma.core import default_fill_value


# [1] 쿠우쿠우 매장 정보 크롤링 서비스
def qooqoo_store(result) :
    for page in  range(1,7) :
        url = f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
        response = urllib.request.urlopen(url)
        htmlData = response.read()
        if response.getcode() == 200 :
            print(">>통신 성공")
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
        else: print(">>>통신 실패")
    return result

# [2] 2차원 리스트를 CSV 변환해주는 서비스, 데이터, csv파일명, 열(제목) 목록
def list2d_to_csv (result,fileName,colsNames) :
    try:
        # 1. import pandas as pd 모듈 호출한다
        # 2. 데이터 프레임 객체 생성, 데이터, 열 목록
        df = pd.DataFrame(result,columns=colsNames)
        # 3. 데이터프레임 객체를 csv 파일로 생성하기
        df.to_csv(f"{fileName}.csv", encoding="utf-8", mode="w")

        return True
    except Exception as e :
        print(e)
        return False

#[3] csv 파일을 JSON 형식의 PY타입으로 가져오기, 가져올 파일명
def read_csv_to_json(fileName) :
    # 1. 판다스를 이용한 csv를 데이터프레임으로 가져오기
    df = pd.read_csv(f"{fileName}.csv" , encoding="utf-8", engine="python", index_col=0)
        # index_col=0 : 판다스의 데이터프레임워크 형식 유지 ( 테이블형식 )
    # 2. 데이터프레임 객체를 JSON 으로 가져오기
    jsonResult = df.to_json(orient='records', force_ascii=False)
    # to_json() : 데이터프레임 객체내 데이터를 JSON 변환함수
    # orient='records' : 각 행마다 하나의 JSON 객체로 구성
    # force_ascii=False : 아스키 문자 사용 여부 : True(아스키) , False(유니코드 utf-8)
# 3. JSON 형식(문자열타입) 의 py타입(객체타입-리스트/딕셔너리)으로 변환
    result = json.loads( jsonResult ) # import json 모듈 호출 # json.loads() 문자열타입(json형식) ---> py타입(json형식) 변환
    return result


#서비스 테스트 확인 구역
# if __name__ == "__main__" :
#     result = []
#     qooqoo_store(result); print(result) #쿠우쿠우 매장정보 크롤링 서비스 호출
#     list2d_to_csv(result,'전국쿠우쿠우매장',['번호','매장이름','연락처','주소','시간','매장'])
