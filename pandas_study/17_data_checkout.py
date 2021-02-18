import pandas as pd
# 数据校验-> 清理 -> 替换
# pandas axis  0-up to down  1-left to right
students = pd.read_excel("17.xlsx")

# try and catch
def score_validation(row):
    try:
        assert 0<=row.Score<=100
    except:
        print(f'#{row.ID}\t student {row.Name}\t has an invalid score {row.Score}.')
# if and else
def score_validation2(row):
    if not 0<=row.Score<=100:
        print(f'#{row.ID}\t student {row.Name}\t has an invalid score {row.Score}.')


students = pd.read_excel("17.xlsx")
students.apply(score_validation2, axis=1)