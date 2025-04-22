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
