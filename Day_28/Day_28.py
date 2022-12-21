# string = input("Enter a String: ")
# print("Reverse of String:", string[::-1])

string = input("Enter String: ")
length = len(string)
for i in range(length-1, -1, -1):
    print(string[i], end="")
