num = int(input("Enter Number: "))
temp = num
rev = 0
while num != 0:
    rem = num % 10
    num = num // 10
    rev = (rev*10) + rem
if rev == temp:
    print(temp, "is a Palindrome.")
else:
    print(temp, "is not a Palindrome.")