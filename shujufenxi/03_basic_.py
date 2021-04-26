import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



if __name__ == "__main__":
    time = range(2,26,2)
    temp = [15,13,14.5, 17, 20, 25, 26, 26,24, 22, 18,15]
    plt.plot(time, temp)
    plt.show()