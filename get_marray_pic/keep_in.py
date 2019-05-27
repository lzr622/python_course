import requests
from bs4 import BeautifulSoup
'''
下面的data是先在浏览器中登录，然后打开开发者选项，找到一个请求方法为POST的请求，复制里面的Form Data
'''
url = 'http://10.0.0.3:8083/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lg4w9'
data = {'username':'2005536','password':'lzr159258357'}
headers = {'user-agent':'Mozolla/5.0'}
# r = requests.post(url,data= data)
'''
这里用requests的session来请求网页，做到维持同一会话的目的
'''
session = requests.Session()
reqsonse = session.post(url=url, headers=headers, data=data)
'''
接下来就可以请求别的登陆后的页面，而不需要处理cookies
'''
url2 = 'http://10.0.0.3:8083/forum.php?mod=forumdisplay&fid=198&page=1'
r = session.get(url=url2, headers=headers).text
bs = BeautifulSoup(r,'lxml')
link_list = bs.find_all('th',{'class':'new'})
print(link_list)