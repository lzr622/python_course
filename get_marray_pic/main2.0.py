# 相比第一版更改为了用户名和密码登陆,更方便

import requests
from bs4 import BeautifulSoup
import os
import random

def mkd(name):
    path = name.strip()
    if not os.path.exists('F:/get_marray_pic/'+path):
        os.makedirs('F:/get_marray_pic/'+path)
        


def get_pic(href,name,res,i,s):
    href_ab = 'http://10.0.0.3:8083/' + href
    r = res.get(href_ab).text
    bs = BeautifulSoup(r,'lxml')
    os.chdir('F:/get_marray_pic/'+name)
    try:
        link_list = bs.find_all('img',{'class':'zoom'})
    except:
        print('第{}页第{}个文章的图片地址不对'.format(i,s))
    else:
        for b,link in enumerate(link_list):
            try:
                pic_link = link['file']
            except:
                print('第{}页第{}个文章的第{}图片地址不对'.format(i,s,b+1))
            else:
                pic_link = link['file']
                url = 'http://10.0.0.3:8083/' + pic_link
                img = res.get(url)
                with open(str(b) +'.jpg','wb+')as f:
                    f.write(img.content)
    os.chdir('F:/get_marray_pic/')


def get_marry_link(url,res,i):
    c = i
    b = i - 1
    b = b*20
    r = res.get(url).text
    bs = BeautifulSoup(r,'lxml')
    link_list = bs.find_all('tbody')
    s = 0
    for link in link_list:
        if (link.find('a',{'class':'xst'})):
            # if s<15:
            #     s = s+1
            # else:
            s = s+1
            name = link.find('a',{'class':'xst'}).text
            href = link.find('a',{'class':'xst'})['href']
            mkd(name)
            get_pic(href,name,res,c,s)
            print('已保存了{}套结婚照'.format(s+b))


def login(un,psd,url,page):
    data = {'username': un,'password':psd}
    res = requests.Session()
    r = res.post(url,data=data).text
    bs = BeautifulSoup(r,'lxml')
    if bs.find('a','top_reg'):
        msg1 = '密码错了老弟,重新输'
        msg2 = '似不似撒,密码都记不住,重新输'
        msg3 = '内网密码都忘了,你还能记住点啥,重新输'
        msg4 = '没啥说的,重新输'
        arr = [msg1,msg2,msg3,msg4]
        print(random.choice(arr))
        usrn = input('请输入内网账号:')
        psd = input('请输入账号密码:')
        page = page
        url1 = url
        return login(usrn,psd,url1,page)
    else:
        print('连接成功')
        return res

def is_int(page):
    try:
        int(page)
    except:
        page = input('页数必须为大于0的正整数,请重新输入:')
        return is_int(page)
    else:
        if int(page) <= 0:
            page = input('页数必须为大于0的正整数,请重新输入:')
            return is_int(page)
        else:
            for s,i in enumerate(page):
                if i!= '0':
                    p = int(page[s:])
                    return p

    

def main(usrn,psd,page):
    url = 'http://10.0.0.3:8083/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lg4w9'
    page = is_int(page)
    page = page+1
    res = login(usrn,psd,url,page)
    for i in range(1,page):
        url = 'http://10.0.0.3:8083/forum.php?mod=forumdisplay&fid=198&page='+str(i)
        get_marry_link(url,res,i)
    
    input("Press <enter>")


if __name__ == "__main__":
    usrn = input('请输入内网账号:')
    psd = input('请输入账号密码:')
    page = input('请输入想保存到第几页:')
    main(usrn,psd,page)