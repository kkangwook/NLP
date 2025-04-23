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
