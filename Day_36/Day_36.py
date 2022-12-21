str1 = input("Enter a string: ")
str2 = str1.capitalize()
last_letter = str2[-1].upper()
str3 = ""
for i in range(len(str2)-1):
    str3 += str2[i]
print(str3+last_letter, end="")


