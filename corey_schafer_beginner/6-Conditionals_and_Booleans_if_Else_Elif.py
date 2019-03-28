


# if else elif statement
# > Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is
# > 在python中没有switch结构，因为if else 及 elif已经足够表达清楚条件结构的逻辑了。
language = "Java"
if language == "Python":
    print("the language is Python")
elif language == "Java":
    print("the language is Java")
elif language == "JS":
    print("the language is JS")
else:
    print("No match")

# and or not key-words
### and
# > and 关键字两边的条件都是true后，才会执行if语句中包含的代码，只要有一个条件不满足，则会执行else中包含的代码。
user = "admin"
logged_in = True
if user == "admin" and logged_in:
    print("admin page")
else:
    print("bad Credit")  # out：admin page

### or
# > or 关键字两边的条件任意一边为true，则会执行if语句中包含的代码，只有两边条件都不满足时，才会执行else中包含的代码。
user = "admin"
logged_in = False
if user == "admin" or logged_in:
    print("admin page")
else:
    print("bad Credit")  # out：admin page

### not
user = "admin"
logged_in = False
# > not关键字将后边条件中的false变成了true，而满足了if的执行条件。为方便理解，也可认为，当想执行if not statement所包含的代码时，需要保证后边的条件语句为**false**
if not logged_in:
    print("please log in")
else:
    print("welcome")



# "is" equal "==" ?
# > "=="判断的是其两边的对象的值是否相等，如果相等则返回True。
# > 而"is"关键字判断的是其两边的对象是否指向同一片内存区域(是否在内存中是同一个id（资源）)。
### a和b分别赋值
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))  # out: 地址1
print(id(b))  # out：地址2
print(a == b)  # out: True
print(a is b)  # out: False
# a is b相当于：
print(id(a) == id(b))  # out: False

### d = c
c = [4, 5, 6]
d = c
print(id(c))  # out: 地址1
print(id(d))  # out: 地址1
print(c == d)  # out: True
print(c is d)  # out: True
# c is d相当于：
print(id(c) == id(d))  # out: True


# False Values:
# > 下面是条件结构中 认为 等同于 "False"的情况，除了这些情况之外的情况，都认为是"True"
### None
condition = None
if condition:
    print("True")
else:
    print("False")
### Zero of any numeric type
condition = 0.0
if condition:
    print("True")
else:
    print("False")
### Any empty sequence. For example, '', (), [].
condition1 = ""
condition2 = ()
condition3 = []
if condition1 or condition2 or condition3:
    print("True")
else:
    print("False")
### Any empty mapping. For example, {}.
condition = {}
if condition:
    print("True")
else:
    print("False")



# https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=7&t=0s
