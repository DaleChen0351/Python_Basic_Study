import pandas as pd

em = pd.read_excel("data/18.xlsx",index_col="ID")
df = em["Full Name"].str.split(expand=True) # expand:分成两个series # n=2, 保留最多两个 # “symbol”，默认是空格和tab
em["First Name"] = df[0]
em["Last Name"] = df[1]
print(em)
print("======================")
print(em["First Name"].str.upper())
