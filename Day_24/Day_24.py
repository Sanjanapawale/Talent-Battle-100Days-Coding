num = int(input("Enter a number to print star pyramid: "))
star_no = 1
for i in range(num):
    print(star_no*"*")
    star_no += 2

# num = int(input("Enter a number to print star pyramid: "))
# star_no = 1
# for i in range(num, 0, -1):
#     # for j in range(5, 1, -1):
#     print(i*" ", star_no*"*")
#     star_no += 2
