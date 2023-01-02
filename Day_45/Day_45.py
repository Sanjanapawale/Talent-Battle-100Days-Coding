arr_size = int(input("Enter the size of array: "))
arr = list(map(int, input("Enter the Array elements: ").split()))

# print("Smallest number of array: ", min(arr))
# print("Smallest number of array: ", max(arr))
for i in range(arr_size):
    for j in range(i, arr_size):
        if arr[i] <= arr[j]:
            pass
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print()
print("Smallest Number in Array: ", arr[0])
print("Largest Number in Array: ", arr[-1])