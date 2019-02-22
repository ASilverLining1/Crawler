#!-*- coding:utf-8 -*-
import numpy as np
from PIL import  Image
import os, glob
#第一部分， 本地路径下的图片读取转换成数组形式，方便后续计算
classes = ['dog', 'cat']
arr = [[]]
print(os.getcwd())
for index, name in enumerate(classes):
    class_path = os.getcwd()+'/data/'+name + '/' #这是我的图片文件夹的存放路径
    #print(glob.glob(class_path+'*.jpg'))
    #glob.glob('c:/pic/*.txt')获得C盘pic文件夹下的所有txt格式的文件,返回的是列表格式，该列表的元素为字符串，为所有txt格式文件的绝对路径
    for infile in glob.glob(class_path + '*.jpg'): #遍历所有文件夹下的jpg格式的图片
        file,ext = os.path.splitext(infile) #将文件路径和名字与格式拆分
        img = Image.open(infile) #使用Image模块打开文件
        img = img.resize([32, 32]) #改变尺寸
        r, g, b = img.split()#将彩色图片拆分为三色通道，r,g,b分别为red,green,black
        #注意r, g, b全部为向量，并不是矩阵，向量的shape是用(1024,)表示，横的显示里面的是元素
        #而矩阵不同,其shape(1024,1)和(1, 1024)不一样，前者为1024行1列；后者为1行1024列
        r_array = np.array(r).reshape([1024])#利用numpy将三色通道中的图片信息数据化
        g_array  =np.array(g).reshape([1024])# 将32 * 32的三色通道的图像都reshape成一行
        b_array  =np.array(b).reshape([1024])
        merge_array = np.concatenate((r_array, g_array, b_array))#将三色通道的图片信息拼接，这就是一张图片的所有信息, shape =(1024*3, )
        if arr == [[]]:
            ##数组一维的就是向量，二维的就是矩阵，向量在外面加[]会变成矩阵
            arr = [merge_array]  #第一张图片放到列表中，后面经过numpy 中的concatenate会变成ndarray格式的
            continue
        #np.concatenate是针对数组进行计算的
        arr = np.concatenate((arr, [merge_array]), axis = 0) #将所有文件夹下的所有的jpg格式的图片信息拼接成一个数组            
#arr就是所要的所有图片的像素
print(arr.shape)


#Eg2 #原路径覆盖保存图片
'''
        class_path = file + '/' #这是我的图片文件夹的存放路径
        print(class_path)
        #name为class的类别, glob.glob('c:/pic*.txt')获得C盘pic文件夹下的所有txt格式的文件,返回的是列表格式，该列表的元素为txt格式文件的绝对路径
        for infile in glob.glob(class_path + '*.jpg'): # 遍历所有文件夹下的jpg格式的图片
            img = Image.open(infile) #使用Image模块打开文件
            img = img.resize([32, 32], Image.ANTIALIAS) #改变尺寸,并且修改图片保证有高质量
            img.save(infile) #原路径覆盖保存
        
        #如果不想图片按照原路径覆盖，另外创建文件夹，比如说桌面路径
'''
#Eg3 #另外创建路径保存图片
#参考 图片从一个地方保存到另一个地方.py