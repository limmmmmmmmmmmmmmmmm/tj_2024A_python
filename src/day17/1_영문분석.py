from audioop import reverse

import pandas as pd
import  glob
import  re
from functools import reduce
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.stem import WordNetLemmatizer
from  collections import Counter
import matplotlib.pyplot as plt
from statsmodels.iolib.summary import summary
from wordcloud import STOPWORDS, wordcloud, WordCloud

# import nltk
# nltk.download()

#[1] 여러개의 파일명 불러오기
all_files = glob.glob("myCabinetExcelData*.xls")
# print(all_files)

all_files_data = []
for file in all_files : #반복문 사용으로 하나씩 순환
    # print(file)
    data_frame = pd.read_excel(file) #엑셀 모듈
    # print(data_frame)
    all_files_data.append(data_frame)

# print(all_files_data)

# [3] 데이터프레임 합치기 #concat(여러개 프레임이 저장된 리스트 , axis = 0 세로방향 1 가로방향,)
all_files_data_concat = pd.concat(all_files_data, axis=0, ignore_index=True)
# print(all_files_data_concat)

# [4]
all_files_data_concat.to_csv("riss_bigdata.csv", encoding="utf-8", index=False)

# - (프로젝트목표 : 학술문서의 제목 분석) 데이터 전처리
# [5] 데이터프레임의 제목(열)만 추출
all_title = all_files_data_concat['제목']
# print(all_title)

#[6] 단어 토큰화 준비
    #stopwords.words() : 영어 불용어 목록 가져 오는 함수
    #WordNetLemmatizer() : 표제어 추출기 객체 생성
        #표제어 : 단어의 원형(기본형) 찾는 과정 runing -> run
영어불용어목록 = stopwords.words('english')
# print(영어불용어목록)
표제어객체 = WordNetLemmatizer()

#[7] 단어 토큰화
words = []
for title in all_title :
    # print(title)
    # 7-1 영문이 아닌것을 정규표현식을 이용해서 치환
    Enwords = re.sub(r'[^a-zA-Z]+'," ",title)
    # print(Enwords)

    #7-2 소문자로 변환 하고 토큰화 # 지정한 문자열을 토큰(단어) 추출 하여 리스트로 반환
    EnWordsToken = word_tokenize(Enwords.lower())
    # print(EnWordsToken)

    #7-3 불용어 제거 (해당 토큰 리스트에 불용어가 포함되어 있으면 제외)
        # 리스트 컴프리헨션 사용 X
    # EnWordsTokenStop = []
    # for w in EnWordsToken :
    #     if w not in 영어불용어목록 : # 해당 토큰(단어)가 불용어목록에 포함 아니면
    #         EnWordsToken.append(w)

        # 리스트 컴프리헨션 사용 O
    EnWordsTokenStop = [w for w in EnWordsToken if w not in 영어불용어목록]
        # if 값 in 리스트 : 리스트내 해당 값이 존재하면 true
        # if 값 not in 리스트 : 리스트내 해당 값이 존재하지 않으면 true

    #7-4 표제어 추출 lemmatize(단어) #단어에서 시제, 단/복수, 진행형 들을 일반화 단어로 추출
    EnWordsTokenStopLemma = []
    # EnWordsTokenStopLemma = [표제어객체.lemmatize(w) for w in EnWordsTokenStop ] # 불용어 제거된 리스트에서 표제어 추출
    for w in EnWordsTokenStop :
        EnWordsTokenStopLemma.append(표제어객체.lemmatize(w))

    words.append(EnWordsTokenStopLemma) #정규화 -> 토큰화 -> 불용어제거 -> 표제어추출한 결과를 리스트에 담기

print(words)
# [8] 2차원 리스트를 1차원 변환
    # reduce 사용 O # reduce(람다식함수, 2차원리스트)
words2 = reduce(lambda  x,y : x+y, words)
# print(words2)

# reduce 사용 x
# words2 = []
# for w in words :
#     words2.extend(w) #.extend() 두 리스트를 하나의 리스트로 반환 함수
# print(words2)

# [9] 리스트내 요소 개수  세기(단어 빈호 구하기)
count = Counter(words2)
# print(count) #Counter ({단어:수},{단어:수},{단어:수})

#[10] 빈도가 높은것만 추출
# print(count.most_common(50)) # [('단어':수),('단어':수),('단어':수)]
word_count = dict()
for tag, counts in count.most_common(50) :
    # print(tag)
    # print(counts)
    if(len(tag)>1) : # 단어길이가 1초과이면
        word_count[tag] = counts
# print(word_count)

'''
    파이썬의 반복문과 리스트/튜플 
        1. for element in list/tuple :
        2. for a1, a2 in tuple :
'''

# sorted_keys =sorted(word_count, key= word_count.get , reverse=True)
# sorted_Values = sorted(word_count.values(), reverse=True)
# plt.bar(range(len(word_count)),sorted_Values,align='center')
# plt.xticks(range(len(word_count)),list(sorted_keys),rotation='85')

#[11] 히스토그램
#plt.bar (x축값, y축값)
#plt.bar[(1,2,3),(4,5,6)]
    # 딕셔너리.keys() : 딕셔너리내 모든 key값 호출 반환  딕셔너리.values() : 딕셔너리내 모든 values 호출 반환
plt.bar(word_count.keys(),word_count.values())
    # x축에 단어 key     y축에 단어 value

# 딕셔너리 정렬 방법 # sorted (딕셔너리 , key=정렬기준)
sorted_keys = sorted(word_count,key=word_count.get , reverse=True)
    # key=word_count.get는 get 메소드를 참조하여 각 키를 value(빈도수) 기준으로 정렬
    # reverse = True 는 내림차순 , 생략시 오름차순
sorted_Values = sorted(word_count.values(),reverse=True)
# print(sorted_keys)

'''
print(range(len(word_count))) #range(0, 50)
plt.bar (range(len(word_count)),  sorted_Values)
plt.xticks(range(len(word_count)), list(sorted_keys))
'''
plt.show()




all_files_data_concat['doc_count'] = 0
summary_year = all_files_data_concat.groupby('출판일',as_index=False)['doc_count'].count()


plt.figure(figsize=(12,5))
plt.xlabel("year")
plt.ylabel("doc=count")
plt.grid(True)
plt.plot(range(len(summary_year)),summary_year['doc_count'])
plt.xticks(range(len(summary_year)),[text for text in summary_year['출판일']])
# plt.show()

stopwords = set(STOPWORDS)
wc = WordCloud(background_color="ivory", stopwords=stopwords, width=800,height=600)
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis('off')
# plt.show()








#