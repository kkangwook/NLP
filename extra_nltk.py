1. nltk.corpus: 언어 데이터를 모아놓은 대규모 텍스트 데이터 모음
download 명령으로 다운

-gutenberg
nltk.download('gutenberg') 
from nltk.corpus import gutenberg

dir(gutenberg) 
'''
fileids() : 말뭉치에서 전체 문서파일 가져오기  
raw() : 문서 파일에서 원문 가져오기  
paras() : 문서 파일에서 문단 가져오기(단어 단위)
sents() : 문서 파일에서 문장 가져오기(단어 단위) 
words() : 문서 파일에서 단어 가져오기 
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
