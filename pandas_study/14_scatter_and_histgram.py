import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 777

def scatter_plot(df):
    df.plot.scatter(x="median_house_value", y="median_income")

def histogram_plot(df,binNum):
    df.plot.hist(bins=binNum)
    plt.xticks(range(0, 10000,1000),fontsize=8, rotation=90)

def kde_plot(df):
    df.plot.kde()
    plt.xticks(range(0, 100000, 500), rotation=90)

if __name__ == "__main__":
    homes = pd.read_csv("data/housing.csv")
    print(homes.head())
    print("==========")
    print(homes.corr())
    histogram_plot(homes.population,100)
    kde_plot(homes.total_rooms)



    plt.show()