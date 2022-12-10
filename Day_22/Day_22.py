num = int(input("Enter Number: "))
li =[]
for i in range(2, num):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        li.append(i)


for i in range(0, len(li)):
    for j in range(i, len(li)):
        add = li[i] + li[j]
        if num == add:
            print(num, "can be expressed as ", li[i], "+", li[j])


