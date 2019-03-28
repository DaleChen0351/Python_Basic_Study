import numpy as np
import matplotlib.pyplot as plt
import math


k=10
x = np.linspace(0, 1*k,500)
xx= np.linspace(0, 300,500)
def my_sinx(lists):
    for it in lists:
        yield math.sin(1/it)*it



def my_area_round(lists):
    for it in lists:
        yield np.pi*it**2

def my_area_round_inverse(lists):
    for it in lists:
        yield math.sqrt(it/np.pi)

y = my_area_round(x)
z = my_area_round_inverse(xx)

yy = list(y)
plt.plot(x, yy,color="green",)
plt.plot(xx, list(z),color="red")
plt.grid()

plt.xlabel('x')
plt.ylabel('y')


plt.show()