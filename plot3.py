# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  

salary = [2500, 3300, 2700, 5600, 6700, 5400, 3100, 3500, 7600, 7800, 
          8700, 9800, 10400]

group = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]


plt.hist(salary, group, histtype='bar', rwidth=0.8)

plt.legend()

plt.xlabel('salary-group')
plt.ylabel('salary')

plt.title(u'测试例子——直方图', FontProperties=font)

plt.show()