import pandas as pd

# merge
 # 并不是以index作为匹配key值
 # 应该以 on or lefton righton key值设置
def merge_sheets(A,B):
    table = A.merge(B, how="left", on="ID") # 以左边的表为准，在右边的表中查询, 并不是
    table=table.fillna(0) # NA 值填写零
    return table

# left on right on
def merge_sheets_2(A,B):
    A.set_index("ID", inplace=True) # 一旦ID设为了index，那么ID就从普通列消失了
    B.set_index("ID", inplace=True)
    return A.merge(B, left_on="ID",right_on="ID").fillna(0) # 如果key值不一样，可以指定left 和 right的匹配key值，

# join:
# 自动使用index联立
def join_sheets(A,B):
    A.set_index("ID", inplace=True)  # 一旦ID设为了index，那么ID就从普通列消失了
    B.set_index("ID", inplace=True)  # df作为函数参数传递，要注意是否会对原始数据（形参）修改！
    return A.join(B,how="left").fillna(0)


if __name__ == "__main__":
    students = pd.read_excel("16.xlsx",sheet_name="Sheet1")
    scores = pd.read_excel("16.xlsx",sheet_name="Sheet2")

    # table = merge_sheets_2(students,scores)
    table = join_sheets(students,scores)
    print(table)