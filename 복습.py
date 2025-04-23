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

3-1.다음 corpus에 대해 문서유사도(2가지) 비교(두가지 방법-bog vs euclidian)->각 컬럼값이 어떤 단어인지 보기
corpus = [
    'i love apple.',
    'apple is delicious which i love too.',
    'i want a delicious food, but not an apple.',
    'deep learning is difficult.'
]
-> 새로운 문장 유사도 비교해서 어떤 문장이랑 가까운지
new=['i learned deep learning today']


3-2. 다음 한국어를 전처리해서 문서유사도비교2가지->빈도수 높은거 10개로
texts = ["우리나라    대한민국, 우리나라 만세", "비아그라 500GRAM 정력 최고!",
         "나는 대한민국 우리나라 사람", "보험료 15000원에 평생 보장 마감 임박",
         "나는 홍길동"]

4. 주피터 노트북에 nltk->복습->newdata=pd.read_csv('./archive/movies_metadata.csv')읽어와
영화넣으면 유사한 영화 10개나오는 함수 만들기

5. 주피터->nltk들어가서 slamdunk.csv읽어오기
-1. 구조확인
-2. 정렬(인덱스/값-'키'), 추출이나 제거
-3. SW의 ' '를 nan으로 치환 후 결측치 확인 후 java로 채우기
-4. 중복값 확인 후 중복값 제거
-5. 존재하는 데이터타입은?->current_time이라는 현재시간 새로운 열 만들고 타입확인하고 문자열로 변환 후 시간으로 바꾸고 제거
-6. C를 C#으로 통일-> 전부 소문자로 통일
-7. 이상치처리 함수 만들고 키 기준 2이상인 애들 제거하는 척 하기
-8. 라벨인코딩을 할 필요가 있는 열은?-> 그 열을 라벨인코딩or one-hot encoding 후 새로운 열로 추가
-9. '국어','영어','수학','과학','사회' 열 정규화 두가지 방법
-10. 키로 구간화하고 구간별 개수보기
-11. 국어-영어-수학-과학을 x로 사회를y로하고 0.3의 비율로 train-test split


6. NaiveBayesClassifier 분류기
from nltk.classify import NaiveBayesClassifier  
from nltk.classify.util import accuracy

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
위의 데이터셋으로 데이터 최적화하고 앞의6개를 훈련세, 뒤의 3개를 검증셋으로
-학습하고 검증점수 확인
-예측해보기 ->밑의 데이터셋 하나하나씩(데이터변형필요)
new_sentence1 = "The service was absolutely wonderful!"
new_sentence2="I’ll be home around 6 PM, see you then."
new_sentence3="The service was worst, i hate it."

7. KMeansCluster로 텍스트 군집화, 유사문서끼리 분류
from nltk.cluster import KMeansClusterer
조건:num_clusters=2, distance=nltk.cluster.util.cosine_distance, repeats=25
documents = [
    "I love watching movies",
    "The movie was fantastic and exciting",
    "Hiking is a great outdoor activity",
    "I enjoy going on hikes in the mountains", # 1
    "Movies are a great way to relax",
    "Mountains and nature hikes are my favorite activities" # 1 
]
이 document를 KMeansClustere에 넣어 유사한 문서끼리 분류하고 클래스가 3일때의 결과값은?
옵션: assign_clusters=True
