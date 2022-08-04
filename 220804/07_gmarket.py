### Gmarket ###
# 베스트 상품 200개 수집

import requests
import pandas as pd
from bs4 import BeautifulSoup

# 1. 웹 서비스 분석 : URL
url = "http://corners.gmarket.co.kr/Bestsellers"

# 2. request > response : HTML(str)
response = requests.get(url)

# 3. HTML(str) > BeautifulSoup Object
dom = BeautifulSoup(response.text, "html.parser")

# 4. BeautifulSoup Object > CSS Selector > DataFrame
# 개발자도구 엘리먼트 찾아서 오른쪽 버튼 > copy > copy selector
elements = dom.select("#gBestWrap > div > div:nth-child(5) > div > ul > li")
items = []
for element in elements:
    data = {
        "title": element.select_one(".itemname").text,
        "o_price": element.select_one(".o-price").text,
        "s_price": element.select_one(".s-price > strong").text,
        "img" : "http:" + element.select_one("img").get("data-original")
    }
    items.append(data)
df = pd.DataFrame(items)
print(df)
