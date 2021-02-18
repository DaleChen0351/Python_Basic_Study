import pandas as pd

students = pd.read_excel("data/19.xlsx", index_col="ID")
print(students)

# row total and average
temp = students[["Test_1", "Test_2", "Test_3"]]
row_sum = temp.sum(axis=1) # 默认是axis =0 ，only axis=1, left to right
row_mean = temp.mean(axis=1)
print(row_sum)
students["Total"] = row_sum
students["Mean"] = row_mean

# list average(mean)
col_mean = students[["Test_1", "Test_2", "Test_3", "Total", "Mean"]].mean() # 默认axis=0，up to down mean
col_mean["Name"] = "Summary"
students = students.append(col_mean,ignore_index=True) # row added, ignore_index=True
print(students)

# max and min corr
