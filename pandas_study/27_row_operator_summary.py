import pandas as pd



# union page1 and page2
def union_page1_page2(page1, page2):
    students = page_1.append(page_2).reset_index(drop=True) # drop origin index
    return students

# append a row in the end
def add_a_row_in_the_end(df):
    neo_row = pd.Series({"ID": 41, "Name": "Peter", "Score": 99}, name=40)  # name is the index for the new row
    df = df.append(neo_row)  # another way is set ignore_index = True
    return df

# replace using "iloc"
def replace_a_row_by_iloc(df):
    stu = pd.Series(["39", "Dale",99], index=df.columns.values)
    df.iloc[38] = stu
    return df

# delete a row: drop
def delete_a_row_by_index_list(s):
    df = s  #如果不加copy，则相当于是浅拷贝
    df.drop(index=[0,1,2],inplace=True)

# delete
def delete_a_row_by_slice_index(df):
    df.drop(index=df[0:3].index, inplace=True) # slice是第几行的含义，不是index值

# condition drop
def delete_rows_with_empty_name(df):
    df["Name"].at[14] = ""
    missing = df.loc[df["Name"] == ""]
    df.drop(index=missing.index,inplace=True)
    df = df.reset_index(drop=True)
    print(df)


if __name__ == "__main__":
    page_1 = pd.read_excel("data/27.xlsx", sheet_name="Sheet1")
    page_2 = pd.read_excel("data/27.xlsx", sheet_name="Sheet2")
    student = union_page1_page2(page_1,page_2)
    student = add_a_row_in_the_end(student)
    # replace using "at"
    student.at[39,"Name"] = "Susan" # 为啥这里没有改变内存中的值？
    # replace using "iloc"
    student = replace_a_row_by_iloc(student)
    # insert a row within df
    part1 = student.iloc[:20]
    part2 = student.iloc[20:]
    new_data = pd.Series(["101", "Bob", "60"],index=student.columns.values)
    student = part1.append(new_data, ignore_index=True).append(part2).reset_index(drop=True)

    #
    delete_a_row_by_index_list(student)
    delete_a_row_by_slice_index(student)
    # delete empty name
    delete_rows_with_empty_name(student)


