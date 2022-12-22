str1=input('Enter an algebraic equation: ')
str2=''
for i in str1:
    if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
        pass
    else:
        str2=str2+i
print(str2)


# import re
# eqn = input("Enter an eqaution which includes paranthesis(): ")
# for element in eqn:
#     if element == '(' or element == ')':
#         result = re.sub("[()]", "", eqn)
# print(result)
