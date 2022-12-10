num = int(input("Enter Number: "))
temp = num
add = 0
while num != 0:
    rem = num % 10
    num = num // 10
    add += rem
print("Sum of the digits of ", temp, "is", add)