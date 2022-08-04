### 정적 페이지 데이터 수집 ###
# - 네이버 연관 검색어 수집
# - bs4 (BeautifulSoup) : HTML(str) > CSS Selector를 이용하여 엘리먼트 선택

import requests
import pandas as pd
from bs4 import BeautifulSoup

# 1. 웹 서비스 분석 : URL
keyword = "kt"
url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={keyword}"

# 2. request(url) > response(html) : HTML(str)
response = requests.get(url)

# 3. HTML(str) > BeautifulSoup Object > BS(CSS Selector) > Data
dom = BeautifulSoup(response.text, "html.parser")  # BeautifulSoup Object
# select() : 엘리먼트 여러 개 선택
# select_one() : 엘리먼트 한 개 선택
elements = dom.select(".lst_related_srch > .item")

# keywords = []
# for element in elements:
#     keyword = element.select_one(".tit").text
#     keywords.append(keyword)
keywords = [element.select_one(".tit").text for element in elements]  # 위와 같은 코드(List comprehension)

# 4. Data > DataFrame
df = pd.DataFrame(keywords)
print(df)
