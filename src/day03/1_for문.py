# 1_for문.py
# while 문과 비슷한 반복문
# for문은 한눈에 들어온다는 장점

# for문의 기본 구조

test_list = ['one','two','three'] # 배열 선언은 자바랑 비슷한듯 let이 없네

for i in test_list: # 클론 다음의 실해문 작성시 들여쓰기 주의 , {} 없다.
    print(i)

'''
(JS방식)
let test_list = ['one','two','three']
test_list.forEach(i =>{
    console.log(i)
})
'''

'''
for mark in marks:
    print(mark) #90,25,67,45,80
'''

a = [(1,2),(3,4),(5,6)]
for(first,last) in a :
    print(f'{first}+{last}는 {first+last}입니다.')

# [1,2,3] : 리스트 타입 (수정/삭제 가능)
# (1,2,3) : 튜플 타입 (수정/삭제 불가능) - 고정형

#예제 3
marks = [90,25,67,45,80]

number = 0 # 학생번호
for mark in marks:
    number = number + 1
    if mark >= 60 :
        #들여쓰기 주의
        print(f"{number}번 학생은 합겹입니다")
    else:
        print(f"{number}번 학생은 불합겹입니다")
    # if 조건문에 ()가 없다.


#continue : 가장 가까운 for문의 처음으로 돌아가게 되는 키워드
number = 0 # 학생번호
for mark in marks:
    number = number + 1
    if mark < 60 :
        continue #continue 를 만나게 되면 아래 코드는 실행되지 않는다.
    print(f"{number}번 학생 축하합니다. 합격입니다")

# range() : 숫자 리스트를 생성하여 반환 해주는 함수
    # range(숫자) : 0부터 숫자 미만까지 포함하는 range 객체를 만들어준다
    # range(사작숫자,끝숫자) : 시작숫자 부터 끝 숫자 미만까지 포함하는 range 객체 만들어준다
    # range(사작숫자,끝숫자,증감식) : 증감단위 만큼 증감하여 객체 만들어준다.
a = range(10)
print(a)
a = range(1,11)
print(a)

# 예제
for value in range(10):
    print(value,end=' ') #print( end='') 줄바꿈처리 안하고 같은 줄에 출력해줌
print()
for value in range(1,11):
    print(value,end=' ')
print()
for value in range(1,11,3):
    print(value,end=' ')

print()
sum = 0
for i in range(1,101):
    #print(i)
    sum = sum + i
print(sum)

for i in range(2,10) :
    for j in range(1,10) :
        print(f"{i} x {j} = {i*j}")


#(4) 리스트 컴프리헨션 사용
    # [표현식/연산식 for 반복변수 in 리스트 if 조건문]

# 1
a = [1,2,3,4]
result = [num*3 for num in a]
# [] 안에서 for문을 사용한다.
# [for 반복변수  in 리스트명]
print(result)

# 2
result = [i for i in a]
# 반복되고 있는 i값을 하나씩 리스트 요소로 대입하여 리스트 생성 한다.
print(result)

# 3 기존 리스트를 반복문을 활용하여 새로운 리스트 생성
print([i for i in a]) # java/js : 리스트명.map()
# 4
result = [num*3 for num in a if num % 2 ==0]
print(result)

result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)