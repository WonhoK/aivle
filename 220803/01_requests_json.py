### WebCrawling
# - 웹 페이지의 종류
# 정적 페이지 : 페이지의 데이터가 변경될 때 URL이 변경 O (HTML)
# 동적 페이지 : 페이지의 데이터가 변경될 때 URL이 변경 X (JSON)
# - request package
# 브라우저의 URL을 입력하면 서버에서 데이터를 다운받아 화면에 출력 : URL > DATA
# requests 패키지 : URL > DATA

### Naver Stock Data
# - KOSPI 지수
# - KOSDAQ 지수
# - USD : 원 달러 환율

import requests
import pandas as pd

### 데이터 수집 (KOSPI)
# 1. 웹 서비스를 분석 (크롬 개발자 도구 사용) : URL
# 개발자 도구 > 네트워크
url = "https://m.stock.naver.com/api/index/KOSPI/price?pageSize=10&page=3"
# 2. request > response : JSON(str)
print('#2')
response = requests.get(url)
print(response)
print(response.text[:200])
print('-------------------------------------------------------')
# 3. JSON(str) > list, dict > DataFrame
print('#3')
data = response.json() # str > list
print(type(data))
print(data[:1])
df = pd.DataFrame(data)[["localTradedAt", "closePrice"]] # list > DataFrame
print(df.tail(2))
print('-------------------------------------------------------')
# 4. 함수 만들기
# params : pagesize, page
def stock_price(pagesize, page, code='KOSPI'):
    """
    This function is crawling stock price form Naver webpage.
    ----------
    *** Params
    pagesize (int) : one page size
    page (int) : page number
    code (str) : KOSPI or KOSDAQ
    ----------
    *** Return
    type : DataFrame (display date, price columns)
    ----------
    """
    url = f"https://m.stock.naver.com/api/index/{code}/price?pageSize={pagesize}&page={page}"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)[["localTradedAt", "closePrice"]]
print()
kospi = stock_price(60, 1)
print(kospi)

# KOSDAQ 데이터 수집 코드 작성
url = "https://m.stock.naver.com/api/index/KOSDAQ/price?pageSize=10&page=1"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)[["localTradedAt", "closePrice"]]
kosdaq = stock_price(60, 1, "KOSDAQ")
print(kosdaq)


### 참고 : docstring
# 함수를 사용하는 방법을 문자열로 작성
# 함수 아래 설명 작성
# """~~~""" 형태로
# help()이용, 혹은 shift+tab 이용
print(help(stock_price))



### 환율 데이터
def exchangeRate(pagesize, page, code="USD"):
    url = f"https://api.stock.naver.com/marketindex/exchange/FX_{code}KRW/prices?page={page}&pageSize={pagesize}"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)[["localTradedAt", "closePrice"]]

usd = exchangeRate(60, 1)
print(usd)

# url --------------> json(str) ----------> list ---------------> dataframe
#       request.get               .json()          .DataFrame()


# 데이터 분석
# 상관관계 분석 : 두 데이터 집합 사이의 어떤 관계가 있는지 확인하는 분석 방법
# ex) 원-달러 환율이 높으면 코스피, 코스닥 지수가 낮다. : <음의 상관관계>

# 피어슨 상관계수
# 1과 가까울수록 강한 양의 상관관계
# -1과 가까울수록 강한 음의 상관관계
# 0과 가까울수록 관계가 없다

# 데이터 전처리 과정
df = kospi.copy()
df["kosdaq"] = kosdaq["closePrice"]
df["usd"] = usd["closePrice"]
df = df.rename(columns={"closePrice" : "kospi"})
# 칼럼 데이터 변경 (str > int) : apply
# df[columns].apply() : 모든 데이터를 함수에 대입한 결과를 출력
df["kospi"] = df["kospi"].apply(lambda data: float(data.replace(",","")))
df["kosdaq"] = df["kosdaq"].apply(lambda data: float(data.replace(",","")))
df["usd"] = df["usd"].apply(lambda data: float(data.replace(",","")))
# 피어슨 상관계수 출력
print(df[['kospi', 'kosdaq', 'usd']].corr())



### copy apply, lambda
# copy
data1 = [1, 2, 3]
data2 = data1         # 얕은복사(주소) : call by reference
data3 = data1.copy()  # 깊은복사(값) : call by value
print(data1, data2, data3)
data1[1] = 4
print(data1, data2, data3) # data2 [1, 2, 3]이 아닌 [1, 4, 3]이 나옴

#apply : 모든 데이터를 func 적용시킨 결과 출력
df = pd.DataFrame(
    [{"age" : 23}, {"age" : 36}, {"age" : 27}]
)
print(df)
def change_ages(age):
    return age // 10 * 10
df["ages"] = df["age"].apply(change_ages)
print(df)

# lambda : 일회성 함수
# 사용 이유 : 간단한 함수(파라미터를 받아서 바로 리턴)를 메모리를 절약하여 사용
def plus(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def calc(func, n1, n2):
    return func(n1, n2)

# 동일한 결과
print(calc(plus, 1, 2), calc(minus, 1, 2))
print(calc(lambda n1, n2 : n1 + n2, 1, 2), calc(lambda n1, n2 : n1 - n2, 1, 2))