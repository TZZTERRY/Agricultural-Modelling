# Development log
## This file is used to record the development log for data collection.

------------------------------------------------------------------------


Date|Version|Contents|Decision making|Risk|Reflection
:---:|:---:|:---|----|------|------|
18/07/2022|v1|Divide whole file(data) to each states|increase the readability of the data|N/A|N/A
18/08/2022|v2|Add weather variables(UVA, UVB humidity, wind)<br> Add additional crop(oat, barley, corn, and rice) data(local and export price, production, yield area)</br>|Weather data <br>Our client suggested to use NASA's data. NASA has reliable satellite system so data from NASA would be reliable. Thus I decided to get weather data from NASA's power.</br> <br> Crop data </br> I used the government publication and statistics because these are from the government, so data must be reliable|Data quality<br>(inaccuracy, missing value)</br>| For radiation, humidity, wind data, I only used one gps point nearby farming area. To improve realiability, add 3 points(weather stations's gps)of weather data and use average value of them </br> <br>For data quality, we will solve it by data cleaning and profiling</br>
25/08/2022|v3|Adjust digits (2 decimal points)<br>Filling missing value</br>Removing redundant crop data<br>Add Covid vector|Previous data were wrote in 7 decimal points so adjust them to 2 decimal points to increase readability.</br><br> As our data set has few data and considering data's characteristic, single regression is a not proper method to replace missing values</br> Thus, mean substitution is used for missing value because our dataset has about 30 years, so I tried to save data as many as possible.</br>  <br>Some states didn't include any data for specific crops, so I removed it to the data set for our algorithm (ex. NT rice, maize)</br> <br> From the research to the effects of Covid19, we assumed it affects local and export crop price during 2020. But after 2020, local and export price increased significantly. Thus, our hypothesis for COVID-19 external factor is based on this research</br>|Can affect our algorithm accuracy.</br><br>Data imbalance issue</br>|This way could not a perfect way to solve missing values, but as we have a few data set, so I choose the way to maintain the number of datasets. However, if it affects our algorithm significantly, we will discuss and change it. 
------------------------------------------------------------------------

## Data unit description
Data|Unit|Type|Period
:---|:---:|:---:|:---:|
Local price|$(AUD)/t|numeric|Yearly
Export price|$(AUD)/t|numeric|Yearly 
Crop production|Kt|numeric|Yearly
Crop yield area|1000 hec|numeric|Yearly
Temperature|℃|numeric|Monthly
Rainfall|mm|numeric|Monthly
Pan evaporation|mm|numeric|Monthly 
UVA|Watts/m2|numeric|Monthly
UVB|Watts/m2|numeric|Monthly
Wind|m/s|numeric|Monthly
Humidity|%|numeric|Monthly
Covid|0,1|binary|Yearly

------------------------------------------------------------------------
## Missing data (Replaced or removed data)
State|Type|Data|Year|
:---:|:---:|---|---|
All|Weather|UVA, UVB|1990 ~ 2000
All|Weather|Pan evaporation|2018.12 ~ 2021
All|Crop|Crop local price|1998 ~ 2001
NT|Crop|Crop data|Removed(All)
Qld|Crop|Rice price|1994 ~ 2009, 2012 ~ 2014
Qld|Crop|Maize price|2008, 2010
SA|Crop|Rice|Removed(All)
SA|Crop|Maize|Removed(All)
TA|Crop|Rice|Removed(All)
TA|Crop|Maize|Removed(All)
TA|Crop|Wheat price|2018 ~ 2019
TA|Crop|Oat price|2020
Vic|Crop|Maize price|2008, 2010
Vic|Crop|Rice crop area|1990 ~ 1996, 2000, 2007 ~ 2009, 2017 ~ 2021
Vic|Crop|Rice production|1990 ~ 1996, 2000, 2008 ~ 2009, 2017 ~ 2021
Vic|Crop|Rice local price|1990 ~ 1996, 2003, 2008 ~ 2009, 2017 ~ 2021
WA|Crop|Rice|Removed(All)
WA|Crop|Maize local price|2002, 2008, 2010
WA|Crop|Maize crop area|2002

------------------------------------------------------------------------
##Where the data from
Weather
<br> Australian Government Bureau of Meteorology http://www.bom.gov.au/?ref=logo
<br>NASA https://power.larc.nasa.gov/data-access-viewer/ </br>

Crop
<br>Australian Government Department of Agriculture, Water and the Environment</br>
https://daff.ent.sirsidynix.net.au/client/en_AU/ABARES/search/results?te=ASSET&st=PD </br>
https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#agricultural-commodities </br>
https://www.agriculture.gov.au/abares/data/weekly-commodity-price-update/world-agricultural-prices
