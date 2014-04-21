#Euler48
#Python
#hashtag

###############
digit_lim = 3
lim = 10**digit_lim
###############

list = []
n = 10
kount = 1
while kount <= 10:
	n = 8
	sum = 1
	count = 1
	while count <= n:
		sum = (sum * n) % lim
		count = count + 1
	list.append(sum)
	kount = count + 1

j = 0
for i in list:
	j = i + j

print (j)
