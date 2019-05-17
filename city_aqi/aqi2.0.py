import requests
from bs4 import BeautifulSoup
import csv


# 获取所有城市的空气信息,存入数组中
def get_all_city(url):
    r = requests.get(url)
    bs = BeautifulSoup(r.text,'lxml')
    all_city = bs.find_all('div',{'class':'bottom'})[1]
    city_list = all_city.find_all('a')
    city_link = []
    for city in city_list:
        city_name = city.text
        
        city_pinyin = city['href'][1:]
        city_link.append((city_name,city_pinyin))
    return city_link
    
def get_city_aqi(url,pinyin):
    # 返回url的文本
    url = url + pinyin
    r = requests.get(url,timeout = 30)
    soup = BeautifulSoup(r.text,'lxml')
    num_all = soup.find_all('div',{'class':'span1'})
    aqi_list = []
    for i in range(8):
        one_zb = num_all[i]
        #print(type(one_zb))
        value = one_zb.find('div',{'class':'value'}).text.strip()
        #print(value)
        #caption = one_zb.find('div',{'class':'caption'}).text.strip()
        #print(caption)
        aqi_list.append(value)
    return aqi_list


def main():
    # city_pinyin = input('请输入城市拼音：')
    # url = 'http://pm25.in/' + city_pinyin
    url = 'http://pm25.in/'
    city_list = get_all_city(url)
    # s = 0
    # for one_city in city_list:
    #     if s < 3:
    #         print(one_city)
    #         pinyin = one_city[1]
    #         city_aqi = get_city_aqi(url,pinyin)
    #     # api_div = '''<div class="span12 data">
    #     #     <div class="span1">
    #     #       <div class="value">
    #     #         '''
    #     # begin_index = url_text.find(api_div)
    #     # begin_index = begin_index+len(api_div)
    #     # end_index = begin_index + 2
    #     # api = url_text[begin_index:end_index]
    #         for i in range(len(city_aqi)):
    #             print('该城市的{}是：{}'.format(city_aqi[i][0],city_aqi[i][1]))
    #         s= s+1
    #     else:
    #         break
    header = ['city','AQI','PM2.5/1h','PM2.5/10h','CO/1h','NO2/1h','O3/1h','O3/8h','SO2/1h']

    with open('city_aqi.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            if ((i+1)%10 == 0):
                print('已输出{}条数据，（共有{}条记录）'.format(i+1,len(city_list)))
            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(url,city_pinyin)
            row = [city_name] + city_aqi
            writer.writerow(row)


if __name__ == "__main__":
    main()