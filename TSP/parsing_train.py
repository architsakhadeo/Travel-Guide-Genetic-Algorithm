#total 435 entries as per two loops. i from 1st to last. j from i+1 to last

#capital = ["Hyderabad,Andhra Pradesh","Itanagar,Arunachal Pradesh","Dispur,Assam","Patna,Bihar","Raipur,Chhattisgarh","Panaji,Goa","Gandhinagar,Gujarat","Chandigarh,Haryana","Shimla,Himachal Pradesh","Srinagar,Jammu & Kashmir","Ranchi,Jharkhand","Bangalore,Karnataka","Thiruvananthapuram,Kerala","Bhopal,Madhya Pradesh","Mumbai,Maharashtra","Imphal,Manipur","Shillong,Meghalaya","Aizawl,Mizoram","Kohima,Nagaland","Bhubaneshwar,Orissa","Jaipur,Rajasthan","Gangtok,Sikkim","Chennai,Tamil Nadu","Agartala,Tripura","Lucknow,Uttar Pradesh","Dehradun,Uttarakhand","Kolkata,West Bengal","Daman and Diu,Union Territory","Delhi,Union Territory","Pondicherry,Union Territory"]
capital = ["Hyderabad","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Srinagar","Ranchi","Bangalore","Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneshwar","Jaipur","Gangtok","Chennai","Agartala","Lucknow","Dehradun","Kolkata","Daman and Diu","Delhi","Pondicherry"]
input_file2 = open('resultsoftrain','r').readlines()
output_file2 = open('resultsFinalTrain','w+')

from distanceVStime_train import *


k = 0	
for i in range(29):
	for j in range(i+1,30):
		output_file2.write(capital[i] + " to " + capital[j] + ' ')
		output_file2.write("Time taken: " + str(ttime[k]) + ' ')
		output_file2.write("Distance: " + str(tdistance[k]) + '\n')
		k += 1
				
output_file2.close()

