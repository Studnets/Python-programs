#Test page
#Goal: Fibonacci sequence
#Method: idfk just fuck around with shit until it works
#New Method: 
#	-Make equation to create fib sequence 
#	-Limit sequence with range function
'''
'''


def fibsequence(n):
	a, b = 0, 1
	for i in range(n):
		yield a
		a, b = b, b + a
d = int(input("range:"))
for i in fibsequence(d):
	print (i)
print ("end program?")
a = input(">>>")