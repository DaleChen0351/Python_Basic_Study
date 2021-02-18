import pandas as pd
import matplotlib.pyplot as plt


students = pd.read_excel("data/10.xlsx") # dtype={"2016":str, "2017":str}
print(students)
students.sort_values(by="2016", ascending=False, inplace=True)
students.plot.bar(x="Field", y=["2016","2017"], color=["orange", "red"]) # pandas的lib库
plt.title("International Students by Field", fontsize=16, fontweight="bold")
plt.xlabel("Field",fontweight="bold")
plt.ylabel("Number", fontweight="bold")

ax = plt.gca() # get current axis
ax.set_xticklabels(students["Field"],rotation=45, ha='right')

f = plt.gcf() # get current figure
f.subplots_adjust(left=0.2, bottom=0.42)
plt.show()

