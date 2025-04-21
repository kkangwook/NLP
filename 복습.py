1. 다음 파일에서 뉴스를 가져와 okt로 정규화->명사추출->단어전처리->단어수세기->top50->워드클라우드화
path = r'C:\ITWILL\3_TextMining\data'
daum_news = pd.read_csv(path + '/daum_news.csv')
news = daum_news.news

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')

wc_result = wc.generate_from_frequencies()

2. 다음 텍스트를 정수인코딩하고 패딩or원핫인코딩하기
text = """A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret!
The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word.
His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. The barber went up a huge mountain."""

3.다음 corpus에 대해 문서유사도(2가지) 비교(두가지 방법-bog vs euclidian)
corpus = [
    'i love apple.',
    'apple is delicious which i love too.',
    'i want a delicious food, but not an apple.',
    'deep learning is difficult.'
]

4. 주피터 노트북에 nltk->복습->newdata=pd.read_csv('./archive/movies_metadata.csv')읽어와
영화넣으면 유사한 영화 10개나오는 함수 만들기
