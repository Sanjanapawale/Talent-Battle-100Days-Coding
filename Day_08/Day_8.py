import math
a, b, c = map(int, input("Enter 3 values for Quadratic Equation: ").split())
x1 = (-b + (math.sqrt((b*b)-4*a*c))) / (2*a);
x2 = (-b - (math.sqrt((b*b)-4*a*c))) / (2*a);
if x1 == x2:
    print("Roots are Equal \nRoot 1 = Root 2 = ", x1)
else:
    print("Roots are Not Equal \nRoot 1 =", x1, ",\tRoot 2 =",x2)   