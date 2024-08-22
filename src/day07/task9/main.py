'''
    csv파일 다루기
    파일 : 인천광역시_부평구_인구현황.csv
    [조건1] 부평구의 동 마다 Region 객체 생성 해서 리스트 담기
    [조건2]
        Region 객체 변수 :
            1.동이름 2.총인구수 3.남인구수 4.여인구수 5.세대수
        Region 함수
            1. 남자 비율 계산 함수
            2. 여자 비율 계산 함수
    [조건3] 모든 객체의 정보를 f포메팅 해서 console 창에 출력하시오.
    [조건4] 출력시 동 마다 남 여 비율 계산해서 백분율로 출력하시오.
    [출력예시]
        부평1동       35141,  16835,  18306,  16861   59%     41%
        부평2동       14702,  7289,   7413,   7312    51%     49%
        ~~~~~~
'''

from tokenize import detect_encoding
from region import Region

BuPyeong = []
def dataLoad():
    global BuPyeong
    try : #예외 처리 #예외가 발생할것 같은 코드
        # 읽기 모드 파일 객체
        f = open('인구현황.txt', 'r')
        # 읽어오기
        data = f.read()
        rows = data.split("\n")
        for row in rows :
            if row : #만약에 데이터가 존재하면
                cols = row.split(',')
                region = Region( cols[0] , cols[1], cols[2], cols[3], cols[4] )
                BuPyeong.append(region)
        print(data)
        # 파일 닫기
        f.close()
        return BuPyeong #리스트 반환
    except FileNotFoundError: #예외처리 # 예외가 발생했을때 실행되는 구역
        return [] # 반환값이 없다.

if __name__ == "__main__" :
    print("start")
    dataLoad()
    for r in BuPyeong :
            if r.Mperson != 0:  # Mperson
                a = r.Mperson / r.Tperson *100
                print(f"남자 비율 {round(a)}%")
    for r in BuPyeong :
            if r.Fperson != 0:  # Fperson
                a = r.Fperson / r.Tperson *100
                print(f"여자 비율 {round(a)}%")

