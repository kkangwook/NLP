# extra
from konlpy.tag import Okt, Hannanum, Kkma

morphs=형태소
pos=morphs+tag
nouns=명사

고유기능
1. hannanum
hanna = Hannanum()
hanna.pos(text)-> N:Noun(명사)   J:Josa(조사)   X:Josa appended to adjective stems(형용사에 붙이는 조사)
E:Eomi(어미)   P:PreEomi(선어말어미)   S:Symbol(기호)

hanna.analyze(text) ->복합명사 분해
ex)  [[('실습', 'ncpa'), ('하자', 'ncn')], [('실습', 'ncpa'), ('하', 'xsva'), ('자', 'ecc')], 
      [('실습', 'ncpa'), ('하', 'xsva'), ('자', 'ecs')], [('실습', 'ncpa'), ('하', 'xsva'), ('자', 'ef')]]
ncn:Common noun(일반 명사)           nqq:Other proper noun(기타 고유 명사)   ncpa:Noun phrase(명사구)
jco:Conjunction(접속 조사)           xsva:Verb stem(동사 어간)               ecx:Case-marking particle(격 조사)
px: PreEomi (선어말어미)             etm:Ending particle(선어말어미)         jp:Josa Particle(조사 어미)
ef: Sentence-final ending (마침표)   sf:Final punctuation(문장 부호)         sy:Other punctuation(기타 부호)


2. kkma
kkma의 nouns는 중복제거
text = "중복입니다. 중복입니다. 중복아님 안녕 잘가. "
kkma.nouns(text)  -> ['중복', '중복아', '아', '안녕']
okt.nouns(text)   ->['중복', '중복', '중복', '안녕']
hana.nouns(text)  ->['중복', '중복', '중복아님', '잘']

따라서 여러 줄의 단어들을 kkma로 추출하고 싶을때는
kkma.sentence(para)이후
for i in sentences:
      nouns.append(kkma.nouns(i))  과정이 필요

kkma.pos(text)
NNG 일반 명사         NNP 고유 명사         NNB 의존 명사     NR 수사            NP 대명사   VV 동사
VA 형용사             VX 보조 용언          VCP 긍정 지정사   VCN 부정 지정사    MM 관형사
MAG 일반 부사         MAJ 접속 부사         IC 감탄사         JKS 주격 조사      JKC 보격 조사
JKG 관형격 조사       JKO 목적격 조사       JKB 부사격 조사   JKV 호격 조사
JKQ 인용격 조사       JC 접속 조사          JX 보조사         EP 선어말어미      EF 종결 어미
EC 연결 어미          ETN 명사형 전성 어미  ETM 관형형 전성 어미                  XPN 체언 접두사
XSN 명사파생 접미사   XSV 동사 파생 접미사  XSA 형용사 파생 접미사                XR 어근

SF 마침표,물음표,느낌표    SE 줄임표     SS 따옴표,괄호표,줄표
SP 쉼표,가운뎃점,콜론,빗금     SO 붙임표(물결,숨김,빠짐)
SW 기타기호 (논리수학기호,화폐기호)     SH 한자     SL 외국어     SN 숫자
NF 명사추정범주       NV 용언추정범주     NA 분석불능범

# NNG : 일반 명사, NNP : 고유 명사,  NP : 대명사, OL : 영문만 뽑기
for word, wclass in ex_pos : # ('형태소', '품사')
    if wclass == 'NNG' or wclass == 'NNP' or wclass=='NP' or wclass == 'OL' :
        nouns.append(word)

3. okt
normalized=okt.normalize(text) ->문자열 일반화(반복문자 줄이기, 맞춤법 조정, 특수문자 제거) 
okt.pos(normalize)
'Noun' : 명사     'Josa' : 조사     'Adjective' : 형용사     'Punctuation' : 문장부호 
'Alpha' : 영문    'Verb' : 동사     'Number' : 숫자 




4. TopN단어 선택
from collections import Counter

wc={}
for word in nouns:
  wc[word]=wc.get(word,0)+1

count=Counter(wc)
top3=count.most_common(3)  여기안에 들어가는 숫자로 topn가져옴
