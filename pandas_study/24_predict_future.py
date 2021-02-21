import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel("data/24.xlsx", dtype={'Month':str})
print(sales)

slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)

exp = sales.index * slope + intercept

print("predict: ", 35*slope + intercept)

plt.xticks(sales.index, sales.Month, rotation=90)



plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color="orange")
plt.title(f"y={slope}X+{intercept}")
plt.tight_layout()
plt.show()


