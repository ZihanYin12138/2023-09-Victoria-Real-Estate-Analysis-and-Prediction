# This is the ORIGINAL `README.md`.

# MAST30034 Project 2 README.md

## Data Description
Structure:
- `../data/landing/`
    - `../data/landing/domain_data/`
    - `../data/landing/external_data/`
- `../data/raw/`
    - `../data/raw/domain_data/`
    - `../data/raw/external_data/`
- `../data/curated/`
    - `../data/curated/domain_data/`
    - `../data/curated/external_data/`
    - `../data/curated/merged_data/`
    - `../data/curated/final_data/`
- `../data/test/`
    - `../data/test/json_files` (for test in very beginning)
    - `../data/test/school_location.csv`

1. `../data/landing/`: This landing data folder serves as all the data which scrape and download from the website, this folder include the internal dataset about the property(domain.com) and external dataset might affect the rental prices(including hospitals, personal income, schools, population,offence count...)
2. `../data/raw/`: The raw data folder consists of two subfiles including internal dataset and external dataset contains data that has been moved from the landing folder but has been do some partial processing for each landing file(feature selection, Replace with Default Values).
3. `../data/curated/`: The curated data folder contains processed data that is ready for analysis and used in project.
    - `../data/curated/domain_data/`: This fold stores `domain_data.csv`, which has been done in preprocessing.
    - `../data/curated/external_data/`: This fold stores external datasets, which has been done in preprocessing.
    - `../data/curated/merged_data/`: This fold stores the data merged by `domain_data.csv` & external datasets by sa2.
    - `../data/curated/final_data/`: This fold stores the data used in analysis & prediction.
4. `../data/test/`: This test folder is used to store data sets in github and data samples for various test scenarios.

## Code Run Order
0. `0-create_folder.ipynb`:  
    This `.ipynb` generates the folders for the further subsequent runnings. The folders are generated in the directory `../data/`. 
     
    Allocation: Zihan Yin 1/1


1. download & preprocess 4 external datasets:  

    `1.1-download_preprocess_population.ipynb`:  
    Pre-processing SA2 Population Data (Victoria). The SA2 population data for Victoria is cleaned, transformed, and shown in this notebook.  

    `1.2-download_preprocess_crime_count.ipynb`:  
    This file will download the offence record vic, preprocess the data and find the total offence count in each sa2 district.
    
    `1.3-download_preprocess_personal_income.ipynb`:  
    This file will download the dataset with Total income - Number of earners, median age of earners, sum , median , mean   by sa2, 2015-16 to 2019-20. Preprocess the dataset and calculate the growth rate of personal income annully, then calculate the future personal income through the average annual personal income growth rate.

    `1.4-download_preprocess_school.ipynb`:  
    This file will download the dataset with the school in victoria. preprocessing the dataset and Using the shapefile of victoria to draw the plot of the distribution of the schools.

    Allocation: Xiaoqing Lei 3/4, Suhui Tu 1/4


2. download domain data & 1 external dataset by scraping:  

    `2.1-scrape_domain.py`:  
    This file will scrape all rental properties information from every suburbs in Victoria Australia by postcode. 
    
    `2.2-scrape_shoppingmall.py`:  
    This file will scrape all shopping mall location from the website: australia-shoppings.com. 

    Allocation: Ximing Wan 2/2


3. `3-download_shapefiles`:  
    This `.py` downloads 4 external shape files:  
    1. VIC sa2 boundary shape file   
    2. VIC postcode boundary shape file   
    3. PTV train station shape file  
    4. VIC park shape file    

    Allocation: Ximing Wan 3/4, Suhui Tu 1/4


4. `4-import_json_files_and_combine.ipynb`:  
    This `.ipynb`:  
    - 1. Import all json files from `data/landing/domain_data/`, then combine together as a pd dataframe
    - 2. preprocessing for raw `domain_data`  

    Allocation: Zihan Yin 1/1

5. `5-merge.ipynb`:  
    This `.ipynb`:  
    - 1. Add 'sa2_code' & 'sa2_name' to `domain_data`, using the shape file `VIC_SA2`
    - 2. Create the dataset `postcode_sa2_relationship`, which describes the relationship between postcodes & sa2
    - 3. Create the dataset `sa2_info`, using the 4 external datasets
    - 4. Merge `domain_data` & `sa2_info` to create `merged_data` 

    Allocation: Zihan Yin 1/1

6. `6-property_analysis.ipynb` (by Zihan Yin):  
    This `.ipynb`:   
    - 1. Correlation of continuous property features
    - 2. Correlation of discrete property features 

    Allocation: Zihan Yin 1/1

7. 3 geoplots:

    `7.1-geoplot-postcode.ipynb`:  
    This file will draw the geo-plot for average rental price in each suburbs according to the postcode for the whole Victoria State.
    
    `7.2-geoplot-SA2.ipynb`:  
    This part will draw the geo-plot for average rental price in each suburbs according to the SA2 for the whole Victoria State. 
    
    `7.3-geoplot-count.ipynb`:  
    This part will draw the geo-plot for the amount of properties in each suburbs according to the sa2 for the whole Victoria State.
    
     Allocation: Ximing Wan 3/3


8. 6 external datasets about facilities:

    `8.1-add_closest_school.ipynb`:  
    This file will find the closest school (straight-line distance) for each properties as the extra features, store school location & distance. 
    
    `8.2-add_closest_hospital.ipynb`:  
    This file will find the closest hospital (straight-line distance) for each properties as the extra features, store location & distance. 
    
    `8.3-add_closest_shopping_centre.ipynb`:  
    This file will find the closest mall (straight-line distance) for each properties as the extra features, store location & distance.  
    
    `8.4-add_closest_parks.ipynb`:  
    This file will find the closest park (straight-line distance) for each properties as the extra features, store location & distance. 
    
    `8.5-add_closest_station.ipynb`:  
    This file will find the closest train station (straight-line distance) for each properties as the extra features, store location & distance.  
    
    `8.6-openrouteservice_PTV.ipynb`:  
    This file will find the closest train station in foot walking for each properties by using Open Route Service.
    
    `8.7-add_CBD_distance.ipynb`:  
    This file will calculate the straight-line distance between properties and CBD.  

    Allocation: Ximing Wan 6/12, Xiaoqing Lei 3/12, Suhui Tu 2/12, Zihan Yin 1/12


9. `9-geoplot_for_facility.ipynb`:  
    This `.ipynb` draws:   
    - 1. geopatial plot for hospitals
    - 2. geopatial plot for schools
    - 3. geopatial plot for shopping centres 
    - 4. geopatial plot for parks
    - 5. geopatial plot for train station
    - 6. geopatial for personal income
    - 7. geopatial for population
    - 8. geopatial for population density
    - 9. geopatial for crime rate
    - 10. geopatial for offence count

    Allocation: Zihan Yin 1/1

10. `10-preprocessing_for_prediction`:  
    This `.ipynb`:   
    - 1. Convert 'population' to 'population_density'
    - 2. Calculate "2023 personal income"
    - 3. overwrite 'crime_rate' by 'offence_count'
    - 4. Reduction for merged data
    - 5. Extra preprocessing for `merged_data_2023` to solve the problem of bad prediction performance
    - 6. Build the data `merged_data_2026`

    Allocation: Zihan Yin 1/1


11. `11-external_analysis.ipynb`:  
    The file will try to find the potential correlation between external features and the properties' rental price by drawing heat maps and pair plots.

    Allocation: Ximing Wan 1/1


12. modelling codes for price prediction:

    `m1_convert_to_modelling_data`: The file will do feature selection to convert the pre-processed data to modelling data.
    
    `m2_linear_models.ipynb`: The file will build a simple linear model as the baseline, and several different General Linear Model(GLM) for prediction.  
    
    `m3_rf&knn&neural-models.ipynb`: The file will build Random Forest Regression and KNN and Neural Network Models for prediction.

    Allocation: Ximing Wan 3/3


13. `13-project_summary.ipynb`:  
    This `.ipynb` summarise the whole project. This is the basis of outline & content for the PowerPoint:
    - 0. Introduction to group
    - 1. Dataset Overview & Introduction 
    - 2. Visualise to find the most important features 
    - 3. Forecast to find the top 10 suburbs with the highest predicted growth rate 
    - 4. Design a metric to find the most livable & affordable suburbs 
    - 5. Recommendations 
    - 6. Additional Insights 
    - 7. Reflection 

    Allocation: Zihan Yin 7/8, Ximing Wan 1/8
