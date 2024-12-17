import os
os.system("cls")
def bankacc():
    print(f"\nWelcome to Kabayan Bank")
    print(f"Create account first to enjoy our service")
bankacc()
while bankacc:
    zapp = input("\nSelect an option: \n\n\t1 - Create an account \n\t2 - Withdraw \n\t3 Check Balance \n\t4 - Stop \n\nEnter your option: ").lower()
    if zapp == "1":
        name = input("\nEnter your name:  ")
        deposit = int(input(f"\nEnter amount to deposit: "))
        print(f"\nAccount for {name} has been created, with a deposit of {deposit} PHP")
        continue
    elif zapp == "2":
        withdraw = int(input("\nEnter the amount you want to withdraw:  "))
        deposit -= withdraw
        print(f"\nYou withdraw, {withdraw} PHP.")
        if withdraw > deposit:
            print("\nSorry you have Insufficient Balance.")
            break
        else:
            continue
    elif zapp =="3":
        print(f"\nYour current balance is {deposit}PHP.")
        a1 = deposit // 1000
        aa1 = deposit % 1000
        a2 = aa1 // 500
        aa2 = aa1 % 500
        a3 = aa2 // 200
        aa3 = aa2 % 200
        a4 = aa3 // 100
        aa4 = aa3 % 100
        a5 = aa4 // 50
        aa5 = aa4 % 50
        a6 = aa5 // 20
        aa6 = aa5 % 20
        a7 = aa6 // 10
        aa7 = aa6 % 10
        a8 = aa7 // 5
        aa8 = aa7 % 5
        a9 = aa8 // 1
        aa9 = aa8 % 1
        print("\nThe current balance of your account is: ")
        print("\n" , a1 ,"-  1000" , "\n" , a2 ,"-  500" , "\n" , a3 ,"-  200" , "\n" , a4 ,"-  100" ,"\n" , a5 ,"-  50" , "\n" , 6 ,"-  20" ,"\n" , a7 ,"-  10" , "\n" , a8 ,"-  5" ,"\n" , a9 ,"-  1\n")
        # print(f"Total balance--->{deposit}")
        continue
    elif zapp == "4":
        print(f"\nProgram terminated, Thank you for supporting our company.")
        break
    else:
        print("Invalid Choice, Please try again.")
        continue