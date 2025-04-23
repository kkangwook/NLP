countervectorizer안에는 텍스트들의 리스트 형태로 들어가야함
->한국어를 넣으면 띄어쓰기만을 기준으로하기에 부정확할수있음

한국어의 문서유사도
texts = ["우리나라    대한민국, 우리나라 만세", "비아그라 500GRAM 정력 최고!",
         "나는 대한민국 우리나라 사람", "보험료 15000원에 평생 보장 마감 임박",
         "나는 홍길동"]
직접 전처리해서 다시 텍스트들의 리스트로 만들어도 되지만 countervectorizer의 tokenizer옵션사용
from konlpy.tag import Okt
okt=Okt()
def tokenizer(text):
    text=okt.normalize(text)
    return okt.nouns(text)

vector=CountVectorizer(tokenizer=tokenizer)
bog=vector.fit_transform(texts).toarray()
a=vector.vocabulary_
print(a,bog)
