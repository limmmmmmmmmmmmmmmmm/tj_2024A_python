'''
    user : user 객체의 클래스 정의
    file : save,load 함수를 정의
    [조건1] 이름과 나이를 입력받아 저장
    [조건2] 프로그램 종료되고 다시 실행해도 names 데이터가 유지되도록 파일 처리

'''
from user import User
from file import *

names = [ ]
def nameCreate( ) :
    newName = input('newName : ')
    newAge = input('newAge : ')
    user = User(newName,newAge)
    names.append(user)
    print(names)
    dataSave(names)
    return

def nameRead( ) :
    for a in names :
        print(a)
    return


if __name__ == "__main__" :
    names = dataLoad()
    while True :
        ch = int( input('1.create 2.read') )
        if ch == 1 : nameCreate( )
        elif ch == 2 : nameRead( )