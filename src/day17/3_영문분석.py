from itertools import count

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

all_files = glob.glob("ExcelData*.xls")
# print(all_files) # 엑셀 파일 5개 뜸

all_files_data = []
for file in all_files :
    data_frame = pd.read_excel(file) # 엑셀로 표시
    all_files_data.append(data_frame) #배열에 넣기 (100개씩 5개)
    # print(all_files_data)


#한개로 합치기
all_files_data_concat = pd.concat(all_files_data, axis=0, ignore_index=True) #500개씩 1개
# print(all_files_data_concat)

# csv 파일로 변환
all_files_data_concat.to_csv("myDoExcel.csv",encoding="utf-8",index=False)

# 제목만 따로 빼내기
all_title = all_files_data_concat['제목']
# print(all_title)

영어불용어목록 = stopwords.words('english')

표제어객체 = WordNetLemmatizer()




words = []
for title in all_title :
    Enwords = re.sub(r'[^a-zA-Z]+'," ",title)

    EnWordsToken = word_tokenize(Enwords.lower())

    EnWordsTokenStop =[]
    for w in EnWordsToken :
        if w not in 영어불용어목록 :
            EnWordsTokenStop.append(w)


    EnWordsTokenStopLemma = []
    for w in EnWordsTokenStop :
        EnWordsTokenStopLemma.append(표제어객체.lemmatize(w))
    # print(EnWordsTokenStopLemma)
    words.append(EnWordsTokenStopLemma)

# print(words)


words2 =[]
for w in words :
    words2.extend(w)
# print(words2)

count = Counter(words2)

if "artificial" in count :
    del count["artificial"]

if "intelligence" in count :
    del count["intelligence"]

word_count = dict()
for tag,counts in count.most_common(50) :
    print(word_count)
    if (len(tag)>1) :
        word_count[tag] = counts
# print(word_count)

plt.bar(word_count.keys(),word_count.values())
sorted_keys = sorted(word_count,key=word_count.get , reverse=True)
sorted_Values = sorted(word_count.values(),reverse=True)
plt.xticks(rotation=90, fontsize=5)
plt.show()

all_files_data_concat['doc_count'] = 0
summary_year = all_files_data_concat.groupby('출판일',as_index=False)['doc_count'].count()
plt.figure(figsize=(12,5))
plt.grid(True)
plt.plot(range(len(summary_year)),summary_year['doc_count'])
plt.xticks(range(len(summary_year)),[text for text in summary_year['출판일']],fontsize=5)
plt.show()


stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white",stopwords=stopwords, width=1000, height=500)
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()