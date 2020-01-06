import math
messag = "dale's name"
print(messag.upper()[0:2])
print(len(messag))
print(messag.find('n'))

name = "dale"
age = 15
greeting = "hello "
print("{},{},{} welcome!".format(greeting, name, age))

cousrses = ["history", "PE", "math"]

cousrses.append("art")
print(cousrses)

cousrses.insert(1, "1")
cousrses.sort()
print(cousrses)
cousrses.remove("1")
print(min(cousrses))

ddlist = [5, 10, 15, 11]
mean = float(sum(ddlist))/float(len(ddlist))
print(mean)
hehe = ",".join(cousrses)

newlist = hehe.split(",", 1)
print(newlist)

squ = []

for it in range(0, 101, 10):
    squ.append(math.sqrt(it))

print(squ)
alist = list(range(1,10))
print(alist)

best = set()



student = {"name": "dale", "age":15, "courses": [1, 2, 3], 1: "index"}
print(student.get("name"))
print(student[1])
student.update({"name":"jane", "address": "ludj"})
print(student)

del student["age"]
print(student)

for key, value in student.items():
    print(key,value)



mystr = "dale is great"

mylist=list(mystr)
mylist.reverse()
print(mylist)
rev_str = "".join(mylist)
print(rev_str)