#Python team maker
from random import randrange
while True:
	try:	
		people = int(input("How many people: "))
		teams = int(input("How many teams: "))
		if people<teams:	print("Teams>People")
		elif people>=teams:	break
	except ValueError:    print("*int")
##########
main = []
main.extend(range(1,people+1))
##########
number = []
count = 1
m_length = len(main)
while count <= people:
	if m_length>1:
		select = randrange(m_length-1)
		a = main[select]    
		number.append(a)
		del main[select]
		m_length-=1
	else:
		number.append(main[0])
	count = count + 1
additional = people%teams
ppert = int(people/teams)
main_teams = []
i=0
mark1 = 0
while i<teams:
	if additional>0:
		main_teams.append(number[mark1:mark1+ppert+1])
		mark1 = mark1+ppert+1
		additional -= 1 
	elif additional==0:
		main_teams.append(number[mark1:mark1+ppert])
		mark1 = mark1+ppert
	i += 1

for i,k in enumerate(main_teams):
	print ("Team "+str(i+1)+":"+'\n'+str(main_teams[i]))
