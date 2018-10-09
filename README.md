**->What the existing code does is:**

1)It accepts the origin city. This city is where the travelling must start and end.

2)It later accepts multiple other cities which have to be covered in the journey.
	
3)It accepts the total number of days the user wants to spend throughout the journey.
	
4)Based on this data, the program outputs the shortest path to travel these cities using the apt mode of transport(bus or train) whichever requires lesser time of the two modes. Based on the number of days available with the user and the amount of time spent in travelling for the rest of the journey, it outputs the number of days viable to stay at a particular city.
        
5)It outputs a map in the browser which gives an idea of how the route will look like approximately. "Approximately" because Google Maps API doesn't allow to plot the roadways and railway paths on the same map. Hence only the roadways are plotted even where actually a railway path would be used. The map merely gives the user an idea of how the whole travel plan might be like. 


**RECOMMENDED** -> Directly run "python matrix.py" to start directly with the stored data in the files "results" and "resultsoftrain"

    INPUT THE CITIES EXACTLY AS THE FOLLOWING STRINGS AS THE INPUT IS CASE SENSITIVE.

            "Hyderabad","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Srinagar","Ranchi","Bangalore",
            "Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneshwar","Jaipur","Gangtok","Chennai",
            "Agartala","Lucknow","Dehradun","Kolkata","Daman and Diu","Delhi","Pondicherry"

Or

**TIME CONSUMING** -> Follow the following steps by running "python main.py" to actually download the data via Google Maps API

python India.py

python India_train.py

python distanceVStime.py

python distanceVStime_train.py

python parsing.py

python parsing_train.py

python matrix.py

**RUN "python genetic.py"** to check a genetic algorithm implementation for TSP

