# Development log
## This file is used to record the development log for data collection.

------------------------------------------------------------------------


Date|Contents|Decision making|Risk|Reflection
---|---|----|------|------|
18/07/2022|Divide whole file(data) to each states|increase the readability of the data|N/A|N/A
18/08/2022|Add weather variables(UVA, UVB humidity, wind), add additional crop(oat, barley, corn, and rice) data(local and export price, production, yield area)|Weather data <br>Our client suggested to use NASA's data. NASA has reliable satellite system so data from NASA would be reliable. Thus I decided to get weather data from NASA's power.</br> <br> Crop data </br> I used the government publication and statistics because these are from the government so data is reliable|data quality<br>(inaccuracy, missing value)</br>| For radiation, humidity, wind data, I only used one gps point nearby farming area. To improve realiability, add 3 points(weather stations's gps)of weather data and use average value of them.
