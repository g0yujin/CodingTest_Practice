degree = int(input())

if degree < 0:
    print("ice")
elif degree >= 100:
    print("vapor")
else:
    print("water")