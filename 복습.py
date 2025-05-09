정수인코딩: tokenizer, label encoding, one-hot encoding
텍스트 벡터화: bow, tfidf



!!!!!!! tokenizer이용한 정수인코딩은 순서가 중요한 딥러닝에 사용-> 높은 빈도수에 낮은 수 할당 !!!!!!!
        열 위치는 중여X, 어떤 값인지가 중요-> 열개수의 최대값은 샘플들 중 단어가 제일 많은 텍스트->나머지 샘플은 패딩으로 채움
!!!!!!! bow는 나오는 단어순서대로 벡터화+그 텍스트에 나오는 단어빈도수로 표현-> 고전적 머신러닝에 사용!!!!!
        열값이 나오는 단어순서대로 옆으로->단어가 많으면 열도 많아짐
!!!!!!! label encoding은 범주형 데이터에 (ex 나라이름 0~220까지)    !!!!!!!


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
-> 너무 희소하게 나오는 단어는 제거/ 너무 자주 나타나는 단어는 제거 파라미터는?

3-2. 다음 한국어를 전처리해서 문서유사도비교2가지->빈도수 높은거 10개로
texts = ["우리나라    대한민국, 우리나라 만세", "비아그라 500GRAM 정력 최고!",
         "나는 대한민국 우리나라 사람", "보험료 15000원에 평생 보장 마감 임박",
         "나는 홍길동"]

4. 주피터 노트북에 nltk->복습->newdata=pd.read_csv('./archive/movies_metadata.csv')읽어와
영화넣으면 유사한 영화 10개나오는 함수 만들기

5. 주피터->nltk들어가서 slamdunk.csv읽어오기
-1. 구조확인
-2. 정렬(인덱스/값-'키'), 추출이나 제거
-3. SW의 ' '를 nan으로 치환 후 결측치 확인 후 java로 채우기-> 워래 결측치에는 뭐가 들어가야할까? (0,평균,최빈값, median)
        하나의 컬럼에서 몇퍼정도가 결측치값이면 그 컬럼을 안쓸까?          ->(40~50%)
        특정 컬럼이 na일때 그 행들 제거하는 방법은?        df=df[ ~df[col].isnull() ]
-4. 중복값 확인 후 중복값 제거
-5. 존재하는 데이터타입은?->current_time이라는 현재시간 새로운 열 만들고 타입확인하고 문자열로 변환 후 시간으로 바꾸고 제거
-6. C를 C#으로 통일-> 전부 소문자로 통일
-7. 이상치처리 함수 만들고 키 기준 2이상인 애들 제거하는 척 하기/ 박스플롯으로 IQR로도 확인해보기
        .describe()로 iqr=75%-25%하고 25%-1.5*iqr 와 75%+1.5*iqr로 가져오기
-8. 라벨인코딩을 할 필요가 있는 열은?-> 그 열을 라벨인코딩or 
        one-hot encoding은 가변수 기준화하여 k-1개로 인코딩 후 새로운 열로 추가     by: drop_first=True
-9. '국어','영어','수학','과학','사회' 열 정규화 두가지 방법
-10. 키로 구간화하고 구간별 개수보기
-11. 국어-영어-수학-과학을 x로 사회를y로하고 0.3의 비율로 train-test split



--'텍스트' classification에 쓰이는 nltk모델 두가지-------------------


-nltk의 두 모델 차이는?                    (지도학습vs비지도학습)

6. NaiveBayesClassifier 분류기
from nltk.classify import NaiveBayesClassifier  
from nltk.classify.util import accuracy

-들어갈수있는 타깃형태는?

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
이 document를 전처리하고(소문자화+stem+불용어제거) KMeansClustere에 넣어 유사한 문서끼리 분류하고 클래스가 3일때의 결과값은?
옵션: assign_clusters=True



--'텍스트' classification에 쓰이는 sklearn모델 두가지-------------------

-두 모델 차이점은?                    (지도학습 vs 비지도학습)
8. 분류
from sklearn.naive_bayes import MultinomialNB # Naive Bayes model
from sklearn.metrics import accuracy_score, confusion_matrix # 평가 
from sklearn.preprocessing import LabelEncoder # 10진수 인코딩 

-multinomialNB에 들어갈 수 있는 데이터 형태는?                              (tfidf,인코딩/문자)

-데이터: df[0]가 정답, df[1]이 텍스트
path = r"C:\ITWILL\3_TextMining\data"
df = pd.read_csv(path + '/spam_data.csv', header=None, encoding='utf-8')

-이 데이터를 전처리하고 test_size=0.2로->학습->예측(텍스트와 예측값 같이보기)->검증 두가지
-정답을 정수 인코딩해서도 해보기
-100번 인덱스의 이메일과 예측값 출력해서 보기

9.군집화
from sklearn.cluster import KMeans

-데이터
documents = [
    "I don't like rainy days.",
    "She isn't feeling well today.",
    "They haven't finished their homework yet.",
    "He can't stand the cold weather.",
    "We didn't enjoy the movie at all.",
    "I love spending time with my family.",
    "She is an incredibly talented musician.",
    "They have accomplished so much in their careers.",
    "He always has a positive attitude.",
    "We had a fantastic time on our vacation."
]

-데이터 전처리해서 n=2로 군집화-> 어떻게 군집화 됐는지 보기
text=["i don't like, hate, isn't"]로 예측해보기
