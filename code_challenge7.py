name = input("\nEnter your name ---> ")
grocery = input("\nDid you buy a grocery? (yes/no) ---> ")
if grocery.lower() == "yes":

	item = input("\nName of the item ---> ")
	price = eval(input("\nPrice of the item ---> "))
	amount = eval(input("\nExact amount given ---> "))
	age = eval(input("\nAge ---> "))
	
	tax = 0.123
	ttm = price * tax
	total = price + ttm
	
	if age <= 59:
		change = amount - total

		print(f"\nHi {name} you purchased a {item} , with a price of {price} plus 12.3% of tax ({ttm}) total of ({total}) ")
		print(f"\nAmount given ---> ({amount})php ")
		print(f"\nChange ---> [round(change , 2)] ")
		print("\nThank you for shopping! ")

	if age >= 60:	
		discount = 0.052
		ddm = price * 0.052
		dtotal = price - ddm
		cchange = amount - dtotal

		print(f"\nHi {name} you paid a price of {price}, for an {item} with a discount of 5.2% ({ddm}). The total amount you paid is (round{dtotal , 2}) ")
		print(f"\nAmount given ---> ({amount})php ")
		print(f"\nChange ---> {cchange} ")
		print("\nThank you for shopping! ")
	
	
else:
	print("\nThank you for checking in")	