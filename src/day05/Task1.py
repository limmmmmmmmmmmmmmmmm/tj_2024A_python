# 문자열 활용, p.50 ~ p.76
# 조건1 : 각 함수들의 구현해서 프로그램 완성
# 조건2 :
# 1.이름을 입력받아 여러명의 이름을 저장
# 2.저장된 여러명의 이름을 모두 출력
# 3. 수정할 이름이 존재하면 새로운 이름을 입력받아 수정
# 4. 삭제할 이름을 입력받아 존재하면 삭제
# 조건3 : names 변수 외 추가적인 전역변수 생성 불가능

names = "" #여러개의 name들을 저장하는 문자열

def nameCreate() :
    global names
    name = input("등록할 이름을 입력해주세요 : ")
    if names != "":
        names += ","
    names += name
    print(f"등록된 이름>>>>>>>>>>>>>>\n{name} 입니다.")
    return

def nameRead() :
    print(f"등록된 이름\n{names}")
    return

def nameUpdate() :
    global names
    print(names)
    name1 = input("수정할 이름을 입력해주세요")
    if name1 in names :
        name2 = input("변경하고 싶은 이름을 입력해주세요")
        names = names.replace(name1,name2)
    else: print("다시 입력해주세요")
    print(names)
    return

def nameDelete() :
    global names
    name = input("삭제할 이름을 입력해주세요.")
    names=names.strip(name)
    print(names)
    return

while True : #무한루프
    ch = int(input("1.create 2.read 3.update 4.delete : "))
    if ch == 1 :
        print("1번입니다")
        nameCreate()
    elif ch == 2 :
        print("2번입니다")
        nameRead()
    elif ch == 3 :
        print("3번입니다")
        nameUpdate()
    elif ch == 4 :
        print("4번입니다")
        nameDelete()
    else: break
