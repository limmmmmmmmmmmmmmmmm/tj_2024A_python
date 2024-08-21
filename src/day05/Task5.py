# day06 > Task5.py
# 딕셔너리/리스트 활용 , 파일처리 , p.175 ~ p.182
# [조건1] : 각 함수 들을 구현 해서 프로그램 완성하기
# [조건2] :  1. 한명의 name , age 를 입력받아 저장 합니다.
#           2. 저장된 여러명의 name , age 을 모두 출력 합니다.
#           3. 수정할 이름을 입력받아 존재하면 새로운 name , age 을 입력받고 수정 합니다.
#           4. 삭제할 이름을 입력받아 존재하면 삭제 합니다.
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능합니다.
# [조건4] : 프로그램이 종료되고 다시 실행되더라도 기존의 names 데이터가 유지 되도록 파일처리 하시오.
#           - dataLoad() , dataSave() 함수를 정의하여 적절한 위치 에서 호출 하시오.
# 제출 : git에 commit 후 카톡방에 해당 과제가 있는 링크 제출

names = [ ] # 샘플 데이터
def dataLoad( ) : # 파일내 데이터를 불러오기
    global names
    f = open('names.txt', 'r',encoding="utf-8" )
    var = f.read()
    # 딕셔너리 만들고 리스트에 담기
    lines = var.split('\n')
    for line in lines [ : len(lines)-1 ]:
        dic = {'name': line.split(',')[0], 'age': line.split(',')[1]}
        print(dic)
        names.append(dic)
    f.close()
    return

def dataSave() :  # 데이터를 파일내 저장하기
    global names
    f = open('names.txt', 'w', encoding='utf-8')
    outstr = ""  # 파일에 작성할 문자열 변수
    for dic in names:
        outstr += f'{dic['name']},{dic['age']}\n'  # 딕셔너리를 CSV 형식의 문자열로 변환 # ,(쉼표) 필드 구분 # \n(줄바꿈) 객체/딕셔너리 구분
    f.write(outstr)  # 파일객체 이용한 데이터 쓰기 # 파일객체.write( 데이터 )
    f.close()
    return

def nameCreate( ) :
    global names
    newName = input('newName : ')
    newAge = input('newAge : ')
    dic = { 'name' : newName,'age' : newAge}  # 딕셔너리 구성
    names.append( dic ) # 딕셔너리를 리스트에 삽입
    print(names)
    dataSave()
    return

def nameRead( ) :
    global names
    for a in names:
        print(a)
    return

def nameUpdate(  ) :
    global names
    oldName = input('oldName : ')
    for dic in names :
        if dic['name'] == oldName :
            newName = input('newName : ')
            newAge = input('newAge : ')
            dic['name'] = newName # 해당 딕셔너리의 속성 값 수정 하기.
            dic['age'] = newAge # 해당 딕셔너리의 속성 값 수정 하기.
            dataSave()
        else: print("잘못입력했습니다"); continue
    return
def nameDelete( ) :
    global names
    deleteName = input('deleteName : ')
    for dic in names :
        if dic['name'] == deleteName :
            names.remove(dic)
            print("삭제성공")
            dataSave()
        else: print("잘못입력했습니다"); continue
    return

dataLoad()
while True :
    ch = int( input('1.create 2.read 3.update 4.delete : ') )
    if ch == 1 : nameCreate( )
    elif ch == 2 : nameRead( )
    elif ch == 3 : nameUpdate( )
    elif ch == 4 : nameDelete( )
    else: break

