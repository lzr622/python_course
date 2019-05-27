import requests
from bs4 import BeautifulSoup
import os


def mkd(name):
    path = name.strip()
    if not os.path.exists(path):
        os.makedirs(name)
        


def get_pic(href,name,header):
    href_ab = 'http://10.0.0.3:8083/' + href
    r = requests.get(href_ab,headers=header).text
    bs = BeautifulSoup(r,'lxml')
    link_list = bs.find_all('img',{'class':'zoom'})
    os.chdir(name)
    for i,link in enumerate(link_list):
        pic_link = link['file']
        url = 'http://10.0.0.3:8083/' + pic_link
        img = requests.get(url,headers=header)
        with open(str(i) +'.jpg','wb+')as f:
            f.write(img.content)
    os.chdir('F:/get_marray_pic/')


def get_marry_link(url,header):
    r = requests.get(url,headers=header).text
    bs = BeautifulSoup(r,'lxml')
    link_list = bs.find_all('th',{'class':'common'})
    for i,link in enumerate(link_list):
        print('已保存了{}套结婚照'.format(i))
        name = link.find('a',{'class':'xst'}).text
        href = link.find('a',{'class':'xst'})['href']
        mkd(name)
        get_pic(href,name,header)


# def login(un,psd,url):
#     data = {'username': un,'password':psd}
#     res = requests.session()
#     r = res.post(url,data=data)
#     r = res.get(url).text
    

def main():

    for i in range(1,2):
        print(i)
        header = {'Cookie':'0cp5_2132_saltkey=Q64Xe6YP; 0cp5_2132_lastvisit=1558660705; 0cp5_2132_ulastactivity=4d7fnAKDlWHmKlaA3wLUR9sv3XS10Ss8p44EUlrmRYdQNwb%2Bj4c6; 0cp5_2132_auth=d90fCMvbCo3u7ODX8z7hTxkMLhf9C4aJY044lJGb6vGEsAFuKTguKN1aAI61%2FLN4HvDNtbQp9VpkpsiZRxgDKRmg; 0cp5_2132_lastcheckfeed=3843%7C1558665018; 0cp5_2132_visitedfid=198; 0cp5_2132_smile=1D1; 0cp5_2132_viewid=tid_11891; 0cp5_2132_sid=SDm5VV; 0cp5_2132_lip=10.0.0.50%2C1558671483; 0cp5_2132_sendmail=1; 0cp5_2132_forum_lastvisit=D_198_1558678116; 0cp5_2132_lastact=1558678176%09forum.php%09ajax'}
        url = 'http://10.0.0.3:8083/forum.php?mod=forumdisplay&fid=198&page='+str(i)
        get_marry_link(url,header)



if __name__ == "__main__":
    main()