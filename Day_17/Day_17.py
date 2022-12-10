num = int(input("Enter Number: "))
print("Factors of ", num, "are : ", end="")
for i in range(1, num):
    if num % i == 0:
        print(i, end = ", ")
print(num)