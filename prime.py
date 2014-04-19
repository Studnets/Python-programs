from math import ceil

marker_0 = 0 
while marker_0 == 0:
	x = input("Type a number and i'll check if it's prime:  ")    
	if not x.isdigit():        
		print ('*Enter valid input')
	else:
	    x = int(x)
	    break

print ('processing...')
if x < 2:
    print (x, 'is not prime')
elif x % 2 == 0:
    print (x, 'is not prime')
elif x % 2 != 0:
    half_x = ceil((x/2))
    while marker_0 < half_x:
        if half_x == 1:
            print (x, 'is prime')
            break
        elif x % half_x == 0:
            print (x, 'is not prime')
            break        
        half_x = half_x - 1
else:
    print ('error')