import requests
url = "https://api.iyiou.com/api/company/list"
headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
params = {
    "page": "4",
"pageSize":"20",
'sortKey': 'valuation',
'sortType': 'desc'
}
res = requests.post(url=url,params=params,headers = headers).json()
datas = res['data']['com_list']
results = []
for data in datas:
    tags = data["tags"]
    tagname =[tag['tagName'] for tag in tags]
    result = {
        "1":tags,
        "公司名称": data['fullName'],
        '公司简介':data['detailIntro']
        
    }
    results.append(result)
    print(results)
import pandas as pd
data1 = pd.DataFrame(results)
data1.to_csv("公司.csv",index=False)
    
    