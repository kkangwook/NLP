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
