# Development log
## This file is used to record the development log for data collection.

------------------------------------------------------------------------


Date|Version|Contents|Decision making|Risk|Reflection
:---:|:---:|:---|----|------|------|
18/07/2022|v1|Divide whole file(data) to each states|increase the readability of the data|N/A|N/A
18/08/2022|v2|Add weather variables(UVA, UVB humidity, wind)<br> Add additional crop(oat, barley, corn, and rice) data(local and export price, production, yield area)</br>|Weather data <br>Our client suggested to use NASA's data. NASA has reliable satellite system so data from NASA would be reliable. Thus I decided to get weather data from NASA's power.</br> <br> Crop data </br> I used the government publication and statistics because these are from the government, so data must be reliable<br>From last semester, when I searched wheat, I was able to find reports for oat, barley, corn, and rice too. So, collecting these crops would be easier than other crops</br>|Data quality<br>(inaccuracy, missing value, etc)</br>| For radiation, humidity, wind data, I only used one gps point nearby farming area. To improve realiability, add 3 points(weather stations's gps)of weather data and use average value of them </br> <br>For data quality, we will solve it by data cleaning and profiling</br>
25/08/2022|v3|Adjust digits (2 decimal points)<br>Filling missing value</br>Removing redundant crop data<br>Add Covid vector|Use Excel instead of Python <br> Python cannot show many columns at once, so when I read the data set by python, I had to check the column manually. To increase work efficiency, I used excel to reduce the working hour. </br> <br>Data wrangling</br> <br> Reduce 7 decimal points to 2 decimal points to increase readability.</br><br> Replace missing value by mean <br> Because of few data sets and data's characteristic(weather = single value), regression or removing null values are not efficient methods</br> Thus, mean substitution is used for missing value to make keep data sets as many as possible.</br> <br>If some states didn't cultivate specific crops, removed it to the data set(ex. NT rice, maize)</br> <br> Use local and export price data to quatify COVID-19. <br> From my research, We set hypothesis like this. "Covid19 affects local and export crop price" </br>| Data issue(complete : this data has some missing value, consistency : our data don't have multiple sources, so cannot do crosscheck) </br><br>These modifications can affect our algorithm accuracy because all missing values in each column are replaced by same mean values.</br><br>Data imbalance issue because of replaced mean values</br>|<br>Data realiability is important. Our data set is from several sources but we didn't do crosscheck to find the data is valid or not. I thought our data is from the government so there are not big problems on reliability. However, because of consistency issue, I will try to find another source to check the data is valid or not.</br><br>This way could not a perfect way to solve missing values, but as we have a few data set, I choosed the way to maintain the number of datasets. However, if it affects our algorithm significantly, we will discuss and change it.</br>
04/09/2022|v4|Add and Improve weather variables(UVA, UVB, humidity, wind)</br><br>Smooth export price outliers</br><br> Add state column and unify column name to all states</br><br>Adjust wrong value</br><br>Remove rice export price</br>| Calculate weather data from each state's westernmost, easternmost, southernmost, and northernmost stations' data to improve the realiability. This is because I cannot cover all weather stations' data so collecting each side of the stations' data.</br> <br>As our backend team is considering using SQL database, I add column to identify states and unify column names of each data files to increase work efficiency</br> <br>To overcome consistency issue from a data assessment, I got export price from another resource. Our initial export price was calculated so data from new source is more precise </br> <br>Remove rice export value because it has a lot of outliers, but cannot find another resources to do cross-check. To overcome consistency issue and realiability, I decide removing the export rice price</br>|The calculation of weather value is only 4 points in each states. So, realiability of weather data increased but it could be still not precise</br><br>Export price is from new resource but it shows each quarter's data so I put the average value in our data set. So, it could be not precise perfectly</br> | Previous weather data(single point) and new weather data(average of 4 sides of states) is quite different. I thought it would be similar but it was not. So, I think to improve weather value, we need put more weather stations' data.</br> <br>Some parts of data (1990~1994 in export price) is still calculated, not from data source. So, they could be not precise. However, there is no perfect data. If I can find these data too, then I will update them </br>
19/09/2022|v5|Adding external factors(Global crop production, export and trade volume), Baltic Dry Index, oil historical price, Australian fertiliser cost, and global container freight index<br><br>Removing rice data in all states </br> | Gathering global data by continents <br>Don't include Africa because there are a lot of missing values and it accounts for small portions so not using this continents makes our data quality high</br><br>Most outliers and missing values were located on rice data. We already have barley, wheat, corn, and oat data so not using rice data is better for our algorithm.</br> <br>Using both baltic dry index and container index because container index starts from 2016 so using this only for COVID-19 </br> | Global production, trade volume and export data in 2021 was missing, so I calculate it from global trend production, trade. Thus, it would be slightly different with real data.| Deal with missing data is the most difficult part of the data collection works. To cover this, I had to check many data sets and websites. However, as I put more efforts on this, it will make more reliable data, so it is worthy to do it. When I need to cover missing value next time, I will put my efforts as much as I can.
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
global production by continents|Kt|numeric|Yearly
global trade volume by continents|Kt|numeric|Yearly
global exports value by continents|$(USD)|numeric|Yearly
Crude oil price|$(USD)/barrel|numeric|Yearly
Fertiliser cost|$(AUD)|numeric|Yearly
Baltic dry index|$(USD)|numeric|Monthly
global container freight index|$(AUD)|numeric|Monthly



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
All|Crop|global crop trade value|2021
All|Crop|global crop exports volume|2021
All|Crop|global crop production|2021
------------------------------------------------------------------------
## How to deal with missing value
Consider the level of implement, advantages and disadvantages, replacement by mean is used in this data set. However, if it is not proper for our algorithm, we will change the mothod.

### Deletion
Method|Description|Advantages|Disadvantages|
:---:|:---:|---|---|
Listwise deletion|Delete all observations where the missing values occur|Easy to implement| Can result in biased estimates if the missing values are not Missing completely at random (MCAR) <br>Wastes useful information <br> Can disrupt time series analysis by creating gaps in dates used for analysis|
Pairwise deletion|Uses all available data when computing means and covariances|Simple to implement<br>Uses all available information</br>|Can result in biased estimates if the missing values are not MCAR <br> Results in different sample sizes being used for different computations</br> Requires that data follow a normal distribution
Variable Deletion|Eliminate a variable from analysis if it is missing a large percentage of observations|Easy to implement|Significant loss in information <br>May result in missing variable bias</br>|

### Imputation
Method|Description|Advantages|Disadvantages|
:---:|:---:|---|---|
Replacement <br> (mean, median, mode)|All missing values are replaced with the variable mean, median or mode|Easy to implement| Distorts the distribution of the data <br> Reduces data variance <br> Results in biased estimates|
Linear Regression|Missing values are predicted using a linear model and the other variables in the dataset|Simple to implement<br>Uses all available information</br>|Biased correlations between variables <br> Underestimated variability </br> Falsely strengthens relationship between variables
Last observation carried forward (LOCF)|Use last observed data value as a replacement for missing data|Appropriate for time series data|Can results in biased estimates even when data is MCAR <br>Modeling techniques should address that data has been imputed by LOCF</br>May incorrectly suggest stability across time stretches if used to fill successions of missing data|
Predictive mean matching|Replacements for missing values are drawn randomly from a group of nearby candidate values|Appropriate for time series data <br> Easy to use and versatile</br> Robust to data transformations <br>Valid for discrete data</br> Will always produce replacements within the observed data range| May result in missing variable bias <br>May duplicate values, especially if sample is small</br> Not suited for small samples, skewed data, or sparse data <br>Cannot be used to extrapolate beyond range of the data</br>|

------------------------------------------------------------------------
## Where the data from
Weather
<br> Australian Government Bureau of Meteorology http://www.bom.gov.au/?ref=logo
<br>NASA https://power.larc.nasa.gov/data-access-viewer/ </br>
<br>
Crop
<br>Australian Government Department of Agriculture, Water and the Environment</br>
https://daff.ent.sirsidynix.net.au/client/en_AU/ABARES/search/results?te=ASSET&st=PD </br>
https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#agricultural-commodities </br>
https://www.agriculture.gov.au/abares/data/weekly-commodity-price-update/world-agricultural-prices
<br>Food and Agriculture Organization of the United Nations
<br>https://www.fao.org/home/en</br>
<br>Our World in Data
<br>https://ourworldindata.org/grapher/crude-oil-prices</br>
<br>Freightos data
<br>https://fbx.freightos.com/</br>
<br>Investing
<br>https://au.investing.com/indices/baltic-dry-historical-data</br>

