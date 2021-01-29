import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,2*np.pi,500)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.cos(x)-1
 
 
plt.plot(x,y1,color = 'r',label = 'sinx')         #label每个plot指定一个字符串标签
plt.plot(x,y2,'-.', color = 'b', label = 'cosx')
plt.plot(x,y3,'--', color = 'g', label = 'cosx-1')
plt.legend(loc='lower right')
 
plt.savefig('.//result//3.7.png')
plt.show()