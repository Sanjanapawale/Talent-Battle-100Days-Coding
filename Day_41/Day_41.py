def check_string(str1, str2):
    str1_size, str2_size = len(str1), len(str2)
    if str1_size == 0 and str2_size == 0:
        return True
    if (str1_size > 1 and str1[0] == '*') and str2_size == 0:
        return False
    if (str1_size > 1 and str1[0] == '?') or (str1_size != 0 and str2_size !=0 and str1[0] == str2[0]):
        return check_string(str1[1:], str2[1:])
    if str1_size != 0 and str1[0] == '*':
        return check_string(str1[1:], str2) or check_string(str1, str2[1:])
        return False

str1 = input('Enter string with wild characters: ')
str2 = input('Enter string without wild characters: ')
if check_string(str1,str2):
    print("Strings are matching")
else:
    print("Stings are not matching")
