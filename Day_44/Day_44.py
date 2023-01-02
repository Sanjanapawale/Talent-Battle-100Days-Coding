arr_size = int(input("Enter size of Array: "))
arr = list(map(int, input("Enter elements of array: ").split()))
even = 0
odd = 0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of Even elements: ", even)
print("Number of Odd elements: ", odd)