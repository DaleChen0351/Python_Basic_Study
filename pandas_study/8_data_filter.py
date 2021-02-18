import pandas as pd



# funct
def greater_than_80(s):
    return 80< s <=100

# lambda


if __name__ == "__main__":
    students = pd.read_excel("8.xlsx", index_col="ID")
    print(students)
    print("==============")
    # loc = locate 定位（attribute）? input  yes or no ?
     # way 1:
    # students = students.loc[students["Score"].apply(greater_than_80)].loc[students.Age.apply(lambda a: 18<= a <23)]
     # way 2:
    mask = students["Score"].apply(greater_than_80) & students["Age"].apply(lambda a:18 <= a < 23)
    students = students.loc[mask]


    print(students)