import pandas as pd

city_aqi = pd.read_csv('city_aqi.csv')
print('基本信息：')
print(city_aqi.info())

print('摘要：')
print(city_aqi.head())

print('AQI最大值：',city_aqi['AQI'].max())
print('AQI最小值：',city_aqi['AQI'].min())
print('AQI平均：',city_aqi['AQI'].mean())


top10 = city_aqi.sort_values(by=['AQI']).head(10)

bottom10 = city_aqi.sort_values(by=['AQI'],ascending=False).head(10)


top10.to_csv('top10.csv',index=False)
bottom10.to_csv('bottom10.csv',index=False)
