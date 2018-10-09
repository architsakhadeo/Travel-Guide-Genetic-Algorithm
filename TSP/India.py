from urllib2 import urlopen

result = open('results','w+')

# LIST OF UNION TERRITORIES & CAPITALS OF STATES

capitals = ['Hyderabad,Andhra+Pradesh', 'Itanagar,Arunachal+Pradesh', 'Dispur,Assam', 'Patna,Bihar', 'Raipur,Chhattisgarh', 'Panaji,Goa', 'Gandhinagar,Gujarat', 'Chandigarh,Haryana', 'Shimla,Himachal+Pradesh', 'Srinagar,Jammu+&+Kashmir', 'Ranchi,Jharkhand', 'Bangalore,Karnataka', 'Thiruvananthapuram,Kerala', 'Bhopal,Madhya+Pradesh', 'Mumbai,Maharashtra', 'Imphal,Manipur', 'Shillong,Meghalaya', 'Aizawl,Mizoram', 'Kohima,Nagaland', 'Bhubaneshwar,Orissa', 'Jaipur,Rajasthan', 'Gangtok,Sikkim', 'Chennai,Tamil+Nadu', 'Agartala,Tripura', 'Lucknow,Uttar+Pradesh', 'Dehradun,Uttarakhand', 'Kolkata,West+Bengal', 'Daman+and+Diu,Union+Territory', 'Delhi,Union+Territory', 'Pondicherry,Union+Territory']


#QUERYING THROUGH THE GOOGLE MAPS API TO EXTRACT DATA IN JSON FORMAT
				
for p in range(29):
	for q in range(p+1,30):
		origin = capitals[p]
		destination = capitals[q]
		url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + origin + '&destinations=' + destination + '&key=YOUR_OWN_API_KEY' #for roadways
		output = urlopen(url).read()
		result.write(output)
		result.write('\n\n\n\n\n\n\n')

result.close()

