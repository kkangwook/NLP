countervectorizer안에는 텍스트들의 리스트 형태로 들어가야함
->한국어를 넣으면 띄어쓰기만을 기준으로하기에 부정확할수있음

1. 한국어의 문서유사도
texts = ["우리나라    대한민국, 우리나라 만세", "비아그라 500GRAM 정력 최고!",
         "나는 대한민국 우리나라 사람", "보험료 15000원에 평생 보장 마감 임박",
         "나는 홍길동"]
----직접 전처리해서 다시 텍스트들의 리스트로 만들어도 되지만 countervectorizer의 tokenizer옵션사용---
from konlpy.tag import Okt
okt=Okt()
def tokenizer(text):
    text=okt.normalize(text)
    return okt.nouns(text)

vector=CountVectorizer(tokenizer=tokenizer)  #TfidfVectorizer도 가능
bog=vector.fit_transform(texts).toarray()
a=vector.vocabulary_
print(a,bog)

-----빈도수 높은거 순서대로 보기----
new_tfidf = TfidfVectorizer(max_features = 20)  #Countervectorizer도 가능



2. 기존 문서에 대해 새로운 문서 유사도 비교
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]
vector=TfidfVectorizer(stop_words='english')
vector.fit(sentences)    #fit_transform대신 fit만
bog=vector.transform(sentences)

new = ['green plant in his study']
newbog=vector.transform(new)

sim=cosine_similarity(newbog, bog)  # (1,3)  반대로 넣으면 (3,1)
sim = sim.reshape(3)
sim_idx = sim.argsort()[::-1]  # 0이 제일 유사한 문장 


3.word2vec :단어를 벡터로 표현하며, 의미적 유사성을 잘 반영하도록 학습
         ->유사 문서나 단어 검색에 이용 ex) “king - man + woman ≈ queen” 같은 연산이 가능
두가지 방식: CBOW(주변단어통해 중심단어 예측), Skip-Gram(중심단어통해 주변단어예측)-> CBOW보다 더 효율적 
word2vec은 다음과 같은 형식으로 들어가야함
sentences = [
    ['나는', '밥을', '먹었다'],
    ['그는', '학교에', '갔다'],
    ['나는', '책을', '읽었다'],
    ['그녀는', '영화를', '봤다']
]
result = [word_tokenize(row) for row in columns.tolist()] 하여 만듬

from gensim.models import Word2Vec
----파라미터----
sentences: 데이터
window: 한번에 학습시킬 단어개수(범위)  (기본값은 5)
min_count:단어가 최소 몇 번 이상 등장해야 학습에 포함되는지 (기본값은 5)
size: 단어 벡터의 차원 (기본값은 100)
sg: 1이면 skip-gram선택, 0이면 CBOW선택

model = Word2Vec(sentences=result, window=5, min_count=1, sg=1)  #모델생성

-유사단어검색-
word_search = model.wv.most_similar(['밥은'],topn=3) #sentences안에있는 데이터 넣음, topn은 유사 상위 개수


