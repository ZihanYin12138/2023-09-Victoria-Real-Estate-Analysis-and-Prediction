# 2023-09 维多利亚省租房价格分析与预测项目

该项目是一个综合性数据科学项目，分析了澳大利亚维多利亚省租房价格的内部因素和外部因素。项目包括网页爬虫，数据预处理，地理信息融合，探索性数据分析，以及预测模型构建。  
  
📄 **English version**: [`README.md`](README.md)  
📑 **项目演示文件**：[Project\_Presentation\_Slide.pdf](Project_Presentation_Slide.pdf)  

---

## 项目目标

本项目以项目顾问的形式，探索影响维多利亚省租房价格的各种因素，目的是为投资与政策决策提供数据支持。分析包括了房产内部特征和社会经济、地理等外部指标。

### 研究问题

1. **对租房价格预测最关键的内部和外部特征是什么？**
2. **未来租量预期增长率最高的前10个地区是哪些？**
3. **根据选定的指标，哪些地区最兼顺居住和价格合理？**

---

## 🗂️ 项目相关结构

```plaintext
├─ data/
│   ├─ landing/               # 原始爬虫或下载的数据
│   │   ├─ domain_data/       # 房产类内部数据
│   │   └─ external_data/     # 外部数据（医院，罪网，收入，学校等）
│   ├─ raw/                   # 初步清洗后的数据
│   │   ├─ domain_data/
│   │   └─ external_data/
│   ├─ curated/               # 完全清洗并可用于融合/预测的数据
│   │   ├─ domain_data/
│   │   ├─ external_data/
│   │   ├─ merged_data/
│   │   └─ final_data/
│   └─ test/                  # 测试样本和临时结果
│       ├─ json_files/
│       └─ school_location.csv
├─ scripts/                   # Python 脚本（爬虫，下载 shapefiles 等）
│   ├── 2.1-scrape_domain.py
│   ├── 2.2-scrape_shoppingmall.py
│   └── 3-download_shapefiles.py
├─ notebooks/                 # Jupyter notebooks（分析，EDA，地理图等）
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
├─ modeling/                  # 预测模型的 notebooks
│   ├── m1_convert_to_modelling_data.ipynb
│   ├── m2_linear_models.ipynb
│   └── m3_rf&knn&neural-models.ipynb
└─ README.md
```

> ⚠️ **注意**
>
> 1. `data/` 目录下所有数据集已装入在 `data.7z` 压缩包中，使用前请先解压。
> 2. `data/landing/external_data/` 目录下的数据集，即使压缩后仍超过 GitHub 文件上传限制（80-100MB），因此未包含在 `data.7z` 中，需要自行下载或准备。你也可以直接使用 `data.7z` 里已预处理的同名版本。

---

## 🔧 技术堆 & 工具

* **编程语言**：Python, Jupyter Notebook
* **库**：Pandas, NumPy, Scikit-learn, Seaborn, GeoPandas, Folium, Matplotlib, Shapely, Requests, BeautifulSoup
* **地理工具**：GeoPandas, shapefile, OpenRouteService
* **爬虫工具**：requests, BeautifulSoup, json 解析
* **模型**：线性图模型，随机森林，KNN，神经网络

---

## 🔁 工作流程概览

### 0. 项目初始化
- `0-create_folder.ipynb`：在 `data/` 目录下创建所需的文件夹结构

### 1. 外部数据收集与预处理
- 人口数据：`1.1-download_preprocess_population.ipynb`
- 犯罪统计：`1.2-download_preprocess_crime_count.ipynb`
- 个人收入：`1.3-download_preprocess_personal_income.ipynb`
- 学校信息：`1.4-download_preprocess_school.ipynb`

### 2. 网页数据爬取
- 从 Domain.com.au 获取租房信息：`2.1-scrape_domain.py`
- 商场位置信息：`2.2-scrape_shoppingmall.py`

### 3. Shapefile 下载
- 行政区划与基础设施边界数据：`3-download_shapefiles.py`

### 4. 内部数据预处理
- 将 `.json` 格式的房源信息转化为结构化表格：`4-import_json_files_and_combine.ipynb`

### 5. 数据整合
- 使用 SA2 和邮政编码（postcode）将内部与外部数据合并：`5-merge.ipynb`

### 6. 探索性数据分析（EDA）
- 特征相关性分析：`6-property_analysis.ipynb`
- 地理可视化分析：`7.x-geoplot-*.ipynb`、`9-geoplot_for_facility.ipynb`

### 7. 特征工程：距离计算
- 添加与最近学校、医院、车站、CBD、商场、公园的距离特征：`8.x-add_closest_*.ipynb`、`8.6-openrouteservice_PTV.ipynb`

### 8. 建模准备
- 清洗与精简最终数据集：`10-preprocessing_for_prediction.ipynb`
- 特征选择：`m1_convert_to_modelling_data.ipynb`

### 9. 预测建模
- 线性模型与广义线性模型（GLMs）：`m2_linear_models.ipynb`
- 树模型、KNN、神经网络模型：`m3_rf&knn&neural-models.ipynb`

### 10. 外部特征影响分析
- 分析外部特征与租金之间的相关性：`11-external_analysis.ipynb`

### 11. 最终交付成果
- 项目总结与可视化仪表盘：`13-project_summary.ipynb`

---

## 📊 预测模型与评估

* 培训数据使用已清洗数据集，应用多种经典机器学习算法
* 评估特征重要性和预测结果
* 将预测扩展到未来年份（例如 2026 年）

---

## 📌 项目成员与分工

| 姓名            | 主要贡献                         |
| ------------- | ---------------------------- |
| **Zihan Yin** | 数据流程整合，房产数据预处理，模型构建，EDA，最终报告 |
| Ximing Wan    | 爬虫，模型，地理图，外部因素分析             |
| Xiaoqing Lei  | 外部数据处理，地理近距分析                |
| Suhui Tu      | 罪网/学校数据处理，地理文件               |

---

## 📚 数据来源

* [Domain.com.au](https://www.domain.com.au/) — 租房信息
* [Australian Bureau of Statistics](https://www.abs.gov.au/) — 收入、人口等数据
* [Data.Vic](https://www.data.vic.gov.au/) — 罪网，学校，地理边界
* [OpenRouteService](https://openrouteservice.org/) — 步行距离计算 API
* [Australia Shopping Directory](https://australia-shoppings.com/) — 商场信息
* [Victorian Schools Location Dataset](https://discover.data.vic.gov.au/dataset/school-locations)
* [PTV Open Data](https://www.ptv.vic.gov.au/footer/data-and-reporting/datasets/) — 地铁站和交通数据

---

## 📄 协议

本项目以 [MIT License](LICENSE) 协议分发。

---

*本项目为墨尔本大学 MAST30034 Applied Data Science 课程 2023 年 S2 实习项目*。
