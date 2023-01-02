def isPalindrome(num):
    temp = num
    rev = 0
    while num != 0:
        rem = num % 10
        num = num // 10
        rev = (rev*10) + rem
    if rev == temp:
        return temp


arr_size = int(input("Enter size of array : "))
arr = list(map(int, input("Enter elements of array : ").split()))
palindrome = []
for i in arr:
    if isPalindrome(i):
        palindrome.append(i)


for i in range(len(palindrome)):
    for j in range(i, len(palindrome)):
        if palindrome[i] >= palindrome[j]:
            Max = palindrome[i]

print("Longest Palindrome in the Array : ", Max)
#print(max(palindrome))