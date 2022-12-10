num = int(input("Enter Number: "))
temp = num
rev = 0
while num != 0:
    rem = num % 10
    rev = (rev*10)+rem
    num = num // 10
print("Reverse number of the ",temp, "is", rev)