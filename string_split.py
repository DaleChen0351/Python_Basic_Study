import pandas as pd
ret = []
with open("JoyceData.txt", encoding='utf-8', mode= 'r') as f:
    for line in f:
        mylist = line.split()
        print(mylist)
        ret.append(mylist)


    csv_data = pd.DataFrame(data = ret)
    csv_data.to_csv('csv_out.csv', encoding="gbk")