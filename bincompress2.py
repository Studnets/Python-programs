#python binary string
import random
from sys import setrecursionlimit
def rand_bin(inp, var):
	count = 0
	bin_list = []
	while count < inp:
		a = random.randint(0, var-1)
		bin_list.append(a)
		count = count + 1
	for a in bin_list:
		if a==0:	a='a'
		if a==1:	a='b'
		if a==2:	a='c'
		if a==3:	a='d'
		if a==4:	a='e'
		if a==5:	a='f'
		print (a, end='')
	return(bin_list, inp)
#enter you're own binary string
'''
bin_list = []
inp = str(input("Length of binary string: "))
for i in inp:
	bin_list.append(i)
'''
def compress(bin_list, bin_list_len, step):
	count = 0
	mark = step
	comp_list = []
	while count<bin_list_len:
		emp = ''
		while count<mark:
			if count > bin_list_len:
				break
			try:
				emp = emp + str(bin_list[count])
			except:
				break
			count = count+1
		emp = int(emp, var)
		comp_list.append(emp)
		mark = mark+step
	comp_list_len1 = 0
	for i in comp_list:
		comp_list_len1 += len(str(i))
	entrys = len(comp_list)
	#print (comp_list)
	for i in comp_list:
		print (i, end='')
	return (comp_list, comp_list_len1, entrys)
def expand(comp_list, entrys, step, var):
	expand = []
	count = 0
	while count < entrys:
		#i = int(bin(comp_list[count])[2:])
		setrecursionlimit(step**2)
		def char(digit):
		    if digit < 10:
		    	return (str(digit))
		    return (chr(ord('a') + digit - 10))

		def nbase(number,base):
		    (d, m) = divmod(number, base)
		    if d > 0:
		        return (nbase(d, base) + char(m))
		    if m < 10:
		    	return (str(m))
		i = nbase(comp_list[count], var)
		if count == entrys-1:
			expand.append(i)
		elif count!=entrys-1:
			while len(str(i))<step:
				i = '0' + str(i)
			expand.append(i)
		count = count+1
	#print (expand_list)
	expand_list = []
	for i in expand_list:
		for j in str(i):
			if j=='0':	j='a'
			if j=='1':	j='b'
			if j=='2':	j='c'
			if j=='3':	j='d'
			if j=='4':	j='e'
			if j=='5':	j='f'
			print (j, end='')
		for j in i:
			expand_list.append(j)
	expand_list_len = len(expand_list)
	return (expand_list, expand_list_len)
def check(bin_list, expand_list, expand_list_len):
	print ("\n===Check===")
	count = 0
	mark = True 
	while count<len(bin_list) and count <len(expand_list):
		if bin_list[count]==expand_list[count]:
			None
		elif bin_list[count]!=expand_list[count]:
			print ("Data lost")
			mark=False
			break
	if mark==True:
		print ("Lossless")
	print ("===========")
#^Functions Above
print ("Compress 2")
a=False
while True:
	var = input("Number of Variables (5 max): ")
	try:
		var = int(var)
		if var<=6:
			a = True
		elif var>6:
			print ('less than 5')
	except:
		print ('*int')
	if a==True:
		break
while True:
	inp = input("Length of binary string: ")
	try:
		inp = int(inp)
		break
	except:
		print("*integer*")
bin_list, bin_list_len = rand_bin(inp, var)
while True:
	inp2 = input("\nCompress? ")
	if inp2 == '':
		break
	else:
		print ("-Hit Enter-")
while True:
	step = input("\nStep (less than length)? ")
	try:
		step = int(step)
		if step>inp:
			print ("step less than length")
		elif step<=inp:
			break
	except:
		print ("int*")
comp_list, comp_list_len1, entrys = compress(bin_list, bin_list_len, step)
while True:
	inp4 = input("\nExpand? ")
	if inp4 == '':
		break
	else:
		print ("-Hit Enter-")
expand_list, expand_list_len = expand(comp_list, entrys, step, var)
while True:
	inp5 = input("\nCheck? ")
	if inp5 == '':
		break
	else:
		print ("-Hit Enter-")
check(bin_list, expand_list, expand_list_len)
print ("\n=====Results=====")
print ("Number of variables: "+str(var))
print ("Binary list: "+str(bin_list_len))
print ("Step: "+str(step))
print ("Compressed list: "+str(comp_list_len1))
print ('Compression: ', float((round(round(float(comp_list_len1/bin_list_len), 5)*100, 4))), '%')
print ("Data Lost:"+str(bin_list_len-expand_list_len)+'%')
print ("=================")
print ("\nTheoredical compression equation: lim b->n log(a)*n\nb=step\nn=length of string\na=number of repeated variables")
