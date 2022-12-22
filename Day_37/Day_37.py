str = input("Enter a String: ")
li = list(set(str))
li.sort()
for i in range(len(li)):
    count = 0
    for j in str:
        if li[i] == j:
            count += 1
    print("Frequency of", li[i], "is", count)
