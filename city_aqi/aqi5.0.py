import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

city_aqi = pd.read_csv('city_aqi.csv')
print('基本信息：')
print(city_aqi.info())

print('摘要：')
print(city_aqi.head())

#数据清洗(去掉’aqi‘等于0的)
# filter_condition = aqi_data['AQI'] > 0
# clean_data = city_aqi[filter_condition]
clean_data = city_aqi[city_aqi['AQI'] > 0]
#前50个城市的数据可视化
top50 = clean_data.sort_values(by=['AQI']).head(50)
top50.plot(kind='bar',x='city',y='AQI',title='空气质量最好的50个城市',figsize=(20,10))

plt.savefig('top50.png')
plt.show()


