1. nltk.corpus: 언어 데이터를 모아놓은 대규모 텍스트 데이터 모음
download 명령으로 다운

-gutenberg
nltk.download('gutenberg') 
from nltk.corpus import gutenberg

dir(gutenberg) 
'''
fileids() : 말뭉치에서 전체 문서파일 가져오기  -> 18종류의 txt파일 존재
files=gutenberg.fileids()[:3]  ->3개 파일이름 가져오기 ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt']
이 파일들을 다음 메서드들에 넣음
raw(files) : 문서 파일에서 원문 가져오기  
paras(files) : 문서 파일에서 문단 가져오기(단어 단위로 3중리스트 안에) ->5265개 문단(리스트개수)
sents(files) : 문서 파일에서 문장 가져오기(단어 단위로 2중리스트 안에) ->16498 문장(리스트개수)
words(files) : 문서 파일에서 단어 가져오기 -> 432174 단어개수
'''




-words
from nltk.corpus import words
nltk.download('words')
eng_words = words.words()  ->리스트형태로 존재
len(eng_words) # 236736


2. 단어들로 이루어진 리스트의 전처리
def clean_text(texts) : 
    from re import sub # 함수 임포트
    texts_re = [st.lower() for st in texts] # 단계1 : 소문자 변경     
    texts_re2 = [sub(r'[^\w\d\s]', '', st) for st in texts_re]  # 단계2 : 특수문자나 문장부호(기호) 제거  
    texts_re3 = [sub('[0-9]', '', st) for st in texts_re2] #단계3 : 숫자 제거 
    texts_re4 = [st for st in texts_re3 if st != '' ] # 단계4 : '' 단어 제거(공백 아님)

    return texts_re4
->이후 불용어 제거


3. lemmatizer
from nltk.stem import WordNetLemmatizer로도 사용가능
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize(word, pos='v') 형식으로 사용

pos 파라미터 : 품사(part-of-speech) 태그 지정
     'a': 형용사 (Adjective)
     'n': 명사 (Noun) : 기본값 
     'v': 동사 (Verb)
     'r': 부사 (Adverb)

4. NaiveBayesClassifier 분류기
train데이터는 밑의 (딕셔너리,클래스)의 튜플형태로 들어감, 클래스값은 이진분류뿐만아니라 다중분류도 가능
    ({"awesome": True, "boring": False}, "pos"),
    ({"awesome": False, "boring": True}, "neg"),

from nltk.classify import NaiveBayesClassifier  
from nltk.classify.util import accuracy   # lr.score()와 같은 기능

dataset = [
    ("I love this movie, it’s fantastic!", 'positive'),
    ("This product is excellent, I would buy it again!", 'positive'),
    ("I hated this movie, it was terrible.", 'negative'),
    ("This is the worst product I have ever bought.", 'negative'),
    ("I’m just going to have lunch now, nothing special.", 'neutral'),
    ("The meeting went as planned, nothing out of the ordinary.", 'neutral'),
    ("Amazing experience, very satisfied!", 'positive'),
    ("Not happy with the service at all.", 'negative'),
    ("The news today was about the economy, pretty standard stuff.", 'neutral')
]

--train데이터형태로 만들기
def extract_features(sentence):
    words = word_tokenize(sentence)
    return {word: True for word in words} # {'단어' : True} : 단어 존재 여부

feature_data = [(extract_features(sentence), label) for (sentence, label) in dataset] #(dict,class)형태로

--훈련셋과 평가셋 나누기
train_data = feature_data[:6] # 6 : 긍정(2)+부정(2)+중립(2)
test_data = feature_data[6:] # 3 : 긍정(1) + 부정(1) + 중립(1)

--학습 .fit대신 .train사용
classifier = NaiveBayesClassifier.train(train_data)

--검증 .score대신 accuracy사용
accuracy(classifier, test_data)

# 분류기 정보 출력 : 학습된 분류기에서 가장 정보량이 높은 특성(feature) 출력  
classifier.show_most_informative_features() # (n=k)로 몇개까지 출력할지

--분류진행 .predict 대신 .classify
new_sentence1 = "The service was absolutely wonderful!" # 긍정문 
features1 = extract_features(new_sentence1) # 특정 추출 
classifier.classify(features1) # 분류기 적용 ->긍정예측

new_sentence2="I’ll be home around 6 PM, see you then."
features2 = extract_features(new_sentence2)
classifier.classify(features2) # 중립 예측

new_sentence3="The service was worst, i hate it."
features3 = extract_features(new_sentence3)
classifier.classify(features3)



5.  nltk.cluster : 텍스트 군집화, 유사문서끼리 분류
from sklearn.feature_extraction.text import CountVectorizer
from nltk.cluster import KMeansClusterer 

documents = [
    "I love watching movies",
    "The movie was fantastic and exciting",
    "Hiking is a great outdoor activity",
    "I enjoy going on hikes in the mountains", # 1
    "Movies are a great way to relax",
    "Mountains and nature hikes are my favorite activities" # 1 
]
vector=CountVectorizer(stop_words='english')
bog=vector.fit_transform(documents).toarray()

num_clusters = 2 # 군집화할 클래스 개수
#분류기
clusterer = KMeansClusterer(num_clusters, 
                            distance=nltk.cluster.util.cosine_distance, #사용할 거리
                            repeats=25)  #반복횟수
#적용
clusters = clusterer.cluster(bog, assign_clusters=True) 
# 클러스터 결과 출력
for i, cluster in enumerate(clusters):
    print(f"Document {i} is in cluster {cluster}")


6. CountVectorizer없이 bog만들기
import pandas as pd 
import numpy as np 
from konlpy.tag import Okt, Kkma
# 원문 텍스트 
text='''
형태소 분석을 시작합니다. 나는 데이터 분석을 좋아합니다. 
직업은 데이터 분석 전문가 입니다. Text mining 기법은 2000대 초반에 개발된 기술이다.
'''
kkma=Kkma()
okt=Okt()
sentences=kkma.sentences(text)
sent_nouns=[]
for i in sentences:
    i=okt.normalize(i)
    sent_nouns.append(okt.nouns(i))

sent_nouns = [['형태소', '분석', '시작'], ['나', '데이터', '분석'], ['직업', '데이터', '분석', '전문가'], ['기법', '초반', '개발', '기술']] 
# 단계1. 유일한 단어집 만들기  
nouns=[]
for i in sent_nouns:
    nouns.extend(i)
    
unique=list(set(nouns))

# 단계2. 영(zeros) 행렬 만들기 
zeros = np.zeros(shape=(len(sent_nouns),len(unique)))

# 단계3. 문서단어행렬(DTM) 만들기 
dtm = pd.DataFrame(zeros,columns=unique)

# 단계4. 문장 단위 단어 카운트
for x,y in enumerate(sent_nouns):
     for i in y:
         dtm.loc[x,i]+=1  # x,i는 행값,열값
print(dtm)
