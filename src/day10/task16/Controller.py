# [1] 플라스크 객체 가져오기
from AppStart import app
# [2] (우리가 만든) 서비스 모듈 가져오기
import Service

# 4. app.run 코드 위에 HTTP 매핑 주소 정의
@app.route( '/jobkorea' , methods = ['get'] ) # http://localhost:5000/qooqoo
def getkorea( ) :
    # (1) 만약에 크롤링 된 CSV 파일이 없거나 최신화 하고 싶을때
    result = []
    Service.잡코리아자바( result )
    Service.to_csv( result,
                  '잡코리아자바검색',
                  ["이름","설명","경력","학력","계약유형","지역","채용기간"])

    # (2) CSV 에 저장된 JSON 으로 가져오기
    result2 = Service.to_json("잡코리아자바검색")

    # (3) 서비스로 부터 받은 데이터로 HTTP 응답하기
    return result2


