### API
# application programing interface
# api를 사용하여 데이터를 수집하는 것은
# 서비스에 데이터를 제공하는 공식적인 방법으로 데이터 수집
# naver api : papago api

import pandas as pd
import requests, json

# 1. APP등록 > app_key(request_token) 수집
# https://developers.naver.com
# Application > 등록하기 페이지
# CLIENT_ID, CLIENT_SECRET= "KcavGNB3lps84cp5kzJp", "CpZgLBr_NB"
CLIENT_ID, CLIENT_SECRET= "IPRfMPq0BH_cAWnRCnCK", "MBboJcJTLD"

# 2. Naver API document 확인 > URL
# Documnets > 파파고 번역 > API 레퍼런스 페이지
url = "https://openapi.naver.com/v1/papago/n2mt"
txt = "파이썬 꿀잼"
params = {"source": "ko", "target": "en", "text": txt}
headers = {
    "Content-Type": "application/json",
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET
}

# 3. request(URL, app_key) > response(json) : JSON(str)
# json.dumps() : 인터넷 트래픽에서는 영문, 숫자, 특수문자만 사용가능
#                한글과 같은 문자를 인코딩해주는 함수(영문, 숫자, 특수문자로)
response = requests.post(url, json.dumps(params), headers=headers)

# 4. JSON(str) > list, dict > DataFrame
response.json()["message"]["result"]["translatedText"]

# 5. 함수로 작성
def translate(txt):
    url = "https://openapi.naver.com/v1/papago/n2mt"
    params = {"source": "ko", "target": "en", "text": txt}
    headers = {
        "Content-Type": "application/json",
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }
    response = requests.post(url, json.dumps(params), headers=headers)
    txt_en = response.json()["message"]["result"]["translatedText"]
    return txt_en

txt = "웹 크롤링은 재미있습니다"
txt_en = translate(txt)
print(txt_en)

# excel을 불러와서 excel로 저장
covid = pd.read_excel("covid.xlsx")[["category", "title"]]
covid_en = covid["title"].apply(translate)
covid["title_en"] = covid_en
print(covid)
covid.to_excel("covid_en.xlsx",index=False,encoding="utf-8-sig")