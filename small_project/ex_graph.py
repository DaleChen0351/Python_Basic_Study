import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-5,5,500)
y = np.power(np.e, x)

plt.plot(x,y)
plt.grid()


plt.show()
