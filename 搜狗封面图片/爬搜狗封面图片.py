#此时爬的为分类的封面图片
# -*- coding: utf-8 -*-
import requests
import urllib
import json, os
from bs4 import BeautifulSoup
#category表示爬的类别，length代表要分类的数量，path表示保存在本地的路径
def getSogpuImag(category, length, path):
    n = length
    cate = category
    imgs = requests.get('https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))
    #loads加载出来的是字典,将imgs转化成文本格式
    jd1 = json.loads(imgs.text)
    print(jd1)
    #jd就是一个列表，元素为字典，每个字典为all_items内的0-15类别每个类别的信息
    #读取字典jd1中的'all_items'的值,all_items的值是列表
    jd = jd1['all_items']
    imgs_url = []
    #读取列表中的每一个字典
    for j in jd:
        imgs_url.append(j['bthumbUrl'])

    m = 0
    for img_url in imgs_url:
        print((str(m)+'.jpg'+'Downloading!').center(40, '*'))
        urllib.request.urlretrieve(img_url, path+str(m)+'.jpg')
        print('Download complete'.center(40, '*'))
        m += 1
#这时候category不能是那网址category后面的那串英文%B1%DA%D6%BD，而是要打开preview之后看到的那个category后面的内容
getSogpuImag('壁纸', 100,os.getcwd()+'/1/')

        
        
