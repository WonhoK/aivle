### 직방 원룸 매물정보 수집 ###
# - 절차(총 세번의 request!!!)
# 동 이름 > 위도,경도 > geohash > 매물 ID > 매물 정보
#            점    >   범위

import requests
import pandas as pd
import geohash2
# max row, max column 설정
pd.options.display.max_columns = 50

# 1. 동 이름 > 위도,경도
addr = "강남구 역삼동"
url = f"https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸"
response = requests.get(url)
data = response.json()["items"][0]
lat, lng = data["lat"], data["lng"]

# 2. 위도, 경도 > geohash
geohash = geohash2.encode(lat, lng, precision=5)  # precision이 커질수록 영역이 작아짐

# 3. geohash > 매물 ID
url = f"https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={geohash}\
&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸"
response = requests.get(url)
items = response.json()["items"]
ids = [item["item_id"] for item in items]

# 4. 매물 ID > 매물 정보
url = "https://apis.zigbang.com/v2/items/list"
params = {
    "domain": "zigbang",
    "withCoalition": "true",
    "item_ids": ids[:900]
}
response = requests.post(url, params)
items = response.json()["items"]
columns = ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
df = pd.DataFrame(items)[columns]
print(df.tail(2))

# 5. 함수로 만들기
def oneroom(addr):
    url = f"https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸"
    response = requests.get(url)
    data = response.json()["items"][0]
    lat, lng = data["lat"], data["lng"]

    geohash = geohash2.encode(lat, lng, precision=5)

    url = f"https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={geohash}\
&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸"
    response = requests.get(url)
    items = response.json()["items"]
    ids = [item["item_id"] for item in items]

    url = "https://apis.zigbang.com/v2/items/list"
    params = {
        "domain": "zigbang",
        "withCoalition": "true",
        "item_ids": ids[:900]
    }
    response = requests.post(url, params)
    items = response.json()["items"]
    columns = ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
    df = pd.DataFrame(items)[columns]
    df_filtered = df[df["address1"].str.contains(addr)].reset_index(drop=True)
    return df_filtered

print(oneroom("마포구 합정동"))