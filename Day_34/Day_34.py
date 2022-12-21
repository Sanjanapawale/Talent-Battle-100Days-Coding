import re
eqn = input("Enter an eqaution which includes paranthesis(): ")
for element in eqn:
    if element == '(' or element == ')':
        result = re.sub("[()]", "", eqn)
print(result)