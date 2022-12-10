def GCD(num1, num2):
    if num1 == num2:
        return num1
    else:
        if num1 > num2:
            greater = num1
        else:
            greater = num2
        li = []
        for i in range(1, (greater // 2)+1):
            if num1 % i == 0 and num2 % i == 0:
                li.append(i)
        return li[-1]

x1, y1 = map(int, input("Enter numerator and denominator for 1st number: ").split())
x2, y2 = map(int, input("Enter numerator and denominator for 2nd number: ").split())
x3 = (x1 * y2) + (x2 * y1)
y3=(y1*y2)
gcd = GCD(x3, y3)
numerator = x3 // gcd
denominator = y3 // gcd
print("Addition of 2 fractions =",numerator,"/",denominator)