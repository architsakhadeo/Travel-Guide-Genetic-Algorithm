a = [14, 24, 9, 27, 6, 20, 28, 7, 8, 25, 13, 4, 19, 26, 10, 3, 21, 2, 16, 18, 15, 17, 23, 1, 0, 22, 29, 11, 5, 12]
b = [14, 10, 24, 27, 6, 20, 28, 7, 8, 25, 9, 13, 4, 19, 26, 3, 21, 2, 16, 18, 15, 17, 23, 1, 0, 22, 29, 11, 5, 12]
c = [-1 for i in range(len(a))]

count = 1
i = 1
c[0] = a[0]
while count < len(a):
	c[i] = a[i]
	if b[i] in c:
		break
	k = a.index(b[i])
	i = k
	count += 1

for i in range(len(a)):
	if c[i] == -1:
		c[i] = b[i]

d = []
for i in c:
	d.append((29 - int(i)))

	

print a
print b
print c
print d


'''
************************************************************************
smaller_list = small_list[:]
smaller_list = sorted(smaller_list)
	a = smaller_list[p]
	p += 1
	b = smaller_list[p]


	c = [-1 for i in range(len(lister[0]))]
	count = 0
	flag = 0
	i = 0
	while count < len(a):
		c[i] = a[i]
		if b[i] in c:
			break
		k = a.index(b[i])
		i = k
		count += 1

	for i in range(len(a)):
		if c[i] == -1:
			c[i] = b[i]
	
	q = smaller_list[-1]
	
	smallest = 0
	for j in range(len(perms[0])-1):
		smallest += time_matrix[perms[0][j]][perms[0][j+1]]
	smallest += time_matrix[a][perms[0][0]] + time_matrix[a][perms[0][len(perms[0])-1]]

	
	d = []
	for i in c:
		d.append(str(29 - int(i)))
	
	
	















***********************************************************************************************************************
time_matrix = [[] for i in range(30)]
mode_matrix =  [[] for i in range(30)]
for i in range(30):
	for j in range(30):
		time_matrix[i].append(0)
		mode_matrix[i].append(0)
capital = ["Hyderabad","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Srinagar","Ranchi","Bangalore","Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneshwar","Jaipur","Gangtok","Chennai","Agartala","Lucknow","Dehradun","Kolkata","Daman and Diu","Delhi","Pondicherry"]
from distanceVStime import time
from distanceVStime_train import ttime
import random
timed = []
mode = []

#DECIDES WHICH MODE TO USE BASED ON TIME TAKEN BY EACH
for i in range(len(time)):
	if time[i] < ttime[i] or ttime[i] == 0:
		timed.append(time[i])
		mode.append("bus")
	elif time[i] >= ttime[i]:
		timed.append(ttime[i])
		mode.append("train")

from math import floor, ceil

k = 0

#matrix of time between two places
for i in range(len(time_matrix)-1):
	for j in range(i+1,len(time_matrix)):
		time_matrix[i][j] = timed[k]
		time_matrix[j][i] = timed[k]
#		if i in [14,22,26,28] and j in [14,22,26,28]:
#			print i, j, k, time[k], ttime[k], timed[k], mode[k]
		mode_matrix[i][j] = mode[k]
		mode_matrix[j][i] = mode[k]
		k += 1
		



min_time = []
cities = capital[:]
cities.remove("Mumbai")
b = [cities.index(i) for i in cities]
a = capital.index("Mumbai")
perms = []
perms.append(b)
for i in range(999):
	random.shuffle(b)
	b.insert(0,a)
	perms.append(b)








		


#print perms
min_index = 0
smaller = 0
for j in range(len(perms[0])-1):
	smaller += time_matrix[perms[0][j]][perms[0][j+1]]
smaller += + time_matrix[a][perms[0][len(perms[0])-1]]

for i in perms:
	total_time = 0
	for j in range(len(i)-1):
		total_time += time_matrix[i[j]][i[j+1]]
	total_time +=  time_matrix[a][i[len(i)-1]]
	if total_time < smaller:
		smaller = total_time
		print smaller
	min_time.append(total_time)
	

minimum = min_time.index(smaller)



import math





print perms[minimum],min_time[minimum]


print " ----------------------------------------- "


lister = []
app = [0 for i in range(len(capital))]
v = 100
for l in range(v):
	
	approached = [0 for i in capital]
	ats = [a]
	approached[a] = 1
	if l == 0:
		m = 0
	else:
		m = 1
	while len(ats) <= int(math.log(l+1)/math.log(30)) + m:	
		i = random.randint(0,29)
		if i not in ats:
		#if i != a:
			app[i] += 1
			approached[i] = 1
			ats.append(i)
	
	i = a
	count = len(ats) - 1 		
	
	while count < len(time_matrix):
		count += 1
		approached[i] = 1
		summ = 0
		for j in range(len(time_matrix)):
			if i == j or approached[j] == 1:
				continue
			if summ == 0:
				summ = time_matrix[i][j]
				k = j
			elif time_matrix[i][j] < summ:
				summ = time_matrix[i][j]
				k = j
		i = k
		if count < len(time_matrix):
			ats.append(i)
	
	lister.append(ats)



min_index = 0

small_list = []
for k in lister:
	smaller = 0
	for j in range(len(k)-1):
		smaller += time_matrix[k[j]][k[j+1]]
	smaller += time_matrix[a][k[len(k)-1]]
	small_list.append(smaller)

print lister
print small_list
print  lister[small_list.index(min(small_list))],min(small_list)
print "----------------------------------------------------------" '''
