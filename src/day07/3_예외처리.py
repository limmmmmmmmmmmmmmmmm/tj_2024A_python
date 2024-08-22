#예외처리란? 프로그램 도중에 발생하는 오류를 다른 실행문으로 처리해주는 역할

list = [1,2,3]

#list[3] # 존재하지 않는 인덱스 이므로 예외 발생

try:
    #예외가 발생 할것 같은 코드들
    list[3]
except :
    # 만약에 예외가 발생 했을때 실행되는 코드들
    print("존재하지 않는 인덱스 입니다.")

#[2] 예외 처리 방법2
try:
    list[3]
except IndexError : #특정 예외를 처리할때는 예외클래스명 작성한다
    print("존재하지 않는 인덱스 입니다.")

#[3] 예외 처리 방법3
try:
    list[3]
except IndexError as e : #특정 예외가 발생한 사유를 보고 싶을떄 as 예외 변수명 작성한다.
    print(e)

#[4] finally : 예외 발생 여부와 상관없이 무조건 실행되는 구역
try:
    list[3]
except IndexError as e :
    print(e)
finally:
    print('예외 여부와 상관없이 실행')

#[5] 다중 except, 다중 except 중 1번 또는 0번 실행된다.
try:
    # list[3]
    # print(4/0)
    list[2]
    int("a")
except ZeroDivisionError as e:    print(e) #ZeroDivisionError 발생시
except IndexError as e :    print(e)       #IndexError 발생시
except Exception as e :    print(e)        #그외 모든 예외 발생시 # 다중예외는 마지막에

