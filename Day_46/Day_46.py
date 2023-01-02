arr_size = int(input("Enter the size of Array: "))
arr = list(map(int, input("Enter the elements of array: ").split()))
add = 0
for i in arr:
    add += i
print("Addition of the Array elements: ", add)
#print(sum(arr))