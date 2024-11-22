[![CI](https://github.com/UzoUwaz/UzoMiniWeek11/actions/workflows/cicd.yml/badge.svg)](https://github.com/UzoUwaz/UzoMiniWeek11/actions/workflows/cicd.yml)

# IDS 706 Mini Project 11 - PySpark Data Processing in DATABRICKS

### 🏗️ Requirements
- Use PySpark to perform data processing on a large dataset
- Include at least one Spark SQL query and one data transformation
- Get this to run successfully in a databricks environment 

### 📂 Project Structure
```
├── .devcontainer
│   └── Dockerfile
│   └── devcontainer.json
├── Makefile
├── README.md
├── data
│   └── unisex_names_tables.csv
├── main.py
├── mylib
│   ├── __init__.py
│   └──extract_transform_load.py and query.py
├── pyspark_output.md
├── requirements.txt
└── test_main.py
```

### 🛠️ Setup Instructions
#### 1. Clone the Repository
```
git clone https://github.com/UzoUwaz/UzoMiniWeek11.git
cd UzoMiniWeek11
```

#### 2. Install Dependencies
```
pip install -r requirements.txt
```

#### 3. Download and set up Apache Spark.
- Download Apache Spark and choose the version compatible with your project.
- Extract the Spark package and set the environment variables if necessary. Refer to the Spark documentation for guidance.
- If this does not work you can also run in GitHub CodeSpaces which has a native PySpark Environment. 

#### 4.	Run the Project:
Refer to the Usage section for running specific scripts or modules.

### 📊 Dataset Description
The data for this project comes from the biopics.csv dataset provided by FiveThirtyEight.

The dataset has the following features:
- ID
- name
- total
- male share
- female share
- gap 

### 🗃️ Spark SQL Query
I constructed a query to select data from certain variables 



More detailed information can be found [in this output markdown file](pyspark_output.md).

## Example Output Below 


|    |   ID | name    |    total |   male_share |   female_share |       gap |
|---:|-----:|:--------|---------:|-------------:|---------------:|----------:|
|  0 |    1 | Casey   | 176544   |     0.584287 |       0.415713 | 0.168573  |
|  1 |    2 | Riley   | 154861   |     0.507639 |       0.492361 | 0.0152781 |
|  2 |    3 | Jessie  | 136382   |     0.477834 |       0.522166 | 0.0443315 |
|  3 |    4 | Jackie  | 132929   |     0.421133 |       0.578867 | 0.157735  |
|  4 |    5 | Avery   | 121797   |     0.335213 |       0.664787 | 0.329574  |
|  5 |    6 | Jaime   | 109870   |     0.561793 |       0.438207 | 0.123586  |
|  6 |    7 | Peyton  |  94896.4 |     0.433719 |       0.566281 | 0.132561  |
|  7 |    8 | Kerry   |  88963.9 |     0.483949 |       0.516051 | 0.0321023 |
|  8 |    9 | Jody    |  80400.5 |     0.352068 |       0.647932 | 0.295864  |
|  9 |   10 | Kendall |  79210.9 |     0.372367 |       0.627633 | 0.255267  |
