# Week 9 Meeting Minutes for MAST30034 Industry Project 22

## 12th meeting
**Time**: 9.15, Thursday, 13:00 ~ 18:00  
**Lcoation**: 93 Flemington Road  
**People**: 
1. Zihan Yin
2. Ximing Wan
3. Suhui Tu
4. Xiaoqing Lei

**What we've done**:  
by Zihan Yin:  
1. Write week 8 meeting minute markdown file

by Ximing Wan:  
1. Write the code which can scape all the shopping center locations of Victoria
2. Aid in debugging and writing code for downloading
3. `add_closest_school.ipynb`: preprocess for the external dataset 'shopping centre', & merge into 'merged data'

by Suhui Tu:  
1. Write the code that downloads the external dataset 'park locations'

by Xiaoqing Lei:  
1. Modify the codes for the external datasets 'personal_income' & 'school_location' to make them work in an updated python environment (debug).
2. Write the code that downloads the external dataset 'hospital locations'
3. `add_closest_hospital.ipynb`: preprocess for the external dataset 'hospital locations', & merge into 'merged data' (based on Ximing Wan's code)



## 13th meeting
**Time**: 9.18, Monday, 15:00 ~ 1:00 a.m.  
**Lcoation**: 93 Flemington Road  
**People**: 
1. Zihan Yin
2. Ximing Wan
3. Suhui Tu

**What we've done**:  
by Zihan Yin:  
1. `add_closest_shopping_centre.ipynb`: preprocess for the external dataset 'shopping centre', & merge into 'merged data' (based on Ximing Wan's code)
2. Convert 'sa2 population' to 'sa2 population density' (for geopatial plot)
3. draw 7 geopatial plots for the external features

by Ximing Wan:  
1. Thoroughly completed the code to find the nearest facilities for each property and save the data as CSV after calculating the distance and merging the data to the main data.
2. (write the codes to) calculate the centroid of each train station based on the PTV shape file and found the three nearest stations for each property based on the centroid coordinates.

by Suhui Tu:  
1. `add_closest_parks.ipynb`: preprocess for the external dataset 'park locations', & merge into 'merged data' (based on Ximing Wan's code)



## 14th meeting
**Time**: 9.19, Tuesday, 13:00 ~ 00:00  
**Lcoation**: 93 Flemington Road  
**People**: 
1. Zihan Yin
2. Ximing Wan
3. Suhui Tu
4. Xiaoqing Lei

**What we've done**:  
by Zihan Yin:  
1. modification on `add_closest_hospital.ipynb`
2. `preprocessing_for_prediction.ipynb`, which includes: 
    - Convert 'population' to 'population_density' in merged data
    - Convert 'crime_rate' to 'offence_count' in merged data
    - Harmonise the 3 features 'population_density', 'offence_count' & 'personal_income' to 2023 data
    - Create 2 datasets for analysis & prediction: `merged_data_2023` & `merged_data_2026`

by Ximing Wan:  
1. `add_closest_station.ipynb`: preprocess for the external dataset 'park locations', & merge into 'merged data'
2. write code to draw heatmaps and pair plots for merged_data that adds distance to facilities. 
3. analyze the distribution and correlation of external features as theoretical support for subsequent modeling.

by Suhui Tu:  
1. finish `add_closest_parks.ipynb` (based on Ximing Wan's code)
2. continue writing the codes of scrapying the api (based on Xiaoqing Lei's code)

by Xiaoqing Lei:  
1. explore the OpenRouteService website and discuss with Ximing Wan how to scape the data.
2. write the codes of scrapying the OpenRouteService for sampled property dataset. there are 2 cloest train station, hence extracting 2 api for each property (codes about api)



## 15th meeting
**Time**: 9.20, Wednesday, 15:00 ~ 00:00  
**Lcoation**: 93 Flemington Road  
**People**: 
1. Zihan Yin
2. Ximing Wan
3. Suhui Tu
4. Xiaoqing Lei

**What we've done**:  
by Zihan Yin:  
1. complete `preprocessing_for_prediction.ipynb`
2. draw 4 geopatial plots for the external features
3. Write (part of) `README.md`

by Ximing Wan:  
1. `add_CBD_distance.ipynb`: code was written to calculate the distance of a property from Melbourne CBD. 
2. the pre-processed data was converted into modelling data: features that could not be used for modelling were removed and features of low significance were removed by backwards elimination.
3. build 1 model, which is random forest tree

by Suhui Tu:  
1. extract distance and duration from api scarping

by Xiaoqing Lei:  
1. discover how to avoid crawling OpenRouteService restrictions.
2. write the for loop to extract the distance and duration of cloest train station (codes about api)
3. create and use multiple mailboxes and accounts to crawl OpenRouteService.


## 16th meeting
**Time**: 9.22, Friday, 10:00~12:00  
**Lcoation**: peter hall  
**People**: 
1. Ximing Wan
2. Suhui Tu
3. Xiaoqing Lei

**What we've done**:  
- Attend the workshop

by Ximing Wan:  
1. Based on the housing and city information in 2023, a random forest model is trained.
2. House prices in 2026 were predicted and the price growth rate calculated for each property.
3. Calculate the average price growth rate for each region.

by Suhui Tu:  
1. debug and scarping data from openroute

by Xiaoqing Lei:  
1. debug and scarping data from openroute