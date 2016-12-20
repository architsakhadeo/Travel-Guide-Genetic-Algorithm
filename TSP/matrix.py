import webbrowser
import types
import re

time_matrix = [[] for i in range(30)]
mode_matrix =  [[] for i in range(30)]
for i in range(30):
	for j in range(30):
		time_matrix[i].append(0)
		mode_matrix[i].append(0)
capital = ["Hyderabad","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Srinagar","Ranchi","Bangalore","Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneshwar","Jaipur","Gangtok","Chennai","Agartala","Lucknow","Dehradun","Kolkata","Daman and Diu","Delhi","Pondicherry"]
from distanceVStime import time
from distanceVStime_train import ttime

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

#functions to approximate the days. The ratios have been decided based on the output of certain data sets
def DaysF(a):
	d = float(a) - int(a)
	if d <= 0.75:
		return floor(a)
	else:
		return ceil(a)

def DaysC(a):
	d = float(a) - int(a)
	if d >= 0.25:
		return ceil(a)
	else:
		return floor(a)

from itertools import permutations
#from time import time

while True:
	#start = time()
	
	value = True
	while value:
		a = raw_input("Enter the origin: ")
		if a in capital:
			value = False
			a = capital.index(a)
		elif a == '':
			print "Enter a city"
		else:
			print "Wrong place, enter right spelling again"
	
	b = []
	print "Enter at least 2 places and at most 10 cities"
	counter = 0
	while counter < 9:
		
		no = raw_input("Enter a place: ")
		
		if no in b:
			print "Already entered"
		
		for i in xrange(len(capital)):
			
			if type(re.match(no,capital[i],re.IGNORECASE)) is types.NoneType:
				flag = 1
				pass
			else:
				b.append(i)
				counter += 1
				flag = 0
				break
	
		if flag:
			print "Wrong place, enter right spelling again"
	
	
	days = int(raw_input("Total number of days of stay: "))
	'''b = []
	for i in capital:
		if i is not "Mumbai":
			b.append(capital.index(i))
	'''
	#print a, capital[a]
	#for i in b:
	#	print i,capital[i]
		
	min_time = []
	perms = [i for i in permutations(b)]
	###print perms
	 
	#PURELY OPTIMUM SOLUTION MEANT ONLY FOR NODES UPTO 10. FOR HIGHER NODES CHECK THE OTHER PROGRAM.
	for i in perms:
		total_time = 0
		for j in range(len(i)-1):
			total_time += time_matrix[i[j]][i[j+1]]
		total_time += time_matrix[a][i[0]] + time_matrix[a][i[len(i)-1]]
		min_time.append(total_time)

	
	minimum = min_time.index(min(min_time))
	#print capital[a]
	
	city = []
	mode = []
	index = []
	city.append(capital[a])
	index.append(a)
	#STORES THE FIELDS CORRESPONDING TO MINIMUM TIME REQUIRED TO TRAVEL ALL PLACES
	
	for j in range(len(perms[minimum])):
		city.append(capital[perms[minimum][j]])
		index.append(perms[minimum][j])
	city.append(capital[a])
	index.append(a)
	
	for i in range(len(index)-1):
		mode.append(mode_matrix[index[i]][index[i+1]])
	
	
	
	print "---------------------------"
	ratio = []
	for i in range(len(index)-2):
		ratio.append(float(time_matrix[index[i]][index[i+1]])/min_time[minimum])
	#print ratio
	
	#print len(time),len(ttime),len(timed)
	for i in range(len(mode)-1):
		print str(city[i]) + " to " + str(city[i+1]) + " by " + str(mode[i]) + ", time taken " + str(round(time_matrix[index[i]][index[i+1]]/3600.0,2)) + " hours, number of days of stay at " + str(city[i+1]) + " " + str(DaysF(ratio[i]*days)) + "-" + str(DaysC(ratio[i]*days))
	print str(city[len(mode)-1]) + " to " + str(city[len(mode)-1+1]) + " by " + str(mode[len(mode)-1]) + ", time taken " + str(round(time_matrix[index[len(mode)-1]][index[len(mode)-1+1]]/3600.0,2))	 + " hours"
	print "Total time taken " + str(round(min_time[minimum]/3600.0,2)) + " hours"
	
	url = "https://www.google.co.in/maps/dir/" 
	for i in city:
		url += str(i) + "/"
	
	#OPENS WEB BROWSER WITH THE REQUIRED PATH	
	webbrowser.open(url)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

