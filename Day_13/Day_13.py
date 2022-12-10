num = int(input("Enter Number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print("Sum of 1st", num, "natural number is ", end=" ")
sum = sum
for j in range(1, num):
    print(j, "+", end=" ")
print(num, "=", sum)
