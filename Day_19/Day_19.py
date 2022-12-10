num = int(input("Enter Number: "))
temp = num
num1 = num
digit = 0
while num != 0:
    num = num // 10
    digit += 1
arm = 0
while temp != 0:
        rem = temp % 10
        # print(rem)
        remo = 1
        for i in range(digit):
            remo *= rem
        arm += remo
        temp = temp // 10
if num1 == arm:
    print(num1, "is an Armstrong number.")
else:
    print(num1, "is not a Armstrong number.")