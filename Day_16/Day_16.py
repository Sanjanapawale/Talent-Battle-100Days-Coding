num = int(input("Enter Number: "))
li = []
for i in range(1,num):
    if num % i == 0:
        li.append(i)
if num == sum(li):
    print(num, "is a Perfect Number.")
else:
    print(num, "is not an Perfect Number.")