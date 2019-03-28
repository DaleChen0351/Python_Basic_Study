

# for loop
# > iteration迭代器依次指代列表中的元素。*break* statement 会立即结束for循环
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found")
        break
    print(num)
# out：
# 1
# 2
# Found

# > *continue* statement 会立即结束本次循环，跳转到iteration指代的下个元素（skip to next iteration）
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num)  # 如果"3"被找到了，则会跳过本次循环，不会打印出“3”。
# out：
# 1
# 2
# Found
# 4
# 5

# > 通过for循环产生序列数
for i in range(1, 11):
    print(i)

# while
# > while 后面的条件不为True时，或者在语句中遇到break statement的时候才会停止循环
### 结束条件
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

### infinite loop
# > 如果在程序执行中遇到了死循环，大部分的终端都可以通过Ctrl+C结束循环。
# while True:
#     print(x)
#     x += 1

c.NotebookApp.ip='*'
c.NotebookApp.password = u'sha1:a892f228a800:45b9ec8332e071e755a9ea46d13d12b6c545bc6b'
c.NotebookApp.open_browser = False
c.NotebookApp.port =8888





