In this notebook we scrape a wikipedia page containing info on the USAs 
50 busiest airports (rank, name, city served, IATA code, etc) and merge 
this with data scraped from a .csv file found online containing lat/long 
data for each US airport. The .csv file is included in the repo. This 
resulting information is used to populate a SQL database. Next, we scrape 
a decade of historical weather data from wunderground for each airport in 
our SQL db and populate another SQL db with this data. Using the Pearson 
correlation coefficient, we then quantify the correlation between weather 
patterns (high temp and precip) between a given pair of airports with a 1, 
3 and 7 day offset. 

These results are then plotted for the top ten correlated 
pairs as a function of total distance as well as longitudinal distance. 
A few trends are visible when plotting the data in this way. First, we see 
for the smallest day offset (1 day) the correlation values tend to be concentrated 
at smaller total and longitudinal distances, while for larger offsets the 
correlation values tend to contain larger total and longitudinal distances. The 
magnitude of the correlation values also decreases slightly as larger day offsets 
are explored. These two trends makes sense, since weather patterns evolve as they move 
(which results in a decrease in correlation strength between two locations), while 
for larger day offsets the weather system will have traveled farther (which results 
in larger total and longitudinal distances between the top ten correlated pairs). 
These trends are seen as being a bit stronger for temperature when compared with 
precipitation - the correlation values decrease and the distribution of 
distances increases at larger day offsets for temp data a bit more reliably than 
for precip data.