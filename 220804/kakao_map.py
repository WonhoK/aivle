# <과제> 카카오 API 사용해서
# 주소 > 위도, 경도, 우편번호
# 또는 반대
# developers.kakao.com
# - REST_API 키 사용
# - 문서 > 로컬 > 개발 가이드
import requests, json
import pandas as pd

# address to lat & lng
def take_lat_lng(addr):
    # url
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    # request
    REST_API_KEY = "0a997122f334c661398563e341b118d7"
    params = {"query": addr}
    headers = {
        "HOST": "dapi.kakao.com",
        "Authorization": f"KakaoAK {REST_API_KEY}"
    }
    response = requests.get(url, params, headers=headers)
    # json
    data = response.json()["documents"]
    # dataframe
    return pd.DataFrame(data)[["x", "y"]]

print(take_lat_lng("정자로 143"))

# lat & lng to address
def take_addr(x, y):
    # url
    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json"
    # request
    REST_API_KEY = "0a997122f334c661398563e341b118d7"
    params = {"x": x, "y": y}
    headers = {
        "HOST": "dapi.kakao.com",
        "Authorization": f"KakaoAK {REST_API_KEY}"
    }
    response = requests.get(url, params, headers=headers)
    # json
    data = response.json()["documents"]
    # dataframe
    return pd.DataFrame(data)[["address_name"]]

print(take_addr(127.120569318684, 37.3644498769797))