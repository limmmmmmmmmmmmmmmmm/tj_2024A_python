# - 테이블형태 다를수 있는 라이브러리
# 1차원 구조

import pandas as pd



print(pd.__version__)
print(type(pd))

#[1] Series : 1차원 자료구조 객체, 인덱스 0부터 시작
data1 = [10,20,30,40,50]
sr1 = pd.Series(data1); print(sr1)

data2 = ["1반","2반","3반","4반","5반"]
sr2 = pd.Series(data2); print(sr2)

sr4 = pd.Series(["월","화","수","목","금"]); print(sr4)

#[4] index 속성
sr5 = pd.Series(data1,index=[1000,1001,1002,1003,1004]); print(sr5)
sr6 = pd.Series(data1,index=data2); print(sr6)
sr8 = pd.Series(data1,index=sr4); print(sr8)

print(sr8.iloc[2])
print(sr8["목"])

# 슬라이싱
print(sr8[0:4])

# 인덱스 확인 / 데이터 확인
print(sr8.index)
print(sr8.values)

# 덧셈 연결
print(sr1+sr5) #숫자타입 덧셈
print(sr4+sr8) #문자타입 연결

#DataFrame
data_dic= {
    "year" : [2018,2015,2023], "sales" : [350,400,1099]
}
df1 = pd.DataFrame(data_dic); print(df1)
data_list = [ [89.2,92.5,96.8], [92.8,89.9,95.2] ]
df2 = pd.DataFrame(data_list, index=("중간고사","기말고사"), columns=data2[0:3]); print(df2)

data_list = [['20201101', 'Hong', '90', '95'], ['20201102', 'kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_list); print(df3)
df3.columns = ["학번","이름","중간고사","기말고사"]
print(df3.head(2)) # 위에서 2개 조회
print(df3.tail(2)) # 아래에서 2개 조회
print(df3["이름"])

df3.to_csv("score.csv", header="False") #df3 객체를 csv로 내보내기
# index_col=0 첫번째 열을 DataFrame의 인덱스로 사용하겠다는 뜻
df4 = pd.read_csv("score.csv",encoding="utf-8", index_col=0)
print(df4)

