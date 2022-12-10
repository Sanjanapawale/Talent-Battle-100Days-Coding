x, y = map(int, input("Enter Values for X and Y: ").split())
if x > 0 and y > 0:
    print("This point lies in first quadrant.")
elif x < 0 and y > 0:
    print("This point lies in second quadrant.")
elif x < 0 and y < 0:
    print("This point lies in Third quadrant.")
else:
    print("This point lies in fourth quadrant.")