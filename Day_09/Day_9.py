num = int(input("Enter Number: "))
digit = 0
temp = num
while num > 0:
    num = num // 10
    digit += 1
print("The number of digits in ", temp, " is ", digit)
