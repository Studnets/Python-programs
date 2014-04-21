#Euler120
#Python


#Much simpler version
'''
total = 0
beg = 3
end = 1000

while beg < end:
    total += 2 * beg * ( ( beg - 1 ) // 2 )
    beg = beg + 1

print (total)
'''



#N value set

print ("Project Euler 120")

marker_0 = 0
while marker_0 == 0:
	n = input("Set N value:  >")    
	if not n.isdigit():        
		print ('*Enter valid input')
	else:  
		n = int(n)
		break


#a value set
while marker_0 == 0:
	a = input("Beginning 'a':  >")    
	if not a.isdigit():        
		print ('*Enter valid input')
	else:  
		a = int(a)
		break

while marker_0 == 0:
	end = input("Ending 'a':  >")    
	if not end.isdigit():        
		print ('*Enter valid input')
	else:  
		end = int(end)
		break
#------------------

max_list = []
print ("Calculating Max's")
while a <= end:
	#result calculations
	#Equation looped for all 'n' and all results put into 'list'
	i = 0
	max = 0
	while i < n:
		r = ((a-1)**i + (a+1)**i) % a**2
		if r > max:
			max = r
		i = i + 1
	max_list.append(max)
	a = a + 1
 
print ("Calculating Sum")
sum = 0	
for i in max_list:
	sum = i + sum

print (sum)




