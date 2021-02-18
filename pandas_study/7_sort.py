import pandas as pd

products = pd.read_excel("data/7.xlsx",index_col="ID")
print(products)
print("======================")
products.sort_values(by=["Worthy", "Price"], inplace=True, ascending=[True, False])
print(products)