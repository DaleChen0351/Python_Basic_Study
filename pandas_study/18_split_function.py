import pandas as pd
import os

em = pd.read_excel("data/18.xlsx",index_col="ID")
df = em["Full Name"].str.split(expand=True) # expand:分成两个series # n=2, 保留最多两个 # “symbol”，默认是空格和tab
em["First Name"] = df[0]
em["Last Name"] = df[1]
print(em)
print("======================")
print(em["First Name"].str.upper())


# path split
path = "/home/cda5szh/data/fusion.csv"
ret = os.path.split(path)
print(ret)  # ('/home/cda5szh/data', 'fusion.csv')
