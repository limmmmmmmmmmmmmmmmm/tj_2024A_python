import urllib.request
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import json

def 잡코리아자바(result) :
    for page in range(1,2) :
        url = f"https://www.jobkorea.co.kr/Search/?stext=java&tabType=recruit&Page_No={page}"
        response = urllib.request.urlopen(url)
        htmlData = response.read()
        if response.getcode() == 200 :
            print("통신 성공")
            soup = BeautifulSoup(htmlData, "html.parser")
            #print(soup)
            list = soup.select_one(".list")
            # print(list)
            listitems = list.select(".list-item")
            for row in listitems :
                이름 = row.select_one('.list-section-corp > a ').string.strip();
                설명 = row.select_one(".information-title > a").text.strip();
                경력 = row.select_one(".chip-information-group").select("li")[0].string.strip();
                학력 = row.select_one(".chip-information-group").select("li")[1].string.strip(); #print(이름)
                계약유형 = row.select_one(".chip-information-group").select("li")[2].string.strip(); #print(이름)
                지역 = row.select_one(".chip-information-group").select("li")[3].string.strip();
                채용 = row.select_one(".chip-information-group").select("li")[4].string.strip();
                일자리정보 = [이름,설명,경력,학력,계약유형,지역,채용]
                # print(일자리정보)
                result.append(일자리정보)
    # print(result)
    return result

# csv로 변환해주는 목록
def to_csv(result,fileName,colsNames) :
    try:
        df = pd.DataFrame(result,columns=colsNames)
        df.to_csv(f"{fileName}.csv" , encoding="utf-8", mode="w")
        return True
    except Exception as e :
        print(e)
        return False

# JSON 형식으로
def to_json (fileName) :
    df = pd.read_csv(f"{fileName}.csv", encoding="utf-8", engine="python", index_col=0)
    # index_col=0 : 판다스의 데이터프레임워크 형식 유지 ( 테이블형식 )
    # 2. 데이터프레임 객체를 JSON 으로 가져오기
    jsonResult = df.to_json(orient='records', force_ascii=False)
    result = json.loads( jsonResult ) # import json 모듈 호출 # json.loads() 문자열타입(json형식) ---> py타입(json형식) 변환
    return result

#
# if __name__ == "__main__" :
#     result = []
#     잡코리아자바(result); #print(result)
#     to_csv(result,"잡코리아자바검색",["이름","설명","경력","학력","계약유형","지역","채용기간"])