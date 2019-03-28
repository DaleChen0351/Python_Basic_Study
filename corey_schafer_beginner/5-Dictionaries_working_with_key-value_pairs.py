
student = {'name': 'Dale', "age": 18, "courses": ["math", "science"], 1: "index"}
### access
print(student[1])  # key值可以使字符串，也可以是数字
print(student["name"])
print(student.get("courses"))
print(student.get("phone", "Not Found"))  # get不存在的key值，会返回None，可通过传入第二个参数来指定key值不存在时的return value
# print(student["live"])  # 如果不使用get函数，则会出现 **KeyError: 'live' **

### dict的updata函数
student.update({"name": "Jane", "age": 28, "phone": "133333"})  # 可以增加key-value键值对，也可以修改已有的键值对
print(student)  # out: {'name': 'Jane', 'age': 28, 'courses': ['math', 'science'], 1: 'index', 'phone': '133333'}

### del 函数
del student["age"]
print(student)  # {'name': 'Jane', 'courses': ['math', 'science'], 1: 'index', 'phone': '133333'}
### pop
ret=student.pop("phone")
print(ret)  # out: 133333
print(student)  # out: {'name': 'Jane', 'courses': ['math', 'science'], 1: 'index'}

### key, value, items
print(student.items())  # dict_items([('name', 'Jane'), ('courses', ['math', 'science']), (1, 'index')])
student.keys()
student.values()
for key, value in student.items():
     print(key, value)

# name Jane
# courses ['math', 'science']
# 1 index

### 特殊的一个例子
test = [['name', 'Jane', 1], ['courses', ['math', 'science'], 2], [1, 'index', 3]]
for index, value, emp in test:
    print(index, value, emp)
# out
# name Jane 1
# courses ['math', 'science'] 2
# 1 index 3

