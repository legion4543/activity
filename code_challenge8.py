sum = 0
odd = 0
even = 0

for j in range(1,11):
    num = int(input(f"\nEnter a Number {j}:  "))
    sum += num 
    if num % 2 == 0:
        odd+=num
    else:
        even+=num

print(f"\nThe sum of all given numbers is {sum}")
print(f"\nThe even of all given numbers is {even}")
print(f"\nThe odd of all given numbers is {odd}")
