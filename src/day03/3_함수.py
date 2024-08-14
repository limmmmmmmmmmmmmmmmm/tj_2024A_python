# 함수
# 입력값을 가지고 어떤 일을 수행한 후 그 결과물을 내어 놓는 것
# 사용목적 : 1.코드재활용(반복사용) 2.기능별 분리


'''
1. python
def 함수명 (매개변수,매개변수)
    실행문
    return 반환값
2. JS
function 함수명 (매개변수,매개변수)
    실행문
    return 반환값 또는 생략
3. java
반환타입 함수명 (타입 매개변수,타입 매개변수)
    실행문
    return 반환값 또는 생략
'''

# 예1 : 함수 이름은 add이고 입력으로 2(a.b)개의 값을 받으면 리턴값(a+b)은 2개의 입력값을 더한 값이다.
def add(a,b) :
    #{} 가 없으므로 들여쓰기 주의
    return a+b
# 함수호출
add(3,4) # add 함수에 3과4 를 매개변수로 전달하여 7 반환 받는다.
print(add(3,4))

a=3
b=4
result = add(a,b)
print(result)

#(2) 입력값과 리턴값의 따른 함수의 형태
# 1. 매개변수 O 리턴 O
def add(a,b) : # 함수정의
    result = a+b
    return result
a = add(3,4) #함수 호출
print('#1',end="  ")
print(a)

# 2. 매개변수 X 리턴 O
def say() : # 함수정의
    return "Hi"
a = say() #함수 호출
print('#2',end="  ")
print(a)

# 3. 매개변수 O 리턴 X
def add(a,b) : # 함수정의
    print('#3', end="  ")
    print(f"{a},{b} 의 합은 {a+b} 입니다.")
add(3,4) #함수 호출


# 4. 매개변수 X 리턴 X
def say() : # 함수정의
    print('#4', end="  ")
    print('Hi')
say() #함수 호출

#(3) 매개변수를 지정하여 호출 하기
def sub(a,b) :
    print(a,b)
    return a-b

# 함수 호출시 인수의 값을 대입할 매개변수를 지정    return a-b
result = sub(b=3,a=7)
print(result)

#(4) 입력값이 몇 개가 될지 모를때
# 1.
def add_many(*args) :
    print(args) # 여러개의 매개변수 값이 들어있는 리스트
    result = 0 # 더한 값을 저장하기 위한 변수
    for i in args : # 여러개의 매개변수 리스트를 반복ㅊ퍼리
        result +=i # 누적합계
    # for 종료후
    return result

result = add_many(1,2,3); print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10); print(result)

def add_mul(choice,*args) : #함수 정의
    if choice == "add" : # 만약에 매개변수 값이 add 이면
        result = 0
        for i in args :
            result = result + i
    elif choice == "mul": # 아니고 만약에 매개변수 값이 mul 이면
        result = 1
        for i in args :
            print(i)
            print(args)
            result = result * i
    return result

# 함수 호출
result = add_mul("add",1,2,3,4,5)
print(result)

result = add_mul("mul", 1,2,3,4,5)
print(result)



# [5] 키워드 매개변수, kwargs키워드, **
# 1.
def print_kwarg(**kwargs) :
    print(kwargs) # {'a': 1} 딕셔너리 타입으로 매개변수 받는다.
                  # {'name': 'tom', 'age': 3}

print_kwarg(a=1) # 인수로 전달시 키에 값으로 전달
print_kwarg(name="tom",age = 3)

# [6] 함수의 리턴값은 언제나 하나이다. 여러개 일때는 [],(),{} 활용
# 1.
def add_and_mul(a,b) :
    튜플 = 1,2
    print("튜플")
    print(튜플)   # (1, 2)
    return a+b, a*b
#함수호출
result = add_and_mul(3,4)
print(result) #(7, 12), 튜플 1개 (튜플안에 요소2개)


# 2.
def add_and_mul(a,b) :
    return a + b
    # return a + b #위에 리턴이 존재하므로 해당 리턴은 실행되지 않는다.

# 3.  서로 다른 수준의 return 은 여러개 존재 할 수 있다.
def add_and_mul(a,b) :
    if a < 0 :
        return #만약에 a가 b보다 작으면 함수 강제 종료, 아래 코드는 실행되지 않는다.
    return a+b

# [7] 매개변수에 초기값 미리 설정하기
    # 주의할점 : 초기화 하고 싶은 매개변수는 항상 뒤쪽에 배치해야 한다.
def say_myself(name,age,man=True) :
    print(f"나의 이름은 {name} 입니다.")
    print(f"나의 나이는 {age} 입니다.")
    if man :
        print('남자입니다.')
    else:
        print('여자입니다.')
# 함수호출
    # 만약에 해당 매개변수의 인자값이 없으면 디폴트값(초기값)이 대입된다.
say_myself('윤석열',80) #나의 이름은 윤석열 입니다. 나의 나이는 80 입니다. 남자입니다.
say_myself('윤석열',80, False) #나의 이름은 윤석열 입니다. 나의 나이는 80 입니다. 여자입니다.

# [8] 함수안에서 선언한 변수의 효력 범위, 지역변수
    # 함수 안에서 사용하는 매개변수는 함수 밖에 변수 이름과는 전혀 상관없다.
a = 1
def vartest (a) :
    a = a + 1
    print(a) #값 2

vartest(a)
print(a) #값 1

# 함수안에서 함수 밖 변수를 활용하는 방법
# 1. return
a=1
def vartest2 (a) :
    a=a+1
    return a # 지역변수는 함수 종료시 사라지므로 함수를 호출했던 곳으로 반환
a = vartest2(a)
print(a)

#2. global 키워드 : 함수 밖 변수를 함수안으로 호출할때 사용하는 키워드
a=1
def vartest ():
    global a
    a=a+1

vartest()
print(a)


b = 1
def vartest():
    c = b + 1
    return c
b = vartest()
print(b)















