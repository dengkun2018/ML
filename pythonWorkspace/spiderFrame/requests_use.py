# coding=gbk
import requests
import json

from PIL import Image
from io import  BytesIO
from bs4 import  BeautifulSoup

#print(dir(requests))

url='http://www.baidu.com'
r=requests.get(url)
print(r.text)
#print(r.status_code)
#print(r.encoding)

'''
#���ݲ���
params={'pageID':'1','type':['1','2','3']}
r=requests.get(url,params)
print(r.url)

params2={'username':'dk','password':'123456'}
r2=requests.get(url,params2)
print(r2.url)

'''


#����������
# r=requests.get("https://www.baidu.com/img/bd_logo1.png?where=super")
# image=Image.open(BytesIO(r.content))
#image.save("baidu.png")  #ע�Ᵽ��ͼƬ�ĺ�׺

'''
#json����
r=requests.get('https://github.com/timeline.json')
print(type(r.json))
print(r.text)
'''


#ԭʼ���ݴ���
# r=requests.get("https://www.baidu.com/img/bd_logo1.png?where=super",stream=True)#����Ϊ������
# with open('baidu2.png','wb+') as f:
#     for chunk in r.iter_content(1024):
#         f.write(chunk)

'''
#�ύ��
#����һ
form={'username':"user",'password':"pass"}
r=requests.post('http://httpbin.org/post',data=form)
print(r.text)
print('*'*50)
#����2
r=requests.post('http://httpbin.org/post',data=json.dumps(form))
print(r.text)
'''

#cookie
'''
url='http://www.baidu.com'
r=requests.get(url)
cookies=r.cookies
for k,v in cookies.get_dict().items():
    print(k,v)
'''
# cookies1={'c1':'v1','c2':'v2'}
# r=requests.get('http://httpbin.org/cookies',cookies=cookies1)#�ϴ�cookies��Ϣ
# print(r.text)


#�ض�����ض�����ʷ
'''
r=requests.head('http://github.com',allow_redirects=True)
print(r.url)
print(r.status_code)

'''

soup=BeautifulSoup(r.text)
print(soup.prettify())
print(soup.title)

print(soup.select('.cp-feedback'))#class="cp-feedback"
print(soup.select('#lh'))#id="lh"


