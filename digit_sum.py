marker_0 = 0
while marker_0 == 0:
	num_list = []
	marker_1 = 0 
	while marker_1 == 0:
		n = input("Type a multi-digit number, and i'll calculate its digit-sum:  ")    
		if not n.isdigit():        
			print ('*Enter valid input')
		else:  
			break
	#^Checks if digit
	j = 0
	n = str(n)
	print ('calculating sum...')
	for i in n:
	    num_list.append(i)
	for i in num_list:
	    i = int(i)
	    j = i + j
	print (j)
####################################################################################################################	
	marker_2 = 0
	marker_3 = 0
	while marker_2 == 0:
		repeat = input("Would you like to find another integers digit-sum? (y/n) ")    
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
#turns input to string and puts each digit into a list and sums the list
