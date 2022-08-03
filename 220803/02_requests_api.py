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
print(response.text)

# 4. JSON(str) > list, dict > DataFrame
print(response.json()["message"]["result"]["translatedText"])
