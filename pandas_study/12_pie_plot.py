import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel("12.xlsx",index_col="Field")
students["2017"].plot.pie(fontsize=8,startangle=-270) #  counterclock=False

plt.title("source of international students", fontsize=16, fontweight="bold")
plt.ylabel("2017",fontsize=12, fontweight="bold")
plt.show()