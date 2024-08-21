# day06 > Task6.py
# 객체/리스트 활용 190p. ~ 207p
# [조건1] : 각 함수 들을 구현 해서 프로그램 완성하기
# [조건2] :  1. 한명의 name , age 를 입력받아 저장 합니다.
#           2. 저장된 객체들을 name , age 을 모두 출력 합니다.
#           3. 수정할 이름을 입력받아 존재하면 새로운 name , age 을 입력받고 수정 합니다.
#           4. 삭제할 이름을 입력받아 존재하면 삭제 합니다.
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능합니다.
# 제출 : git에 commit 후 카톡방에 해당 과제가 있는 링크 제출

names = [ ]
class studentList :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"student(name='{self.name}', age={self.age})"

def nameCreate( ) :
    global names
    newName = input('newName : ')
    newAge = input('newAge : ')
    student = studentList(newName,newAge)
    names.append(student)
    return

def nameRead( ) :
    global names
    print(names)
    return

def nameUpdate(  ) :
    global names
    oldName = input('oldName : ')
    for student in names :
        if student.name == oldName :
            newName = input('newName : ')
            newAge = input('newAge : ')
            student.name = newName
            student.age = newAge
            print(student)
        else: print("잘못입력했습니다")

    return

def nameDelete( ) :
    global names
    deleteName = input('deleteName : ')
    for student in names:
        if student.name == deleteName:
            names.remove(student)
        else: print("잘못입력했습니다")
    return

while True :
    ch = int( input('1.create 2.read 3.update 4.delete : ') )
    if ch == 1 : nameCreate( )
    elif ch == 2 : nameRead( )
    elif ch == 3 : nameUpdate( )
    elif ch == 4 : nameDelete( )
    else: break

