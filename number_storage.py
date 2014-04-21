user_list = []
marker_0 = 0 
while marker_0 == 0:
	number_storage = input("How many numbers should I store for you?  ")    
	if not number_storage.isdigit():        
		print ('*Enter valid input')
	else:  
		number_storage = int(number_storage)
		break
#define loop as constantly true until forcibly broken
#.isdigit used to detect valid input

		
count = 1 #set to increment until it meets number_storage
marker_1 = 1 #end loop incase user enters to large of number_storage value

print ('Enter digits. Type "end" to end storage')
while count < number_storage+1: # '+1' used so 'number 0' doesn't get printed
    print ("number", count,"=")
    while marker_0 == 0:
        user_input = input()
        if user_input == 'end':
            marker_1 = marker_1 -1
            break
        elif not user_input.isdigit(): #used to detect valid input
            print ('*Enter valid input')
        else:
            number_storage = int(number_storage)
            break
    if marker_1 == 0:
        break
    user_list.append(user_input) #loops .append function to add numbers to list
    count = count + 1
	
#basic print list code
print ("Got them all stored for you. Want me to print? (y/n)")
yes_no = input()
print ('') #empty line for space
if yes_no == 'y' or yes_no == "yes":
    for i in user_list:
        print (i)
elif yes_no == 'n' or yes_no == "no":
    print ("ok, bye for now")
else:
    print ("*invalid input")
    print ("ending...")
print ("See you later")