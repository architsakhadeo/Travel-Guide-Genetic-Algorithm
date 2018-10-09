#total 435 entries as per two loops. i from 1st to last. j from i+1 to last

capital = ["Hyderabad","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Srinagar","Ranchi","Bangalore","Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneshwar","Jaipur","Gangtok","Chennai","Agartala","Lucknow","Dehradun","Kolkata","Daman and Diu","Delhi","Pondicherry"]

input_file_train = open('resultsoftrain','r').readlines()
output_file_train = open('resultsDictTimeTrain','w+')
output_train = []


line = 0

#SCANS THROUGHT THE JSON FILE AND STORES STRINGS OF A JSON OBJECT IN A LIST
for i in range(1,436):
	string = ""
		
	if "ZERO_RESULTS" in input_file_train[line+7]:
		for j in range(14):
			string += input_file_train[line]
			line += 1
		line += 7
	else:
		for j in range(22):
			string += input_file_train[line]
			line += 1
		line += 7
	#print string, i
	output_train.append(string)  #array of json strings


import urllib
import json
tpythonDict = []
tdistance = []
ttime = []

#STORES TIME AND DISTANCES BETWEEN PLACES
for i in range(len(output_train)):
	z = json.loads(urllib.unquote(output_train[i]))
	tpythonDict.append(z)  #array of json objects
	
	if z['rows'][0]['elements'][0]['status'] == "ZERO_RESULTS":
		ttime.append(0)  #array of time taken
		tdistance.append(0)  #array of distance
	else:
		ttime.append(tpythonDict[i]['rows'][0]['elements'][0]['duration']['value'])  #array of time taken
		tdistance.append(tpythonDict[i]['rows'][0]['elements'][0]['distance']['value'])  #array of distance



k = 0	


#DISTANCES ARE SORTED, TIME TAKEN IS SORTED. IT IS FOUND THAT BOTH METHODS GIVE DIFFERENT ORDER OF INDICES MEANING THAT DISTANCE AND TIME
#NOT NECESSARILY VARY DIRECTLY. IN PLACES OF HIGHER ELEVATION, LESS DISTANCE MAY REQUIRE MORE TIME.
#THUS SHORTEST PATH IS FOUND OUT BASED ON THE TIME TAKEN AND NOT THE DISTANCE.

sorted_time = ttime[:]
sorted_distance = tdistance[:] 
time_index = []
distance_index = []
for i in range(len(ttime)):
	time_index.append(i)
	distance_index.append(i)

for i in range(len(ttime)-1):
	for j in range(len(ttime)-i-1):
		if sorted_time[j] > sorted_time[j+1]:
			temp = sorted_time[j]
			sorted_time[j] = sorted_time[j+1]
			sorted_time[j+1] = temp
			temp = time_index[j]
			time_index[j] = time_index[j+1]
			time_index[j+1] = temp

for i in range(len(ttime)-1):
	for j in range(len(ttime)-i-1):
		if sorted_distance[j] > sorted_distance[j+1]:
			temp = sorted_distance[j]
			sorted_distance[j] = sorted_distance[j+1]
			sorted_distance[j+1] = temp
			temp = distance_index[j]
			distance_index[j] = distance_index[j+1]
			distance_index[j+1] = temp
			
output_file_train.write("Sorted Distance and Sorted Time with their indices\n")
for i in range(len(ttime)):
	output_file_train.write(str(sorted_distance[i])+"    "+str(sorted_time[i])+"    "+str(distance_index[i])+"  "+str(time_index[i])+"\n")
output_file_train.write("***********************************************************************************************************************") #resultsdistvstime
output_file_train.write("\nDistance and Time with their sorted indices\n")
for i in range(len(ttime)):
	output_file_train.write(str(tdistance[i])+"    "+str(ttime[i])+"    "+str(distance_index.index(distance_index[i]))+"  "+str(time_index.index(time_index[i]))+"\n")


#FOLLOWING COMMENTED CODE GIVES "FALSE" VALUE AS EXPECTED
'''if distance_index == time_index:
	print "True"
else:
	print "False"
'''
							
output_file_train.close()


