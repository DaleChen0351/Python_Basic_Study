import pandas as pd

pd.options.display.max_columns=999


videos = pd.read_excel("data/summary.xlsx", sheet_name="transform",index_col="Month")
print(videos)
print("===============")
print(videos.transpose())
