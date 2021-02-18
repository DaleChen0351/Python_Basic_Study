import pandas as pd
import numpy as np
from datetime import date, timedelta

# depandence: openpyxl  xlrd
def init_df():
    ID = [1,2,3,4,5]
    Name = ["Dale","Linda", "Bob","Mike","huahua"]
    Type = ["type", "type", "type","type","type"]

    # init df
    df = pd.DataFrame({"ID":ID, "Name":Name, "Type":Type})
    print(df.head())
    df = df.set_index("ID")
    print("===========")
    print(df)
    df.to_excel("output2.xlsx") # new

# read_excel
def read_with_no_header():
    reader = pd.read_excel("output.xlsx", header=None)
    print(reader)
    print("==============")
    reader.columns = ["ID", "Name","Type"] # 指定columns
    print(reader)



def read_with_index_col():
    reader2 = pd.read_excel("output2.xlsx", index_col="ID")
    print(" index_col")
    print(reader2)
    print(reader2.shape)
    print(reader2.columns)


def read_and_set_index():
    reader = pd.read_excel("output2.xlsx")
    reader = reader.set_index("ID")
    print(" set_index")
    print(reader)

# skiprows = 3, usecols="C:F "
def read_skiprows():
    books = pd.read_excel("data/data.xlsx",skiprows=3,usecols="C:F", dtype={"ID":str, "InStore": str, "Data":str}) # Nan 默认是float64类型，为了后面方便改成str
    print(books.head())
    start = date(2021,2,27)
    for i in books.index:
        books["ID"].at[i] = i+1
        books["InStore"].at[i] = "Yes" if i%2 == 0 else "No"
        books["Data"].at[i] = start + timedelta(days=i)

    books.set_index("ID", inplace=True)
    print(books.head())

# columns


if __name__ == "__main__":
    # read_with_index_col()
    read_skiprows()





