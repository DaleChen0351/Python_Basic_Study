import pandas as pd
import numpy as np

page1 = pd.read_excel("data/27.xlsx",sheet_name="Sheet1")
page2 = pd.read_excel("data/27.xlsx",sheet_name="Sheet2")


# concat axis=1
def concat_axis_1(page1,page2):
    student = pd.concat([page1,page2],axis=1)
    print(student)
# add new columns
def add_new_columns(df):
    df["Age"] = np.arange(0,len(df))
# drop a columns
def drop_a_columns(df):
    df.drop(columns=["Score"],inplace=True)
# insert a columns
def insert_a_columns(df):
    df.insert(1,column="c1",value=np.repeat("foo",len(student)))
# rename
def rename_columns(df):
    df.rename(columns={"c1":"FOO","Name":"name"},inplace=True)
# remove empty
# 只有转化为float类型，才能设为nan

if __name__ == "__main__":
    student = pd.concat([page1,page2]).reset_index(drop=True)
    add_new_columns(student)
    drop_a_columns(student)
    insert_a_columns(student)
    rename_columns(student)
    print(student)