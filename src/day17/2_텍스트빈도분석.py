from nltk.corpus import words

#1. 분석할 텍스트 준비
textData = """
Big data refers to the large volume of data – both structured and unstructured – that inundates a business on a day-to-day basis. 
But it’s not the amount of data that’s important. It’s what organizations do with the data that matters. 
Big data can be analyzed for insights that lead to better decisions and strategic business moves.
"""

#2. 다양한 전처리
    # (1) 정규형 : 모든 영대소문자를 소문자로 변환
textData = textData.upper()
print(textData)
# "문자열".upper() : 대문자로 변환 함수

textData = textData.lower()
print(textData)
# "문자열".lower() : 소문자로 변환 함수
    # (2) 정규형 :
import re
textData = re.sub(r'[^\w\s]',"",textData)
    # \w : 문자 혹은 숫자
print(textData)
words = textData.split(" ") # 띄어쓰기 기준으로 문자 구현
print(words)

# 3. 문자 개수 세기
from collections import  Counter
wordCount = Counter(words)
print(wordCount)

#4. 빈도수가 높은 상위 n개 만큼 출력
print(wordCount.most_common(1))

#5. 시각화 : 워드클라우드
from wordcloud import WordCloud #모듈 호출
import matplotlib.pyplot as plt

#워드 클라우드 객체 생성   #WordCloud(사이즈 설정, 배경색 설정)     # generate(시각화 문자열)
wordcloud = WordCloud(width=500, height=500, background_color="white").generate(textData)

plt.imshow(wordcloud) # 워드 클라우드 객체를 맷플롤립에 적용
plt.axis("off") # 축 숨기기
plt.show()

