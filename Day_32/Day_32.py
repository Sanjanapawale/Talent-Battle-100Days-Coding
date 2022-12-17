string = input("Enter a String: ")
for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        pass
    else:
        print(i, end="")

# string = input("Enter a String: ")
# vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
# result = ""
# for i in string:
#     if i not in vowels:
#         result += i
# print(result)