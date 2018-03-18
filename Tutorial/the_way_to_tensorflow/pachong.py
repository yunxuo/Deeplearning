import requests     #获取页面
from bs4 import BeautifulSoup   #解析网页

url = 'http://www.cbooo.cn/year?year=2018'

rawhtml = requests.get(url).content     #先用request去get url 得到里面的content
soup = BeautifulSoup(rawhtml, 'html.parser')
#用beautifulsoup去解析原始的html，这里用的解析器是html.parser,也可以用lxml


movie1 = soup.find_all('table', {'id':'tbContent'})[0]  #[0]的作用是将列表里的第一个元素提取出来

# print(movie1)

movie2 = movie1.find_all('tr')#把每一行的元素以列表的形式抽取出来


# 提取包含电影更多信息的网址
urls=[]
for tr in movie2[1:]:
    urls.append(tr.find_all('td')[0].a.get('href'))

urls=[tr.find_all('td')[0].a.get('href') for tr in movie2[1:]]
#列表里的元素从0开始数，[1：]表示从第二个元素一直到列表最后一个元素

# 提取电影封面图片地址
pictures=[tr.find_all('td')[0].img.get('src') for tr in movie2[1:]]

# movie name
names=[tr.find_all('td')[0].a.get('title') for tr in movie2[1:]]

# movie type
types=[tr.find_all('td')[1].string for tr in movie2[1:]]#string,提取标签之间的字符串,注意string的位置

# movie box
boxoffices=[int(tr.find_all('td')[2].string) for tr in movie2[1:]]

import pandas as pd
df = pd.DataFrame({'name': names,
                   'url': urls,
                   'type': types,
                   'boxoffice': boxoffices,
                   'picture':pictures,
                   },columns =['name','type','boxoffice', 'url','picture'])



df.to_csv ("moviespider.csv" , encoding = "utf-8")#导出为csv文件

df.groupby('type').agg({'boxoffice':["count","mean","sum"]})
#groupby是panda包的一个函数，聚合、分组运算 ；count计数 mean求某类型票房平均值 sum求某类型票房总和

type_mapping = {'喜剧' : 'xj', '爱情' : 'aq', '动作' : 'dz', '科幻' : 'kh',
'剧情' : 'jq', '奇幻' : 'qh', '动画' : 'dh','惊悚' : 'js','战争' : 'zz'}
df['type'] = df['type'].map(type_mapping)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.figure(figsize=(10,6))#像素，宽10*80；高6*80
data = df['boxoffice'].groupby(df['type']).mean()
data.plot(kind='bar',color='blue', stacked=True)
plt.title('电影')
plt.xlabel('电影类型')
plt.ylabel('票房')
plt.legend()   #显示图示
plt.show()


# 圆饼图
data.plot.pie(autopct='%1.2f%%') #画饼图（百分数保留两位小数点）
plt.title("Pie chart")
plt.show()

