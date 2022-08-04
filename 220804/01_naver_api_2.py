### Summary ###
# Web : server-client : url
# request, response : get, post

# 페이지 종류
# - 정적 페이지(HTML) : URL 변화 해서 페이지 데이터 변경
# - 동적 페이지(JSON) : URL 변화 없이 페이지 데이터 변경

# 동적 페이지 데이터 수집 프로세스
# 1. 웹서비스 분석 (개발자 도구) : URL
# 2. request(url, params, headers) > response(json) : JSON(str)
# 3. JSON(str) > list, dict > DataFrame

# API를 이용한 데이터 수집
# 1. APP 등록 : application key(id, secret)
# 2. api 문서 : url
# 3. request(url, params, headers(application key)) > response(json) : JSON(str)
# 4. JSON(str) > list, dict > DataFrame

### 크롤링 정책 ###
# - url/robots.txt
# - ex) https://www.ted.com/robots.txt
# - 아직 법적 제재는 없음(권고 사항)
# - 과도한 크롤링으로 서비스에 영향을 주었을 때 문제가 될 수 있음 : 영업 방해, 지적 재산권 침해
# - 크롤링을 할 경우 되도록 API를 사용
# - 사례 : 잡코리아, 사람인

### 네이버 검색어 트랜드 수집 ###
import requests, json
import pandas as pd

# 1. application key
CLIENT_ID = "IPRfMPq0BH_cAWnRCnCK"
CLIENT_SECRET = "MBboJcJTLD"

# 2. documents : url, params, headers
url = "https://openapi.naver.com/v1/datalab/search"
params = {
    "startDate": "2018-01-01",
    "endDate": "2022-07-31",
    "timeUnit": "month",
    "keywordGroups": [
        {"groupName": "트위터", "keywords": ["트위터", "트윗"]},
        {"groupName": "페이스북", "keywords": ["페이스북", "페북"]},
        {"groupName": "인스타그램", "keywords": ["인스타그램", "인스타"]}
    ]
}
headers = {
    "Content-Type": "application/json",
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET
}

# 3. request(url, params, headers) > response(json) : JSON(str)
response = requests.post(url, json.dumps(params), headers=headers)

# 4. JSON(str) > list, dict > DataFrame
# <참고> list comprehension : 간단한 for, if문을 사용하여 리스트 데이터를 만들 때 사용하는 방법
# list[출력문 / 반복문 / 조건문(선택)]
# ex) 0 ~ 9 까지 홀수만 제곱해 리스트를 출력
#     -> result[n**2 for num in range(10) if num % 2]
data = response.json()["results"]
df = pd.DataFrame({
    "data": [period["period"] for period in data[0]["data"]],
    "twitter": [ratio["ratio"] for ratio in data[0]["data"]],
    "facebook": [ratio["ratio"] for ratio in data[1]["data"]],
    "instagram": [ratio["ratio"] for ratio in data[2]["data"]]
})

# 5. visualization
df.plot(figsize=(20,5))