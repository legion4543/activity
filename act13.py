sum = 1
num=int(input('Enter a number: '))

for x in range (num,0,-1):
    sum *= x
print(f"The factorial of {num} is {sum}")