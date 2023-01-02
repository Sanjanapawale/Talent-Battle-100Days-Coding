arr_size1 = int(input("Enter the size of first Array: "))

# It takes each array element on new line
# arr1 = []
# print("Enter the elements of first array: ")
# for i in range(arr_size):
#     element = int(input())
#     arr1.append(element)

arr1 = list(map(int, input("Enter the elements of first array: ").split()))

arr_size2 = int(input("Enter the size of Second Array: "))

# It takes each array element on new line
# arr2 = []
# print("Enter the elements of Second array: ")
# for i in range(arr_size2):
#     element = int(input())
#     arr2.append(element)

arr2 = list(map(int, input("Enter the elements of first array: ").split()))
print()
if arr_size1 != arr_size2:
    print("Arrays are Not same.")
else:
    if arr1 == arr2:
        print("Both arrays are Same")
    else:
        print("Arrays are Not same")



