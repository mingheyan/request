import requests
from lxml import etree

# cookies = {
#     'auto_id': '422d22d151513f68a1b68caeef8ba330',
#     'uuid': '8e0c089d-579c-4bbe-9fd0-a60b5972d2a6',
#     '_utrace': '8e0c089d-579c-4bbe-9fd0-a60b5972d2a6',
#     'city': '%7B%22cityId%22%3A201%2C%22cityName%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22citySpell%22%3A%22beijing%22%2C%22cityCode%22%3A%22110100%22%2C%22storeId%22%3A321484%7D',
#     'storeId': '321484',
#     'ipCity': '{%22cityId%22:201%2C%22cityName%22:%22%E5%8C%97%E4%BA%AC%22%2C%22citySpell%22:%22beijing%22%2C%22cityCode%22:%22110100%22}',
# }

# headers = {
#     'Accept': '*/*',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'auto_id=422d22d151513f68a1b68caeef8ba330; uuid=8e0c089d-579c-4bbe-9fd0-a60b5972d2a6; _utrace=8e0c089d-579c-4bbe-9fd0-a60b5972d2a6; city=%7B%22cityId%22%3A201%2C%22cityName%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22citySpell%22%3A%22beijing%22%2C%22cityCode%22%3A%22110100%22%2C%22storeId%22%3A321484%7D; storeId=321484; ipCity={%22cityId%22:201%2C%22cityName%22:%22%E5%8C%97%E4%BA%AC%22%2C%22citySpell%22:%22beijing%22%2C%22cityCode%22:%22110100%22}',
#     'Origin': 'https://m.taocheche.com',
#     'Referer': 'https://m.taocheche.com/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
#     'cityId': '201',
#     'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'storeId': '321484',
#     'type': '0',
# }
# def get_city():
#     params = {
#         'type': '0',
#     }

#     response = requests.get(
#         'https://proconsumer.taocheche.com/c-city-consumer/city/v2/get-all-city-by-group',
#         params=params,
#         cookies=cookies,
#         headers=headers,
#     ).json()
#     # print(response)
#     datas = response['data']
#     results =[]
#     for data in datas:
#         cityList = data['cityList']
#         for city in cityList:
#             result={
#                 'cityName':city['cityName'],
#                 'citySpell':city['citySpell']
#             }
#             results.append(result)
#     return results
#     # print(results)
# def main():
#     cities = get_city()
    # print(cities)
headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
#     for city in cities:
#         results =[]
#         for page in range(1,2):
#             # print(city,page)
# #             params={
# #                 'page':str(page),
# # #             }
        

response = requests.get("https://m.taocheche.com/cars?city=beijing",headers=headers)
# print(response)
content  =response.text
# print(content)
html = etree.HTML(content)
# print(html)
divs = html.xpath('//div[@class="CarItem_right__vhygZ"]')
resuly =[]

for div in divs:
    title ="".join(div.xpath('./a/div[@class="CarItem_brand__aqPXu"]/text()'))

    resuly.append(title)
print(resuly)
            
    