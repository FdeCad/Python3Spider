import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('qunar_routes.csv')
#提取评分信息
df['评分']=df.评分.str.extract('(\d\.\d)\/\d分')
'''
#将酒店类型映射成数值型
class_map={' ':0,'舒适型':1}
df['酒店等级']=df['酒店类型'].map(class_map)
df.dropna(axis=1)
'''
#对变量画直方图,查看是否有异常值
# fig,axes=plt.subplots(1,2,figsize=(12,4))
# axes[0].hist(df['价格'],bins=20)
# axes[1].hist(df['评分'],bins=20)
#使用前一个值代替缺失值
df.fillna(method='bfill',limit=1)
df=df.dropna(axis=1)
#按价格从高到低排序
df.sort_values('价格',ascending=False)