# Week 8 Meeting Minutes for MAST30034 Industry Project 22

## 8th meeting
**Time**: 9.12, Tuesday, 14:30 ~ 00:30a.m.  
**Location**: 93 Flemington Road  
**People**: 
1. Zihan Yin
2. Ximing Wan
3. Suhui Tu
4. Xiaoqing Lei

**What we've done**:  
by Zihan Yin:  
1. The found dataset of postcode-sa2 relationships was preprocessed and feature selection was performed (but then this dataset was found to be unfavourable for later merge work and was abandoned)  
2. Think out a way to build a dataset with the relationship between postcode & sa2  
3. With the sa2 shape file, add the features about sa2 to the `domain_data` by determining if the property location is within the sa2 shape (the original `domain_data` only had the post code)  

by Ximing Wan:  
1. Find a shape file which describes Australian postcode boundaries
2. Write the code to download this shape file. 
3. Preprocess this shape file.
4. Draw the geopatial plot to reflect the distribution of rent prices across Victoria using the postcode shape files.  

by Suhui Tu:  
1. think about whether population forecast uses population growth rate calculated in the past few years to predict the present and future, or whether it finds future population data.
2. try to find population forecast sa2 (but fail), use linear regression to predict future population (but fail), and integrate two population related datasets to predict population future population (but fail).  
3. Write (part of) code for `population_data_processing`

by Xiaoqing Lei:  
1. process the external dataset `personal income`, including filtering out the districts of Victoria, calculating personal income using the number of earners and total income for each sa2, and calculating the rate of growth of personal income.  
2. visualisation of the processed data, drawing a bar plot for the 10 districts with the highest income growth rates.  



## 9th meeting
**Time**: 9.13, Wednesday, 12:00 ~ 19:00, 21:00 ~ 2:00a.m.  
**Lcoation**: 93 Flemington Road  
**People**: 
1. Zihan Yin
2. Ximing Wan
3. Suhui Tu
4. Xiaoqing Lei

**What we've done**:  
by Zihan Yin:  
1. Modify `4-import_json_files_and_combine.ipynb` with respect to all the crawled domain data (debug).
2. Create `5-merge.ipynb`, which includes:
    - Add features about as2 to `domain_data` using sa2 shape file
    - Create the dataset `postcode_sa2_relationship`, which describes the relationship between postcodes & sa2
    - Create the df `sa2_crime_rate` using `sa2_population` & `postcode_crime_count`
    - Create the dataset `sa2_info` using `sa2_personal income`, `sa2_population` & `sa2_crime_rate`
    - Merge `domain_data` & `sa2_info` to create `merged_data`  
3. a little bit modification on `population_data_processing`

by Ximing Wan:  
1. Scape all the domain data (about 9 thousand instances)
2. Write code to download a shape file which describes Australian sa2 boundaries
3. Preprocessed this shape file.
4. Draw the geopatial plot to reflect the distribution of rent prices across Victoria using the sa2 shape files.  

by Suhui Tu:  
1. complete `population_data_processing` to determine the population growth rate calculated using the past population from 2001 to 2021 to predict the population data from 2021 to the next five years.
2. selected the top 5 Victoria sa2 districts in the population dataframe to plot the predicted population profile 
3. attempt to plot the population distribution using geopatial plot

by Xiaoqing Lei:  
1. found that some values in personal income are very strange values, such as NaN, so check the dataframe one by one to convert the strange values such as np, NaN, inf, etc. to 0.
2. draw geospatial plot of the locations of schools.



## 10th meeting
**Time**: 9.14, Thursday, 14:00 ~ 1:00a.m.  
**Lcoation**: 93 Flemington Road  
**People**: 
1. Zihan Yin
2. Ximing Wan

**What we've done**:  
- Discuss prediction of future & OpenRouteService API

by Zihan Yin:  
1. Refine & adjust on `5-merge.ipynb` (debug)
2. Manage the files in the github repository and numbered the `.py` and `.ipynb` files in running order.

by Ximing Wan:  
1. Write the code that can find out the nearest facility (e.g. school station etc.) for each property and calculate the distance.
2. Write the code that downloads the PTV train station shape file.
3. Draw the geopatial plot to reflect the distribution of number of rental properties across Victoria using the sa2 shape files.



## 11th meeting
**Time**: 9.15, Friday, 10:00~12:00  
**Lcoation**: peter hall  
**People**: 
1. Zihan Yin
2. Ximing Wan
3. Suhui Tu
4. Xiaoqing Lei

**What we've done**:  
- Attend the workshop
- Solve some problems with the help of tutor
- Discuss with other groups about external datasets & prediction



## 12th meeting
**Time**: 9.15, Thursday, 13:00 ~ 18:00
**Lcoation**: 93 Flemington Road  
**People**: 
1. Zihan Yin
2. Ximing Wan
3. Suhui Tu
4. Xiaoqing Lei

**What we've done**:  
- Plan the future work & manage the github repository

by Zihan Yin:  
1. Write week 8 meeting minute markdown file

by Ximing Wan:  
1. Write the code which can scape all the shopping center locations of Victoria
2. Aid in debugging and writing code for downloading

by Suhui Tu:  
1. Write the code that downloads the external dataset `park_locations`

by Xiaoqing Lei:  
1. Modify the codes for `personal_income` & `school_location` to make them work in an updated python environment (debug).
2. Write the code that downloads the external dataset `hospital_locations`