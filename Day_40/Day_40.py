import re
str1 = input("Enter a String : ")
str2 = input("Enter the substring to be removed : ")
str3 = input("Enter the new substring : ")
# result = re.sub(str2, str3, str1)
# print("The new String : ", result)
result = str1.replace(str2, str3)
print("The new String : ", result)