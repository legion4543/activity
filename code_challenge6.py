blck1 = eval(input("\nEnter your grades in Prelims ---> "))
blck2 = eval(input("\nEnter your grades in Midterms ---> "))
blck3 = eval(input("\nEnter your grades in Semi-Finals ---> "))
blck4 = eval(input("\nEnter your grades in Finals ---> "))
blck5 = eval(input("\nEnter your grades in Quizzes ---> "))
blck6 = eval(input("\nEnter your grades in Projects ---> "))

if (blck1 >= 65 and blck1 <=100) and (blck2 >= 65 and blck2 <=100) and (blck3 >= 65 and blck3 <=100) and (blck4 >= 65 and blck4 <=100) and (blck5 >= 65 and blck5 <=100) and (blck6 >= 65 and blck6 <=100):
	brtt = (blck1 * 0.15) + (blck2 * 0.15) + (blck3 * 0.15) + (blck4 * 0.15) + (blck5 * 0.25) + (blck6 * 0.15) 
	if brtt >= 75:
		print("\nCongratulations for passing the Semester ")
		print(f"\nThis is your grades for the Semester {brtt} ")
	else:
		print("\nYou failed for the Semester ")
		print(f"\nThis is your grades for the Semester {brtt} ")
else:
	print("\nINVALID GRADES")