string = input("Enter a String: ")
for i in string:
    if i.islower():
        upper = i.upper()
        print(upper, end="")
    else:
        lower = i.lower()
        print(lower, end="")
