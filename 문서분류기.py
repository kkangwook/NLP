-텍스트분류: Naive Bayes사용   (수치형 분류는 Kneighborsclassifier, logistic regression, SGDclassifier)
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer # DTM 
from sklearn.naive_bayes import MultinomialNB # Naive Bayes model
from sklearn.metrics import confusion_matrix, accuracy_score # model 평가

# 1. dataset 만들기 
texts = [
    "I don't like rainy days.",
    "I love spending time with my family.",
    "She isn't feeling well today.",
    "She is an incredibly talented musician.",
    "They haven't finished their homework yet.",
    "They have accomplished so much in their careers.",
    "He can't stand the cold weather.",
    "He always has a positive attitude.",
    "We didn't enjoy the movie at all.",
    "We had a fantastic time on our vacation." ]

target = [1,0,1,0,1,0,1,0,1,0] # 정답

# 평가용 데이터셋    
test_texts = ["I don't like chocolate ice cream.",
              "She isn't going to the party tonight.",
              "I love spending time with my family.",
              "They didn't finish their homework on time."]

test_target= [1,1,0,1] # 정답

-데이터가 모델에 들어갈때는 x=tfidf, y=target 형태로 들어감, 이때 y는 숫자, 문자도 가능!!!!!!!!!!!, 다중분류도 가능!!!!!

train = pd.DataFrame({'target' : target, 'texts' : texts}) 
x_train=train['texts']
y_train=train['target']

test = pd.DataFrame({'target' : test_target, 'texts' : test_texts}) 
x_test=test['texts']
y_test=test['target']


#tfidf만들기
tfidf = TfidfVectorizer(stop_words='english')
train_dtm = tfidf.fit_transform(x_train) 
x_train = train_dtm.toarray()

x_test=tfidf.transform(x_test).toarray()

# 모델 만들기
model = MultinomialNB()
model.fit(x_train, y_train)

#예측
y_pred=model.predict(x_test)
y_pred

#검증
valid_matrix=confusion_matrix(y_test,y_pred)
print(valid)  #diagnol이 정분류된애들 개수, 나머지가 잘못분류개수

score=accuracy_score(y_test, y_pred)
print(score)   # R^2값과 유사(실제y값, 예측y값으로 넣어야함)
