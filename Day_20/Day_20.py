num = int(input("Enter Number: "))
if num == 1:
    print("1 is not a prime number.")
else:
    for i in range(2, (num // 2) + 1):
        count = 0
        if num % i == 0:
            count += 1
    if count != 0:
        print(num,"is not a prime number.")
    else:
        print(num,"is a prime number.")



