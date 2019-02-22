# -*- coding: utf-8 -*-
import winreg, os, time, glob
from PIL import Image
#获得桌面路径
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    #print(winreg.QueryValueEx(key, "Desktop")[0])
    return winreg.QueryValueEx(key, "Desktop")[0]

        
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("A new folder is created!")
    else:
        print("The folder has been existed and all files will be stored in this folder..")
    time.sleep(2)
        
if __name__ == "__main__":
    get_picture_folder = input("enter folder of getting pictures:") #源图片的文件夹名称
    directory = input("enter the folder's name saving pictures:") #需要保存的图片位置的文件夹名称
    keyword = input("enter the keyword of  the picture:") #需要保存的图片关键字
    directory_path = get_desktop() + '/' + directory #图片保存的绝对路径
    mkdir(directory_path)
    m = 0
    class_path = get_desktop()+ '/' + get_picture_folder + '/'  #这是我的图片文件夹的读取路径

    #name为class的类别, glob.glob('c:/pic*.txt')获得C盘pic文件夹下的所有txt格式的文件,返回的是列表格式，该列表的元素为txt格式文件的绝对路径
    for infile in glob.glob(class_path + '*.jpg'): # 遍历所有文件夹下的jpg格式的图片
        try:
            img = Image.open(infile) #使用Image模块打开文件
            #print(img) #返回这些 <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1200x852 at 0x25A199BC9B0>
            #img = img.resize([32, 32], Image.ANTIALIAS) #改变尺寸,并且修改图片有高质量
            file = directory_path + '/' + keyword + '_' + str(m) + '.jpg' #我的图片存放的新路径
            img.save(file) #这种保存形式前提是在Image的情况下打开的图片形式
            m += 1
        except :
            continue
           
        '''
        #用另一种方式来复制图片从一个地方到另一个地方
        fq = open(infile, 'rb')
        content = fq.read() #这个就是url
        #content的内容就是从pics = requests.get(pic_url, timeout=15)的内容，参考图片的实时更新down_pic函数，可以print一下
        fq1 = open(file, 'wb')3#file就是需要保存的图片的新路径
        fq1.write(content)
        fq.close()
        fq1.close()
        '''
