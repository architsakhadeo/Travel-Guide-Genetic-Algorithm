#DO NOT CHANGE THE POSITION OF CITIES OR ADD OR DELETE ANY CITY AS THIS IS NOT A DYNAMIC PROGRAM. IT DEPENDS ON TWO OTHER PROGRAMS FOR INPUT. THIS PROGRAM IS MEANT TO RUN ONLY ON THE GIVEN INPUT TO TEST A GENETIC APPROACH TO TSP.

#THIS IMPLEMENTS A GENETIC ALGORITHM TO FIND A "GOOD SOLUTION" TO 30 CITIES. THIS CAN BE EASILY MADE DYNAMIC WITH FEW CHANGES TO THE CODE. HOWEVER THIS IS STATIC RIGHT NOW DUE TO DEPENDENCY ISSUES. 

#HERE TIME IS CONSIDERED AS A FACTOR TO FIND SHORTEST DISTANCE SINCE SHORTER DISTANCES CAN REQUIRE MORE TIME. HENCEFORTH IF "DISTANCE" WORD OCCURS, CONSIDER IT
#TO BE TIME.

#ACTUAL ALGORITHM STARTS FROM LINE 120

#THERE ARE THREE STAGES

#STAGE 1 -> POPULATION
				#Population is a randomly selected data set to work upon in order to arrive at a better solution.
				#Here a partial random and a partial greedy solution is implemented to get the best results.
#STAGE 2 -> CROSSOVER
				#Crossover is the formation of a child from two parents, which inherits the good properties of both the parents.
				#Here the property considered is "shortest route" and hence the paths with "longer route" are replaced by these children with "shorter route"
				#Crossover gives a greater gain 
#STAGE 3 -> MUTATION 
				#Mutation is slightly changing the nodes within the route purposely to shift from the local optimum
				#When multiple crossovers are performed, the system arrives at an equilibrium i.e. a local optima. In order to explore different routes
				#   we swap two nodes randomly and check if they lead to a shorter route and we choose them if they qualify our requirement

#ANSWER VARIES EVERY TIME AS WE USE RANDOM APPROACH TO FIND A MEANINGFUL "GOOD SOLUTION"


print
time_matrix = [[] for i in range(30)]
mode_matrix =  [[] for i in range(30)]
for i in range(30):
	for j in range(30):
		time_matrix[i].append(0)

capital = ["Hyderabad","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Srinagar","Ranchi","Bangalore","Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneshwar","Jaipur","Gangtok","Chennai","Agartala","Lucknow","Dehradun","Kolkata","Daman and Diu","Delhi","Pondicherry"]

from distanceVStime import time
from distanceVStime_train import ttime
import random
import math

timed = []
mode = []

#DECIDES WHICH MODE TO USE BASED ON TIME TAKEN BY EACH
for i in range(len(time)):
	if time[i] < ttime[i] or ttime[i] == 0:
		timed.append(time[i])
	elif time[i] >= ttime[i]:
		timed.append(ttime[i])

from math import floor, ceil

k = 0


for i in range(len(time_matrix)-1):
	for j in range(i+1,len(time_matrix)):
		time_matrix[i][j] = timed[k]
		time_matrix[j][i] = timed[k]
		k += 1


#THIS IS A RANDOM APPROACH. CITIES ARE RANDOMLY ARRANGED AND CHECKED FOR THE SHORTEST ROUTE

print "Random approach"

min_time = []
cities = capital[:]
b = [cities.index(i) for i in cities]
a = capital.index("Mumbai")
cities.remove("Mumbai")
b.remove(a)


def shuffleACopy(x):
        b = x[:] # make a copy of the keys
        random.shuffle(b) # shuffle the copy
        return b # return the copy


perms = [shuffleACopy(b) for x in range(999)]
perms.append(b)


min_index = 0                                                                             
smaller = 0
for j in range(len(perms[0])-1):                                                              #
	smaller += time_matrix[perms[0][j]][perms[0][j+1]]										  #
smaller += time_matrix[a][perms[0][0]] + time_matrix[a][perms[0][len(perms[0])-1]]            #
                                                                                              #   TO FIND THE SMALLEST DISTANCE
for i in perms:                                                                               # 
	total_time = 0                                                                            #
	for j in range(len(i)-1):
		total_time += time_matrix[i[j]][i[j+1]]
	total_time +=  time_matrix[a][i[0]] + time_matrix[a][i[len(i)-1]]
	if total_time < smaller:
		smaller = total_time
	min_time.append(total_time)
	

minimum = min_time.index(smaller)




gg = perms[minimum][:]
gg.insert(0,14)


print gg,str(min_time[minimum]) + ' millisec = ' + str(round(min_time[minimum]/3600.0,2)) + ' hours'
print capital[a],
for i in perms[minimum]:
	print capital[i],
print capital[a]
print
print "----------------------------------------------------------"



#ACTUAL ALGORITHM STARTS HERE

# 'lister' and similar variables contain indices of cities
# 'small_list' and similar variables contain total 


print "First step in population, greedy approach"
lister = []
app = [0 for i in range(len(capital))]
v = 1000                                                    # v can be any number. Greater the number, better the solution, slower the execution
for l in range(v):
	
	approached = [0 for i in capital]                       # approached checks if the city is already visited
	ats = [a]
	approached[a] = 1
	if l == 0:
		m = 0
	else:
		m = 1
	while len(ats) <= int(math.log(l+1)/math.log(30)) + m:	 # Planned greedy solution with a random factor of choosing a city(node)
		i = random.randint(0,29)
		if i not in ats:
			app[i] += 1
			approached[i] = 1
			ats.append(i)
	i = a
	count = len(ats) - 1
	
	# Algorithm for greedy solution. We collect such 'v' paths
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
# PRINTS SHORTEST SOLUTION FROM THE GREEDY APPROACH
small_list = []
for k in lister:
	smaller = 0
	for j in range(len(k)-1):
		smaller += time_matrix[k[j]][k[j+1]]
	smaller += time_matrix[a][k[len(k)-1]]
	small_list.append(smaller)


print  lister[small_list.index(min(small_list))],str(min(small_list)) + ' millisec = ' + str(round(min(small_list)/3600.0,2)) + ' hours'
for i in lister[small_list.index(min(small_list))]:
	print capital[i],
print capital[a]
print
print "----------------------------------------------------------"






lister1 = lister[:]                       #contains list of possible paths
small_list1 = small_list[:]               #contains respective distances

def summed(Z):
	s = 0
	for i in range(len(Z)-1):
		s += time_matrix[Z[i]][Z[i+1]]
	s += time_matrix[a][Z[len(Z)-1]]
	return s

zz = 0

print "After crossover and mutation"
#WE PERFORM CROSSOVER IN THIS ITERATION ALONG WITH NESTED MUTATION

#CROSSOVER
	#parent1 = 12345678 
	#parent2 = 85213647 

	#child 1 = 15243678 
	#child 2 = 84756321


#MUTATION
	#node = 12345678
	#after mutation -> 12645378

#CROSSOVER
for x in range(75):                                      # x can be any number. Greater the number, better the solution, slower the execution
	cc = [-1 for i in range(len(lister1[0]))]
	count = 1
	i = 1
	
	least = sorted(small_list1)
	
	aa = lister1[small_list1.index(least[zz%50])]
	bb = lister1[small_list1.index(least[(zz+1)%50])]
	zz += 2

	cc[0] = aa[0]
	while count < len(aa):
		cc[i] = aa[i]
		if bb[i] in cc:
			break
		k = aa.index(bb[i])
		i = k
		count += 1
	
	for i in range(len(aa)):
		if cc[i] == -1:
			cc[i] = bb[i]
	
	dd = []
	for i in cc:
		dd.append((29 - int(i)))


	if summed(cc) < least[-1]:
		small_list1[small_list1.index(least[-1])] = summed(cc)
		lister1[small_list1.index(summed(cc))] = cc
	
	if summed(dd) < least[-2]:
		small_list1[small_list1.index(least[-2])] = summed(dd)
		lister1[small_list1.index(summed(dd))] = dd
	
	
	
	#MUTATION
	lister2 = lister1[:]
	for i in lister2:
		for j in range(30):	                                              # j can be any number. Greater the number, better the solution, slower the execution
			while True:	
				in1 = random.randint(0,29)
				if in1 != 0:
					break
			while True:
				in2 = random.randint(0,29)
				if in1 != in2 and in2 != 0:
					break		
			i[in1],i[in2] = i[in2],i[in1]
			
			if summed(i) < min(small_list1):
				lister1[lister2.index(i)] = i
				continue
			i[in1],i[in2] = i[in2],i[in1]
	
	#PRINTS SHORTEST DISTANCE AFTER ALL PROCEDURES AFTER EACH CROSSOVER ACCOMPANIED BY A MUTATION	
	
	small_list1 = []
	for k in lister1:
		smaller = 0
		for j in range(len(k)-1):
			smaller += time_matrix[k[j]][k[j+1]]
		smaller += time_matrix[a][k[len(k)-1]]
		small_list1.append(smaller)
				
	print min(small_list1)
	


print 
print "********************************************************"
print


#PRINTS SHORTEST DISTANCE AFTER ALL PROCEDURES. THIS IS THE FINAL "GOOD SOLUTION"

small_list1 = []
for k in lister1:
	smaller = 0
	for j in range(len(k)-1):
		smaller += time_matrix[k[j]][k[j+1]]
	smaller += time_matrix[a][k[len(k)-1]]
	small_list1.append(smaller)
					
print min(small_list1)



print lister1[small_list1.index(min(small_list1))],str(summed(lister1[small_list1.index(min(small_list1))])) + ' millisec = ' + str(round(summed(lister1[small_list1.index(min(small_list1))])/3600.0,2)) + ' hours'  

for i in lister1[small_list1.index(min(small_list1))]:
	print capital[i],
print capital[a]


print
print "----------------------------------------------"
