#Checks input to see if input is integer, float, or character
integer = []
floats = []
not_number = []
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
full_list = ['100', '234', 'random', '5.23', '55.55', 'random2']

for i in full_list:
	i = str(i) 
	length = len(i)
	count = 0 
	marker = 0
	for j in i:
		for k in digits:
			if k == j:
				count = count + 1
				#k loops through digits to see if j single character 
				#string input is number			
		if count == length:
			integer.append(i)
			marker = 1
		if j == '.':
			floats.append(i)
			marker = 1
			#Once '.' is found, input is "considered" a float
		if marker == 1:
			break
	else:
		not_number.append(i)
		#If code above else proves that input is not a number the 
		#only result is that it isn't a number
print ('Integers: ', integer)
print ('Float: ', floats)
print ('Not Numbers', not_number)








'''
my_file = [100, 3.00, 101, 3.14]
i = ''
for i in my_file:
	i = str(i)
	j = ''
	length_i = len(i)
	for j in i:
		count_0 = 0
		while count_0 < length_i:
			if j == '.':
				print ("FLOAT")
				break
			count_0 = count_0 + 1
		count_1 = 0
		while count_1 < length_i:
			try:
				j = (int(j))
				print ("INTEGER")
				break
			except ValueError:
				print ("FLOAT")
				break
			count_1 = count_1 +1 

'''




'''
length = len(my_file)

i = ''
marker = False
for i in my_file:
	for j in str(i):
		
		if j >= 0 or j < 0:	
			marker = True
		elif j == '.':
				print (i, " is a FLOAT")
	for k in str(i):
		if marker == True:
			break
		try:
			print (int(i), ' is an INTEGER')
		except ValueError or AttributeError:
			print (i, " is a Character")
'''
	
	
	
	



print ("DONE")