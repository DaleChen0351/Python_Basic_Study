import pandas as pd



def drop_duplicates_data(df):
    df.drop_duplicates(subset="Name", inplace=True, keep="first")  # keep="last" 默认是first
    print(df)

def get_duplicated_data(df):
    dupe = df.duplicated(subset="Name")
    df = df.loc[dupe]
    print(df)

def get_duplicated_data2(df):
    dupe = df.duplicated(subset="Name")
    dupe = dupe[dupe==True]
    print(df.iloc[dupe.index]) # 根据df中的index确定哪些row被选中


students = pd.read_excel("data/20.xlsx")
print(students)
print("===================")
# drop_duplicates_data(students)
get_duplicated_data(students)
# get_duplicated_data2(students)
