import pandas as pd
import matplotlib.pyplot as plt




# 叠加柱状图
def accum_bar(df):
    df.sort_values(by="total", ascending=False, inplace=True)
    df.plot.bar(x="Name", y=["Oct", "Nov", "Dec"], stacked=True)

# 水平叠加柱状图
def accum_bar_h(df):
    df.sort_values(by="total", inplace=True)
    df.plot.barh(x="Name", y=["Oct", "Nov", "Dec"],stacked=True)



if __name__ == "__main__":
    users = pd.read_excel("11.xlsx")
    users["total"] = users.Oct + users.Nov + users.Dec # 注意！

    accum_bar_h(users)
    plt.xlabel("Name", fontweight="bold")
    plt.ylabel("Number", fontweight="bold")
    plt.title("User use number by month", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()
