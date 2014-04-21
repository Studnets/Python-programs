marker_0 = 0
while marker_0 == 0:
	marker_1 = 0 
	while marker_1 == 0:
		x = input("Type an integer and i'll calculate its factorial:  ")    
		if not x.isdigit():        
			print ('*Enter valid input')
		else:
		    x = int(x)
		    break
	#Checks valid input
	print ("Processing...")
	while marker_1 == 0:
		if x < 0:
			print ("Error: No negative factorials")
			break
		if 0 <= x < 2:
			print (1)
			break
		elif x >= 2:
			length_x = x
			marker_1 = 1
			while marker_1 < length_x:
				x = x * (length_x - marker_1)
				marker_1 = marker_1 + 1
			break
			#define x as separate value (length_x) so -1 decrement doesn't 
		#affect multiplicative sum 
	print (x)
#####################################################################################################################
	marker_2 = 0
	marker_3 = 0
	while marker_2 == 0:
		repeat = input("Would you like to find another integers factorial? (y/n) ")    
		if repeat == "y" or repeat == "yes":
			break
		elif repeat == "n" or repeat == "no":
			marker_3 = 1
			break
		else:
			print ("*Enter valid input")
	if marker_3 == 1:
		print ("Closing...")
		break
