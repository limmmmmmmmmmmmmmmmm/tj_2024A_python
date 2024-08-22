from tkinter.font import names

from user import User

#Save
def dataSave(names):  # 데이터를 파일내 저장하기
    # 1. 쓰기 모드 파일 객체
    f = open('user.txt', 'w', encoding='utf-8')
    # 2.
    outstr = ''
    for user in names :
        outstr += f"{user.name},{user.age}\n"
    f.write(outstr)
    f.close()
    return

#Load
def dataLoad():
    try : #예외 처리 #예외가 발생할것 같은 코드
        # 읽기 모드 파일 객체
        f = open('user.txt', 'r', encoding="utf-8")
        # 읽어오기
        names = []
        data = f.read()
        rows = data.split("\n")
        for row in rows :
            if row : #만약에 데이터가 존재하면
                cols = row.split(',')
                user = User( cols[0] , cols[1] )
                names.append(user)
        print(data)
        # 파일 닫기
        f.close()
        return names #리스트 반환
    except FileNotFoundError: #예외처리 # 예외가 발생했을때 실행되는 구역
        return [] # 반환값이 없다.