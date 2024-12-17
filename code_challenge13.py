# for x in range (6, 1, -1):
#     for z in range(x, 1, +1):
#         print(" ", end =" ")
#     for y in range(6, x, 1):
#         print(y, end =" ")
#     for j in range (x, 1, +1):
#         print(j, end =" ")
#     print()

# for x in range (1,7):
#     for y in range(6, x, - 1):
#         print(" ", end =" ")
#     for z in range(x, 1, -1):
#         print(z, end =" ")
#     for j in range (1, x + 1):
#         print(j, end =" ")
#     print()

for x in range (6, 1, -1):
    for y in range(x, 1, - 1):
        print(" ", end =" ")
    for z in range(x, 7, +1):
        print(z,end=" ")
    for j in range (x, 6, 1):
        print(j,end=" ")
    print()
        
for x in range (1,7):
    for y in range(1, x, 1):
        print(" ", end =" ")
    for z in range(7, x, -1):
        print(z,end=" ")
    for j in range (x, 6, +1):
        print(j,end=" ")
    print()