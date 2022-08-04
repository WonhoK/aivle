### daum exchange ###
# 환율정보 수집
# headers : referer, user-agent
import requests
import pandas as pd

# 1. 웹 서비스 분석 : URL
url = "https://finance.daum.net/api/exchanges/summaries"

# 2. request > response : JSON (str)
headers = {
    "referer": "https://finance.daum.net/exchanges",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}
response = requests.get(url, headers=headers)

# 3. JSON(str) > DataFrame
data = response.json()["data"]
df = pd.DataFrame(data)[["date", "currencyCode", "basePrice"]]
print(df)
