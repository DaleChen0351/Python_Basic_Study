import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_ = pd.read_csv("csv_out.csv")
print(data_.head(5))
print(data_.shape)
print(data_.columns)
print(data_.index)
print(data_.dtypes)

print("")
#查询列
print(data_["lane"])
print(data_[["lane", "Vy"]])# 依然是一个dataFrame对象

#替换列
data_.loc[:, "lane"] = data_["lane"].str.replace("ego", "Ego") # 写入修改是不是只能是用loc函数？
print(data_)
# 条件查询
print("————————————————————————————-")
print(data_.loc[data_["Vx"] < 28.5, :])# good
# 查询行
print("")
print(data_.loc[4])
print(data_.loc[4:5])

# series 创建
print("")
print("series with list")
temp_list = [1, 2, 2.4, "left"]
series1 = pd.Series(temp_list)
print(series1)

print("series with map")
temp_map = {"A": "apple", "B": "ball", "C": 100}
print(pd.Series(temp_map))

print("series with index")
s3 = pd.Series(temp_list, index=["dx", "dy", "vx", "vy"])
print(s3)
print(s3.index )

print("search info")
print(s3["dx"])
print(s3[["dx", "dy"]])

# DataFrame
print("")
print("mulit-map ctor a DataFrame")
data = \
{
    "dx": [12.5, 13.4, 13.6],
    "dy": [22.3,24.1, 44.5],
    "lane": ["ego", "left", "right"]

}
df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df.index)



# df.set_index("ymd",inplace = True)
# 将默认索引，改成按日期索引

# 查询
# 基本采用loc函数，第一个参数传入的是 index相关，第二个参数传入 的是 column name相关 df.loc[3,"lane"]
# 这两个参数还有几种拓展，可以是 一个列表 ["ego", "right"]  . 也可以是一段 闭区间 [4:5]


# 条件查询
# df.loc[df[""]]

