


def pang_hi():
    print("HI IT1C")

def pang_hi_v2(name):
    print(f"Hello {name}")

def termi():
    print("PROGRAM TERMINATED")

def activity_2():
    number1 = eval (input("enter a number--->" ))
    number2 = eval (input("enter another number--->" ))
    answer = (number1 + number2)
    print(f"The sum of {number1} and {number2} is {answer}")

tuloy =  True
while tuloy == True:
    ask = input("Enter a name---> ")

    if ask.lower() != "stop":
        pang_hi_v2(ask)
        if ask == "2":
            activity_2()
            continue
    else:
        termi()
        break