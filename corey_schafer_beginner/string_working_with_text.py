
message_double="Dale's world"
#print(message_double)

message_slash='dale\'s world'
#print(message_slash)

message_single='"dale"'
#print(message_single)

print(message_double[0:5])
print(len(message_double))

print(message_double.upper())
print(message_double.count('Dale'))
print(message_double.find('w'))


message_replace="dale dale dale,hello!"
print(message_replace.replace('dale',' ',message_replace.count('dale')-1))

greeting="hello"
name='dale'
age=15
print(greeting+', '+ name +'. welcome!')
print("{}, {}{}.welcome!".format(greeting,name,age))# https://youtu.be/k9TUPpGqYTo?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
print(f'{name.upper()} is a boy')

print(help(str))