# 2023-09 Victoria Real Estate Analysis and Prediction

An end-to-end data science project analyzing internal and external drivers of rental prices across Victoria, Australia. The project includes web scraping, data preprocessing, geospatial integration, exploratory data analysis, and predictive modeling.

📄 **中文版请见**: [`README.zh.md`](README.zh.md)  
📑 **Project Presentation Slide (.pdf)** is located [here](Project_Presentation_Slide).

---

## Project Objective

This consulting-style project investigates the determinants of rental prices in Victoria, Australia, with the goal of guiding investment and policy decisions. The analysis leverages both **internal** property features and **external** socio-economic and geographic indicators.

### Research Questions

1. **What are the most important internal and external features in predicting rental prices?**  
2. **What are the top 10 suburbs with the highest predicted growth rate?**  
3. **What are the most liveable and affordable suburbs according to your chosen metrics?**

---

## 🗂️ Project Structure

```plaintext
├── data/
│   ├── landing/               # Raw scraped and downloaded datasets
│   │   ├── domain_data/       # Internal property listings (e.g., Domain.com.au)
│   │   └── external_data/     # External datasets (e.g., hospitals, crime, income, schools)
│   ├── raw/                   # Partially cleaned data after initial filtering
│   │   ├── domain_data/
│   │   └── external_data/
│   ├── curated/               # Fully cleaned datasets for merging and modeling
│   │   ├── domain_data/
│   │   ├── external_data/
│   │   ├── merged_data/
│   │   └── final_data/
│   └── test/                  # Test samples and interim results
│       ├── json_files/
│       └── school_location.csv
├── scripts/                   # Python scripts (scraping, downloading shapefiles, etc.)
│   ├── 2.1-scrape_domain.py
│   ├── 2.2-scrape_shoppingmall.py
│   └── 3-download_shapefiles.py
├── notebooks/                 # Jupyter notebooks (analysis, EDA, geoplots)
│   ├── 0-create_folder.ipynb
│   ├── 4-import_json_files_and_combine.ipynb
│   ├── 5-merge.ipynb
│   ├── 6-property_analysis.ipynb
│   ├── 7.1-geoplot-postcode.ipynb
│   ├── 7.2-geoplot-SA2.ipynb
│   ├── 7.3-geoplot-count.ipynb
│   ├── 9-geoplot_for_facility.ipynb
│   ├── 10-preprocessing_for_prediction.ipynb
│   ├── 11-external_analysis.ipynb
│   ├── 13-project_summary.ipynb
│   └── external-book/
│       ├── 1.1-download_preprocess_population.ipynb
│       ├── 1.2-download_preprocess_crime_count.ipynb
│       ├── 1.3-download_preprocess_personal_income.ipynb
│       ├── 1.4-download_preprocess_school.ipynb
│       ├── 8.1-add_closest_school.ipynb
│       ├── 8.2-add_closest_hospital.ipynb
│       ├── 8.3-add_closest_shopping_centre.ipynb
│       ├── 8.4-add_closest_parks.ipynb
│       ├── 8.5-add_closest_station.ipynb
│       ├── 8.6-openrouteservice_PTV.ipynb
│       └── 8.7-add_CBD_distance.ipynb
├── modeling/                 # Jupyter notebooks (for modeling)
│   ├── m1_convert_to_modelling_data.ipynb
│   ├── m2_linear_models.ipynb
│   └── m3_rf&knn&neural-models.ipynb
├── README.md
```

> ⚠️ **Note**  
> 1. All datasets under the `data/` directory are stored in the archive `data.7z`. You need to extract the contents to use the project properly.  
> 2. Datasets under `data/landing/external_data/` exceed GitHub’s file size limit (100MB) even after compression and are therefore **not included in `data.7z`**. Please download or prepare them manually from the data sources if needed. You can also use the raw and curated versions of them, which are archived in `data.7z`.

---

## 🔧 Technologies & Tools

- **Languages**: Python, Jupyter Notebook  
- **Libraries**: Pandas, NumPy, Scikit-learn, Seaborn, GeoPandas, Matplotlib, Shapely, Requests, BeautifulSoup  
- **Geospatial Tools**: GeoPandas, Shapefiles, OpenRouteService  
- **Web Scraping**: `requests`, `BeautifulSoup`, `.json` parsing from Domain.com.au and other sites  
- **Modeling**: Linear Regression, Random Forest, KNN, Neural Networks  

---

## 🔁 Workflow Overview

### 0. Project Initialization
- `0-create_folder.ipynb`: Create necessary directory structure under `data/`.

### 1. External Data Collection & Preprocessing
- Population: `1.1-download_preprocess_population.ipynb`
- Crime Stats: `1.2-download_preprocess_crime_count.ipynb`
- Personal Income: `1.3-download_preprocess_personal_income.ipynb`
- Schools: `1.4-download_preprocess_school.ipynb`

### 2. Web Scraping
- Rental listings from Domain.com.au: `2.1-scrape_domain.py`
- Shopping mall locations: `2.2-scrape_shoppingmall.py`

### 3. Shapefiles Download
- Administrative and infrastructure boundaries: `3-download_shapefiles.py`

### 4. Internal Data Preprocessing
- Convert `.json` listings to structured format: `4-import_json_files_and_combine.ipynb`

### 5. Data Integration
- Merge internal and external datasets using SA2 and postcode levels: `5-merge.ipynb`

### 6. Exploratory Data Analysis
- Feature correlation analysis: `6-property_analysis.ipynb`
- Geospatial visualization: `7.x-geoplot-*.ipynb`, `9-geoplot_for_facility.ipynb`

### 7. Feature Engineering: Proximity Measures
- Add distances to closest school, hospital, station, CBD, shopping mall, park: `8.x-add_closest_*.ipynb`, `8.6-openrouteservice_PTV.ipynb`

### 8. Data Preparation for Modeling
- Clean and reduce final dataset: `10-preprocessing_for_prediction.ipynb`
- Feature selection: `m1_convert_to_modelling_data.ipynb`

### 9. Predictive Modeling
- Linear models & GLMs: `m2_linear_models.ipynb`
- Tree-based, KNN & neural models: `m3_rf&knn&neural-models.ipynb`

### 10. External Feature Impact Analysis
- Correlation between external features and rental prices: `11-external_analysis.ipynb`

### 11. Final Deliverable
- Project summary and visual dashboard: `13-project_summary.ipynb`

---

## 📊 Modeling & Evaluation

- Trained on curated data using multiple traditional machine learning algorithms.
- Feature importance and prediction scores evaluated.
- Predictions extended to future years (e.g., 2026 forecast).

---

## 📎 Contributors & Roles

| Name         | Major Contributions                                                         |
|--------------|------------------------------------------------------------------------------|
| **Zihan Yin** | Pipeline integration, property data preprocessing, modeling, EDA, final report |
| Ximing Wan   | Scraping, modeling, geoplots, external feature analysis                     |
| Xiaoqing Lei | External data preprocessing, proximity analysis                             |
| Suhui Tu     | Crime/school data processing, geospatial files                              |

---

## 📚 Data Sources

- [Domain.com.au](https://www.domain.com.au/) – Rental property listings  
- [Australian Bureau of Statistics](https://www.abs.gov.au/) – Income, population data  
- [Data.Vic](https://www.data.vic.gov.au/) – Crime, school locations, and shapefiles  
- [OpenRouteService](https://openrouteservice.org/) – Walking distance computation API  
- [Australia Shopping Directory](https://australia-shoppings.com/) – Shopping mall locations  
- [Victorian Schools Location Dataset](https://discover.data.vic.gov.au/dataset/school-locations)  
- [PTV Open Data](https://www.ptv.vic.gov.au/footer/data-and-reporting/datasets/) – Train station and transit data

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).

---

_Project completed as part of MAST30034 Applied Data Science at the University of Melbourne, Semester 2, 2023._
