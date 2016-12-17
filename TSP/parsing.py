#total 435 entries as per two loops. i from 1st to last. j from i+1 to last

capital = ["Hyderabad","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Srinagar","Ranchi","Bangalore","Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneshwar","Jaipur","Gangtok","Chennai","Agartala","Lucknow","Dehradun","Kolkata","Daman and Diu","Delhi","Pondicherry"]
input_file1 = open('results','r').readlines()
output_file1 = open('resultsFinal','w+')
output = []
from distanceVStime import *

k = 0	
for i in range(29):
	for j in range(i+1,30):
		output_file1.write(capital[i] + " to " + capital[j] + ' ')
		output_file1.write("Time taken: " + str(time[k]) + ' ')
		output_file1.write("Distance: " + str(distance[k]) + '\n')
		k += 1
				
output_file1.close()

