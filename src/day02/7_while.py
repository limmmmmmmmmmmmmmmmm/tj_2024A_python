

coffee = 3
while True :  # 파이썬은 쌍점으로
    money = int(input("돈을 입력하세요"))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee -1 # 파이썬은 증감연산자 없어서 이런식으로 표현
    elif money > 300 :
        print("거스름돈 %d를 주고 커피를 줍니다 " %(money-300)) #같은데 다른버전
        print(f"거스름돈 {money-300}를 주고 커피를 줍니다") #같은데 다른버전
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다.")
    if coffee == 0 :
        print("커피가 다 떨어졌습니다")
        break