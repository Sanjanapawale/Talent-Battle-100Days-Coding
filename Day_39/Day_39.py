str1, str2 = input("Enter a String: ").split()
if len(str1) != len(str2):
    print(str1, "and", str2, "are not Anagram")
else:
    if sorted(str1.lower()) == sorted(str2.lower()):
        print(str1, "and", str2, "are Anagram")
    else:
        print(str1, "and", str2, "are not Anagram")
