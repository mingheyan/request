import requests
from lxml import etree
import pandas as pd


city = input("城市：")
page = int(input("请输入页数："))
headers ={
   
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

}
city_code_dict={
    "上海":538,"北京":530,'广东': 763
}
url_list =[]
city_code = city_code_dict[city]
for p in range(page):
    url = 'https://sou.zhaopin.com/?jl={}&kw={}&p={}'.format(city_code,'数据分析师',p+1)
    url_list.append(url)
final_df_dict={}
for url,num in zip(url_list,range(len(url_list))):
    print('开始爬取第{}页'.format(num+1))
    response =requests.get(url,headers=headers).text
    html =etree.HTML(response)
    job = html.xpath("//span[@class='jobinfo__name']/text()")
   
    salary = html.xpath("//p[@class='jobinfo__salary']/text()")
    for i in range(len(salary)):
        salary[i] = salary[i].strip('\n').strip(' ').rstrip('\n')
    location,experience,education =([] for i in range(3))
    require = html.xpath("//div[@class='jobinfo__other-info']")
    for req in require:
        exp = req.xpath('.//div[@class="jobinfo__other-info-item"]/text()')[1]
        exp1 =  exp.strip('\n').strip(' ').rstrip('\n')
        experience.append(exp1)
        edu = req.xpath('.//div[@class="jobinfo__other-info-item"]/text()')[2]
        edu1 =  edu.strip('\n').strip(' ').rstrip('\n')
        education.append(edu1)
        
    location = html.xpath("//div[@class='jobinfo__other-info-item']/span/text()")
    data_list =[job,salary,education,experience,location]
    get_data = pd.DataFrame(columns = ['职位名称',"薪资",'教育水平','经验','地点'])
    for col,data in zip(get_data.columns,data_list):
        get_data[col] =data
        
    final_df_dict[num]=get_data
    print('第{}页爬取完成'.format(num+1))
concat_df=pd.concat(list(final_df_dict.values()),ignore_index=True)
file_name = '{}招聘信息.csv'.format(city)
path=r'C:\Users\yan\Desktop\计算机\爬虫\{}'.format(file_name)
concat_df.to_csv(file_name,encoding='utf-8',index=False)
print('{}保存成功'.format(file_name))
    
    
  
        