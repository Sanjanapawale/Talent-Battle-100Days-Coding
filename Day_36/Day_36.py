Str1 = input('Enter a string: ')
Str1 = Str1[0:1].upper() + Str1[1:len(Str1)-1] + Str1[len(Str1)-1:len(Str1)].upper()
print(Str1)

# str1 = input("Enter a string: ")
# str2 = str1.capitalize()
# last_letter = str2[-1].upper()
# str3 = ""
# for i in range(len(str2)-1):
#     str3 += str2[i]
# print(str3+last_letter, end="")


