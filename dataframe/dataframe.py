import numpy as np
import pandas as pd
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" #填写url读取
df = pd.read_csv(data_url)
#输出同上，为了节省篇幅这儿就不粘贴了

print (df.head())
print('\n' * 2)

print (df.tail())
print('\n' * 2)

print (df.sort_values(by='tip')) #根据tips排序
print('\n' * 2)

print (df.columns) #打印列名
print('\n' * 2)

print (df.index)   #打印行名
print('\n' * 2)


print (df.ix[10:20, 0:3])  #打印10~20行前三列数据
print('\n' * 2)

print (df.iloc[3]) #选取第三行打印
print('\n' * 2)


print (df.iloc[[1,3,5],[2,4]]) #提取不连续行和列的数据，这个例子提取的是第1,3,5行，第2,4列的数据
print('\n' * 2)

print (df.iat[3,2]) #专门提取某一个数据，这个例子提取的是第三行，第二列数据（默认从0开始算哈）
print('\n' * 2)

print (df.iloc[2:4]) #选取第二行到第四行打印
print('\n' * 2)

print (df.iloc[0,0]) #选取第三行，第二列的数据
print('\n' * 2)

print (df[df.tip>8])
print('\n' * 2)

print (df[(df.tip>7)|(df.total_bill>50)]) #筛选出小费大于$7或总账单大于$50的数据
print('\n' * 2)

print (df[(df.tip>7)&(df.total_bill>50)]) #筛选出小费大于$7且总账单大于$50的数据
print('\n' * 2)

print (df[['day','time']][(df.tip>7)|(df.total_bill>50)])#假如加入了筛选条件后，我们只关心day和time
print('\n' * 2)

print (df.describe()) #描述性统计

group = df.groupby('day')



#1
print (group.first())#打印每一组的第一行数据
print('\n' * 2)
#2
print (group.last())#打印每一组的最后一行数据
