### str object is immutable
# > a相当于是指向了不同的变量地址，地址中本身的变量值并没有改变
a="Dale"
print("address of a is {}".format(id(a)))  # out: address of a is 2285135483936
a="Bob"
print("address of a is {}".format(id(a)))  # out: address of a is 2285136261672

##### change a char of the str
# > since str obj is an immutable obj, you cant change a single char's content within a str obj.
# a[0]= "C" # TypeError: 'str' object does not support item assignment
#print(a)

### list object is mutable
# > a相当于是指向了不同的变量地址，地址中本身的变量值并没有改变
a=[1, 2, 5, 6]
print("address of a is {}".format(id(a)))  # out: 地址1
a=[2, 5, 7, 9]
print("address of a is {}".format(id(a)))  # out: 地址2
##### change a item value within a list
# > list obj 是mutable obj 因此可以改变某个地址中的变量的某个元素值，而并没有形成新的对象
a[2]=99
print(a)
print("address of a is {}".format(id(a)))  # out: 地址2

# https://www.youtube.com/watch?v=5qQQ3yzbKp8

print("---------------------")
### tuples object is immutable


# > tuples obj is immutable obj, so you cant change a single item within a tuple, but what you can do is to loop it and access each single item
a=(1, 2, 5, 6)
print("address of a is {}".format(id(a)))  # out: 地址1
a=(2, 5, 7, 9)
print("address of a is {}".format(id(a)))  # out: 地址2
##### change a item value within a list
# >
a[2]=99  #TypeError: 'tuple' object does not support item assignment


### tuples变量指向
# > a相当于是指向了不同的变量地址，地址中本身的变量值并没有改变
tuple1=(1,3,4,7,2)
tuple2=tuple1 # 将tuple类型变量变成list，则变量id也均指向同一地址
print("address of a is {}".format(id(tuple1)))  # out: 地址1
print("address of a is {}".format(id(tuple2)))  # out: 地址1
##### 修改tuple1的指向
# > tuple1 地址改变，而tuple2地址不变
tuple1=(1,2,6,3)
print("address of a is {}".format(id(tuple1)))  # out: 地址2
print("address of a is {}".format(id(tuple2)))  # out: 地址1