import pandas as pd
import matplotlib.pyplot as plt

# pandas 的制图是 继承自matplotlib的
 # 所以使用plt.bar 灵活性更大


def pandas_plot_bar(df):
    df.plot.bar(x="Field", y="Number", color="orange", title="International Students by Filed")
    plt.tight_layout()

def matplotlib_plot_bar(df):
    retPlt = plt.bar(df.Field, df.Number,color="orange")
    plt.xticks(df.Field, rotation="90")

    plt.title("International Students by Field")
    plt.xlabel("Field")
    plt.ylabel("Number")
    plt.tight_layout()

    plt.legend([retPlt],["Number"])

if __name__ == "__main__":
    student = pd.read_excel("data/9.xlsx")
    print(student)
    student.sort_values(by="Number",ascending=False, inplace=True)
    # pandas_plot_bar(student)
    matplotlib_plot_bar(student)
    plt.show()