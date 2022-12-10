num = int(input("Enter Number: "))
temp = num
def factorial(digit):
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    return fact

sum = 0
while num != 0:
    rem = num % 10
    num = num // 10
    sum += factorial(rem)

if temp == sum:
    print(temp, "is an Strong Number.")
else:
    print(temp, "is Not an Strong Number")