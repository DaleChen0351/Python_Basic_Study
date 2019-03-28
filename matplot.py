import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-1, 1, 256)
C, S = np.arccos(X), np.arcsin(X)
he=C+S

# 绘制cosine函数，颜色是蓝色，line宽为1.0，line类型是实线
plt.plot(X, C, color='blue', linewidth=1.0, linestyle='-',label="cosine")

# 绘制sine函数，颜色是绿色，line宽为1.0，line类型是实线
#plt.plot(X, S, color='green', linewidth=1.0, linestyle='-',label="sine")

#plt.plot(X, he, color='red', linewidth=1.0, linestyle='-',label="np.arccos(X), np.arcsin(X)")

plt.ylim(-5,5)
plt.gridon =True
#plt.yticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.show()