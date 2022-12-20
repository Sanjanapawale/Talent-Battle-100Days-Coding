string = input("Enter a String including number:")
count = 0
for i in string:
    if i.isdigit():
        count += int(i)
print(count)