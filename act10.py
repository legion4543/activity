isDLL= input('Are you a current student of DLL (yes/no):  ')

if isDLL.lower() == 'yes':
	print('Welcome to the DLL BSIT Scholarship form')
	isCotta= input('Are you from Barangay Cotta (yes/ no):  ')

	if isCotta.lower() == 'yes':
		print('Please fillup the second form')
		isLevel=input('What is your current level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer')
		if isLevel.lower() == 'f':
			print('Hi Freshmen')
		elif isLevel.lower() == 's':
			print('Hi Sophomore')
		elif isLevel.lower() == 'j':
			print('Hi Junior')
		elif isLevel.lower() == 'r':
			print('Hi Senior')
		else:
			print('Invalid choice')
		isNeeded = input('Do you need this scholarship (yes/no):  ')
	
		if isNeeded.lower() == 'yes':
			print('Scholarship Granted')
		else:
			print('Thanks for stopping by')
	else:
		print('Sorry, this Scholarship grant are only for resident of Cotta')

else:
	print('Thanks for stopping by')