#Alexander Comerford Python function 
#If reading code start bottom
'''Give equation input, max integer, increment, and output style. Program will print x values (incremented
with given input value) and corresponding equation value.'''



import time
import threading
import parser
import matplotlib.pyplot as plt
import numpy,pylab
import math
def eq_print():
	print("\n\nType an equation only with the variable x\n==========================================")
	print("    ||Available Expressions||	")
	print("-Addition: +")
	print("-Subtraction: -")
	print("-Multiplcation: *")
	print("-Division: /")
	print("-Powers: **")
	print("-Modulo: %")
	print("==========================================")
class In_Check:
	#In print messages#
	MAX_print = "Max 'x' value (Integer): "
	eq_print = "f(x) = "
	inc_print = "Increment (Max 5 digits):"
	valid = "\n===Valid Input===\n"
	out_print = "\n\nStatic output or recorded output? \n ([S]tatic / [R]ecorded): "
	#Error messages#
	eq_error = "*invalid equation"
	MAX_error = "'*Enter valid input (POSITIVE INT)"
	inc_error = "*Enter valid input (POSITIVE NUMBER)"
	out_error = "Invalid Input (Not valid option)"
	def gen_check(self, check_val):
		while True:
			error_message = "Something fucked up"
			response = ''
			return_out = ''
			try:
				if check_val =="equation":
					error_message = self.eq_error
					eq_in = input(self.eq_print)
					eq_parsed=parser.expr(eq_in).compile()
					x=0
					eval(eq_parsed)
					return_out = eq_parsed
					break
				elif check_val=="Increment":
					error_message = self.inc_error
					increment=float(input(self.inc_print))
					return_out = increment
					break
				elif check_val == "MAX_int":
					error_message = self.MAX_error
					MAX=int(input(self.MAX_print))
					return_out = MAX
					break
				elif check_val == "output":
					error_message = self.out_error
					select = input(self.out_print)
					if select.lower()=='s' or select.lower()=='static':
						select='static'
					elif select.lower()=='r' or select.lower()=='recorded':
						select='recorded'
					return_out = select
					break
			except:
				print (error_message)
		return (return_out)

############################################################################################
def graph1(runOnce, graphx, graphy):
	while runOnce:
		plt.axis([0,10,0,10])
		plt.ion()
		plt.show(block=False)
		runOnce=False
	pylab.xlim([graphx-10, graphx+10])
	pylab.ylim([graphx-10, graphy+10])
	plt.scatter(graphx, graphy)
	plt.draw()
def stats(eq_parsed,MAX,increment,out):
	print("\n\n====================")
	print("Equation:",'f(x) =', str(eq_parsed))
	print('Max Val: '+str(MAX)+'\n'+'Increment: '+str(increment))
	print('Output: '+ out)
	print('Total Amount of values: '+str(int(MAX/increment)+1))
	print('Aprroximated amount of time: '+ str(round(((float(MAX)/float(increment))*0.08), 4))+' seconds')
	print("====================\n\n")
def stop():
	global pause
	pause = input() #user types or hits anything to break loop
	pause = None
def engine():
	T=True
	while T==True: #big loop used incase user unwanted input
		eq_parsed = In_Check.gen_check("equation")
		print (eq_parsed)
		while True:
			MAX = In_Check.gen_check('MAX_int')
			increment = In_Check.gen_check("Increment")
			if increment>MAX: #makes sure increment isn't greater than max to prevent no output
				print("*Error: Increment>MAX\n----------------\n")
			elif increment<=MAX:
				break 
		out = In_Check.gen_check('output')
		while True: #loop used to make sure input is what user intended
				stats(eq_parsed,MAX,increment,out)
				check = str(input('Indended input? (y/n): '))#asks if input is what user intended
				if check=='n':
					break #break to repeat big loop and re-enter values
				elif check=='y':
					T=False
					break 
				else:
					print ('Invalid input* (y/n) only')
	input("\n\nYou can hit enter or type anything to stop.\nType anything to run: ")
	#x=MAX
	#plt.axis([0,MAX,0,eval(eq_parsed)])
	#Last verification before program runs
	#Let's user know program ready to go :D
###############################################
	if len(str(increment))-1 <= 6:
		round_indic = len(str(increment))-1
	elif len(str(increment))-1 > 6:
		round_indic = 6
	#^rounding specifications incase increment is too long
###############################################
	global equation, pause
	equation = eq_parsed
	pause = False
	t1 = threading.Thread(target=stop(), args=(), daemon=True)
	t1.start()
	'''^Thread started incase user entered large data set or
	incorrect parameters.'Emergency stop'   '''
	runOnce=True
	x_list = [] #x data stored
	y_list = []	#y data stored
	length = len(str(increment)) #length used to format printing			  
	x=0 #x counter
	count = 0 #list counter
###############################################
	while x<=MAX: #loop used to make x values first
		if pause: #incase stop is activated while loop will break
			break					  
		x = round(x, round_indic)
		x_list.append(x)
		y = eval(equation)
		y = round(y, (round_indic))						  
		y_list.append(y)
		#^^^^^List generated one value at a time for storage
		#pylab.xlim([ x_list[count]-10, x_list[count]+10])	
		#pylab.ylim([y_list[count]-10, y_list[count]+10])	  
		adj = 5	#define generic space value 
		adj = adj + (length - len(str(x))) #space value changes based on length of x	
		space = ' ' * adj	
		if out=='recorded':
			if count==0:
				print('X:'+space+'Y:')
			print(str(x_list[count])+space+str(y_list[count]))
		elif out=='static':									  
			print('X: '+str(x_list[count])+space+'Y: '+str(y_list[count]), end='\r')
		graphx = x_list[count]
		graphy = y_list[count]
		graph1(runOnce,graphx, graphy)
		time.sleep(.005)
		count = count + 1
		x=x+increment
	#print(x_list)
	#print(y_list)
	print("\n-----END!-----\n\nPass:")
###################################################################		
#START
In_Check = In_Check()
mark=False
while True: #loop used for specific input
	if mark==False:n=input("\nStart Program (y/n): ") #initial 'start' input
	elif mark==True:n=input("\nStart Again? (y/n): ") #after full excecution new 'start' input
#----------------------------------------
	if n.lower()=='y':
		engine()
		mark=True
	elif n.lower()=='n':break
	else:print("Invalid Input*")
