import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
IO = r'E:\科师\2021春资料\课程\python\课件\第十章 实现数据' \
     r'可视化\数据\1.xlsx'
sheet = pd.read_excel(IO)
# print(sheet['平均成绩'])
a = sheet['平均成绩']
b = pd.cut(a,bins=[50,60,70,80,90,100])
for i,j in dict(b.valu_counts()):
     print(i)
# print(b.value_counts())
# print(b.value_counts().values)
# print(b.value_counts)