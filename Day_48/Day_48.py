arr_size = int(input("Enter size of array : "))
arr = list(map(int, input("Enter the elements of Array : ").split()))
li = []
print("After Removing Duplicate Elements in Array : ", end="")
for i in arr:
    if i in li:
        pass
    else:
        li.append(i)
        print(i, end=" ")
#print(li)