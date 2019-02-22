# -*- coding: utf-8 -*-
import os
#为了获取C盘路径中的Users后面的类似于Adminisitrator 或者Xu这一段
ls, ls1, ls2 = [], [], []
m = 0
cwd = str(os.getcwd())
for i in "\\":
    cwd = cwd.replace(i, "/")
for i in cwd.strip():
    ls.append(i)
for j in range(len(ls)):
    if ls[j] == "/":
        if m ==1 or m ==2:
            ls1.append(j)
        m += 1
for j in range(ls1[0]+1, ls1[1]):
    ls2.append(ls[j])
str1 = "".join(ls2)
print(str1)