char = input("Enter a Character: ")
if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' or char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("Vowel")
elif ((char >= 'A' and char <= 'Z') or  (char >= 'a' and char <= 'z')):
    print("Consonent");
else:
    print("Invalid Input");
