#num = int(input("Enter Number: "))
# num2 = 0
# if num == 0:
#     num2 = 1
# while num != 0:
#     rem = num % 10
#     if rem == 0:
#         rem = 1
#     num = num // 10
#     num2 = (num2*10)+rem
#
# rev = 0
# while num2 != 0:
#     rem = num2 % 10
#     num2 = num2 // 10
#     rev = (rev*10)+rem
# print(rev)
# str_num = str(num)
# print(type(str_num))
# for i in str_num:
#     if i == '0':
#         i=1
# print(str_num)

# num = int(input("Enter Number: "))
# li = str(num)
# CNum = "";
# for i in range(0, len(li)):
#     if li[i] == '0':
#         print(CNum.join('1'), end="")
#     else:
#         print(CNum.join(li[i]), end="")

num = int(input("Enter Number: "))
li = str(num)
CNum = "";
for i in range(0, len(li)):
    if li[i] == '0':
        CNum += '1'
    else:
        CNum += li[i]

print(CNum)
