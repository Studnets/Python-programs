num_list = []
marker_0 = 0 
while marker_0 == 0:
	n = input("Type a multi-digit number:  ")    
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
#turns input to string and puts each digit into a list and sums the list
