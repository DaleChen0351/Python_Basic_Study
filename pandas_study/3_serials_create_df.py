# 行和列都可以用serials表示，使用不同的方法加入到df中，才能决定是以行还是以列加入df中
    # 列形式加： dict形式
# Series 和 python中dict很像

import pandas as pd


# 创建Serials
def init_serials_by_dict():
    d = {"x":100, "y": 200,"z":300}
    s1 = pd.Series(d) # 生成序列对象
    print(s1)

def init_serials_by_list():
    L1 = ["a","b","c"]
    L2 = [1,2,3]
    s1 = pd.Series(L1,index=L2)
    print(s1)
    print("==================")
    s2 = pd.Series(["d",'e',"f"],index=L2) # 直接
    print(s2)


# 以列的形式添加到df中： using dict
def add_serial_as_new_columns():
    s1 = pd.Series(["Dale","Susan","Linda"],index=range(3),name="Name")
    s2 = pd.Series(["17", "17", "15"], index=range(3), name="age")
    df = pd.DataFrame({s1.name:s1, s2.name:s2})
    print(df)

def add_serial_as_new_columns_with_diff_index():
    s1 = pd.Series(["Dale","Susan","Linda"],index=range(3),name="Name")
    s2 = pd.Series(["17", "17", "15"], index=[1,2,3], name="age")
    df = pd.DataFrame({s1.name:s1, s2.name:s2})
    print(df)



# 以行的形式添加到df中:  using list
def add_serials_as_new_row():
    s1 = pd.Series(["Dale", "Susan", "Linda"], index=range(3), name="Name")
    s2 = pd.Series(["17", "17", "15"], index=range(3), name="age")
    df = pd.DataFrame([s1,s2])
    print(df)

def add_serials_as_new_row_2():
    columns_name = ["Name","Age","Sex"]
    data1 = ["Dale","17","Male"]
    data2 = ["Bob", "22", "Male"]
    s1 = pd.Series(data1,index=columns_name,name=1) # 这里的name就相当于是序号了
    s2 = pd.Series(data2, index=columns_name, name=2)
    df = pd.DataFrame([s1,s2])
    print(df)


# serials 访问








if __name__ == "__main__":
    init_serials_by_dict()
    # init_serials_by_list()
    # add_serial_as_new_columns()
    # add_serial_as_new_columns_with_diff_index()
    # add_serials_as_new_row()
#add_serials_as_new_row_2()