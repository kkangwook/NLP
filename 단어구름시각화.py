#단어구름시각화
from konlpy.tag import Okt 
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt 

data
normalized=okt.normalize(data)  #정규화
nouns=okt.nouns(normalized)    #명사추출

nouns_count = {} # 단어 카운터
for noun in nouns : 
    if len(noun) > 1 :
        nouns_count[noun] = nouns_count.get(noun, 0) + 1

# TopN 단어 선정  
word_count = Counter(nouns_count)
top5_word = word_count.most_common(5) 

#  단어 구름 시각화객체 생성(안에 설정들)
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',   # 한글 폰트 경로 
          width=500, height=400,                          # 윈도 크기 
          max_words=100,max_font_size=150,                # 최대 빈도수와 폰트크기 
          background_color='white')                       # 배경색 

# 단어구름이미지 생성
wc_result = wc.generate_from_frequencies(dict(top5_word))  #딕셔너리 형태로 넣음

#시각화
plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()



#--------------------------------kkma사용버전-------------------
from konlpy.tag import Kkma
kkma = Kkma()  
sentences=kkma.sentences(texts)

nouns = [] # 중복 명사 저장
for sentence in sentences:
    nouns=nouns+kkma.nouns(sentence)

# okt처럼 정규화 없어서 따로 전처리(단어 길이 1음절 제외, 숫자 제외)
nouns_count = {} # 단어 카운터 
from re import match 
for noun in nouns : 
    if len(noun) > 1 and not(match('^[0-9]', noun)) :  #숫자제외
        nouns_count[noun] = nouns_count.get(noun, 0) + 1
하고 진행
