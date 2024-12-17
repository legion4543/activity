lname = input("\nType your last name ---> ")
fname = input("\nType your first name ---> ")
mname = input("\nType your middle name ---> ")

prtt1 = eval(input("\nAmount to deposit ---> "))

blck1 = prtt1 // 1000
brtt1 = prtt1 % 1000

blck2 = brtt1 // 500
brtt2 = brtt1 % 500

blck3 = brtt2 // 200
brtt3 = brtt2 % 200

blck4 = brtt3 // 100
brtt4 = brtt3 % 100

blck5 = brtt4 // 50
brtt5 = brtt4 % 50

blck6 = brtt5 // 20
brtt6 = brtt5 % 20

blck7 = brtt6 // 10
brtt7 = brtt6 % 10

blck8 = brtt7 // 5
brtt8 = brtt7 % 5

blck9 = brtt8 // 1
brtt9 = brtt8 % 1

print("\nHello", fname , mname , lname ,"this is the breakdown of your deposit: \n")
print(blck1 ," - 1000")
print(blck2 ," - 500")
print(blck3 ," - 200")
print(blck4 ," - 100")
print(blck5 ," - 50")
print(blck6 ," - 20")
print(blck7 ," - 10")
print(blck8 ," - 5")
print(blck9 ," - 1")