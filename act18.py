tri = eval(input("Enter a number of triangle---> "))

for x in range (1, 6):
    for r in range (1 , tri + 1):
        for y in range (1 , x + 1):
            print("*", end=" ")
        for z in range (6, x, -1):
            print(" ",end=" ")
    print()