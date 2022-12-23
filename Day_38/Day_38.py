str1 = input("Enter a String: ")
for i in str1:
    if str1.count(i) > 1:
        pass
    else:
        print(i, end=" ")
