marker_0 = 0 
while marker_0 == 0:
	x = input("Type a number and i'll calculate its factorial:  ")    
	if not x.isdigit():        
		print ('*Enter valid input')
	else:
	    x = int(x)
	    break
#Checks valid input


while marker_0 == 0:
    if x < 0:
        print ('Error, no negative factorials')
    elif 0 <= x < 2:
        print ('1')
        break
    elif x >= 2:
        length_x = x
        marker_0 = 1
        while marker_0 < length_x:
            x = x * (length_x - marker_0)
            marker_0 = marker_0 + 1
        break
        #define x as separate value (length_x) so -1 decrement doesn't 
		#affect multiplicative sum 
print (x)