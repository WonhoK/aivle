#1
l = list(range(7,101,7))
print(l)
print()

#2
print(l[4])
print(l[5])
print(l[6])
print(l[7])
print()

#3
print(l[-3])
print()

#4
print(len(l))
print()

#5
print(sum(l))
print(sum(l)/len(l))
print()

#6
for i in range(2, 101):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check: print(f'{i} ', end = '')
print()
print()

#7
d = {'v1' : [1,2,3], 'v2' : {'a' : 23, 'b' : [4, 5]}}
print(d)
print()

#8
print(d['v1'])
print()

#9
print(d['v2']['a'])
print()

#10
print(d['v2']['b'][1])
print()

#11
d['newKey'] = (1, 2)
print(d['newKey'])
print()