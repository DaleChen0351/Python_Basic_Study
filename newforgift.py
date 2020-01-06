
type = [90, 135, 223, 426, 720]
print(type)

sum = 8407
for a in range(0, sum//type[0]):
    for b in range(0, sum // type[1]):
        for c in range(0, sum // type[2]):
            for d in range(0, sum // type[3]):
                for e in range(0, sum//type[4]):
                    if a * type[0] + b*type[1] + c*type[2] + d*type[3] + e*type[4] == sum:
                        if a and b and c and d and e:
                            print(a, b, c, d, e)

