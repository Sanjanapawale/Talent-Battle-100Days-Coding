num = int(input("Enter number: "))
a = 0
b = 1
print("Fibonacci series for ", num, " is:")
print(a, end=" ")
print(b, end=" ")
for i in range(0, num-2):
    c = a + b
    a = b
    b = c
    print(c, end=" ")
