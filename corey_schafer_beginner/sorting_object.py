li = [9, 4, 5, 6, 2, 1, 3, 7, 8]
# sorted ：return a new list
s_li = sorted(li)
print("sorted li\t", s_li)
print("origin li\t", li)
# 不用新建一个变量,直接改变list本身
li.sort()  # return a None
print("list_sorted\t", li)
# reverse = True
print("reverserd li\t", sorted(li, reverse=True))

# tup
tup = [9, 4, 5, 6, 2, 1, 3, 7, 8]
print("tup\t",sorted(tup))
# dict
di = {"name": "cale", "job": "programming", "age": "none", "os": "mAC",}
s_di = sorted(di)
print("默认排序Dict\t",s_di)

def get_value(dii):
    retlist=[]
    for key, value in dii.items():
        retlist.append(value)
    return retlist

s_di_value = sorted(get_value(di))
print(s_di_value)

# 接下来的视频将会使用sorted函数，基于其他类型的变量

li2= [-6, -5, -4, 1, 2, 3]
s_li2 = sorted(li2)
print(s_li2) # 整数排序
s_li3 = sorted(li2, key=abs)
print(s_li3)