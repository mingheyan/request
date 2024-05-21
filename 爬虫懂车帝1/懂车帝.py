import requests
import pandas as pd
url = "https://index.dongchedi.com/dzx_index/rank/list"
params = {
    "rank_type": "新能源榜单",
"date":"2024-02-03",
"sub_rank_type": "全部新能源",
"price": "全部价格",
"province": "全国"}
headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
res = requests.get(url=url,params=params,headers=headers).json()
# print(res)
datas = res["data"]["form_data"]["data"]
# print(datas)
results = []
for data in datas:
    result = {
        "汽车id":data["id"],
        "name":data["name"]
    }
    results.append(result)
print(results)
data1 = pd.DataFrame(results)
data1.to_csv("汽车数据.csv",index=False)

