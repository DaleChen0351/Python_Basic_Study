

courses = ["history", 'PE', "$", 'math', 'comsci']
courses_2 = ['english', 'chinese']
num=[2, 1, 3, 5, 4, 9]
### slice
print(courses[:2])  # 前闭后开
print(courses[-1])  # comsci slicing  https://www.youtube.com/watch?v=ajrtAuDg3yw
print(courses[-2])  # math

### add items
courses.append("art")  # 在最后位置增加
courses.extend(courses_2)  # 将两个list合并
### insert items
courses.insert(1, "IT")  # 1: 将会插入的绝对位置   IT将会是list中的第二个元素

### remove item
courses.remove("PE")
### POP
poped=courses.pop()  # 将list中的最后一个元素弹出到返回值 chinese
print(courses)

### 倒序打印
courses.reverse()  # 将原list的元素顺序进行了永久改变，如果需要恢复到原始list，可随时再次调用reverse函数
print(courses)
### 升序排序
courses.sort()  # 默认按照ASCII码顺序升序排列 out：['$', 'IT', 'art', 'comsci', 'english', 'history', 'math']
### 降序排序
courses.sort(reverse=True)  # out:['math', 'history', 'english', 'comsci', 'art', 'IT', '$']
num.sort(reverse=True)  # out: [9, 5, 4, 3, 2, 1]

### 原数组不变排序
new=sorted(courses, reverse=True)  # 采用系统内置函数
### 类似内置函数
print(min(num))
print(min(courses)) # 通过比较元素首字母的ASCII码值
print(sum(num))

### get index
print(courses.index("IT"))

### 检查某个元素是否在某个列表中
print("$" in courses)  # bool ret value

### enumerate
for index, value in enumerate(courses, start=1):
    print(index, value)

### list to str
courses_str=", ".join(courses)  # join函数可以将list中的每个元素按照顺序串联起来，且在元素之间添加任意连接字符
print(courses_str)  # out：math, history, english, comsci, art, IT, $
### str to list
##### 全部分割
newlist = courses_str.split(", ")  # split 函数 out：['math', 'history', 'english', 'comsci', 'art', 'IT', '$']
##### 分割N次
newlist = courses_str.split(", ", 1)  # split 函数将原始字符串分割了一次，形成前后两个部分 len=2的list
print(newlist)

# set
cs_courses = {'history', "math", "phy", "computer"}
art_courses = {'history', "math", "art", "design"}

### 无法保存多个相同的元素

### 求两个set的交集 合集 差集
# > 只有set才有的内置函数，list和tuple均没有
print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))
print(cs_courses.difference(art_courses))

### build a empty obj
##### list
alist = []
blist = list()
##### tuple
atuple = ()
btuple = tuple()
##### set
aset = {}  # 这是dict的初始化方式
bset = set()  # 这才是set的初始化方式

### question
# > set 和 dict的区别是什么呢？
