#python binary string
import random
def rand_bin(inp):
	count = 0
	bin_list = []
	while count < inp:
		a = random.randint(0, var-1)
		if a==0:a='a'
		if a==1:a='b'
		if a==2:a='c'
		if a==3:a='d'
		if a==4:a='e'
		bin_list.append(a)
		count = count + 1
	#print (bin_list)
	for i in bin_list:
		print (i, end='')
	return(bin_list, inp)
	
#enter you're own binary string
'''
bin_list = []
inp = str(input("Length of binary string: "))
for i in inp:
	bin_list.append(i)
'''
def compress(bin_list):
	count = 0
	comp_list = []
	while count < len(bin_list):
		begin = bin_list[count]
		comp_list.append(begin)
		count2 = 1
		while count+count2 < len(bin_list):
			finish = bin_list[count+count2]
			if begin == finish:
				None
			elif begin!=finish:
				if count2>2:
					comp_list.append(count2)
				elif count2==1:
					None
				elif count2==2:
					comp_list.append(begin)
				break
			count2 = count2+1
		count = count+count2
	if count2>2:
		comp_list.append(count2)
	if count2==1:
		None
	if count2==2:
		comp_list.append(begin)
	comp_list_len = len(comp_list)
	#print (comp_list)
	for i in comp_list:
		print (i, end='')
	return (comp_list, comp_list_len)
def expand(comp_list, comp_list_len):
	expand_list = []
	count = 0
	while count<comp_list_len:
		expand_list.append(comp_list[count])
		try:
			a=int(comp_list[count+1])
			if a>2:
				while a-1!=0:
					expand_list.append(comp_list[count])
					a = a - 1
				count=count+1
		except:
			None
		count = count+1
	#print (expand_list)
	for i in expand_list:
		print (i, end='')
	return (expand_list, len(expand_list))
#^Functions Above
print("Compression 1")
a=False
while True:
	var = input("Number of Variables (5 max): ")
	try:
		var = int(var)
		if var<=5:
			a = True
		elif var>5:
			print ('less than 5')
	except:
		print ('*int')
	if a==True:
		break
while True:
		inp = input("Length of random string: ")
		try:
			inp = int(inp)
			break
		except:
			print("*integer*")
bin_list, bin_list_len = rand_bin(inp)
while True:
			inp2 = input("\nCompress? ")
			if inp2 == '':
				break
			else:
				print ("-Hit Enter-")
comp_list, comp_list_len = compress(bin_list)
while True:
			inp2 = input("\nExpand? ")
			if inp2 == '':
				break
			else:
				print ("-Hit Enter-")
expand_list, expand_list_len = expand(comp_list, comp_list_len)

print ("\n=====Results=====")
print ("Number of variables: "+str(var))
print ("Binary list: "+str(bin_list_len))
print ("Compressed list: "+str(comp_list_len))
print ('Compression: ', float(round(float(comp_list_len/bin_list_len), 5)*100), '%')
print ("Data Lost:"+str(float((round(float(expand_list_len/bin_list_len)-1, 4)*100)))+'%\n')
print ("Theoredical compression equation: lim n->∞ ((a^2 - 1)/(a^2)) * n\na=number of repeating variables\nn=length of string")
