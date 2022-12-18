str1 = input("Enter a string: ")
str2 = str1[::-1]
if str1 == str2:
    print(str1, "is a Palindrome string.")
else:
    print(str1, "is not a Palindrome string.")