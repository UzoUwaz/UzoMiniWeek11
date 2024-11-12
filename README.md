[![CI](https://github.com/nogibjj/MiniWeek10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/MiniWeek10/actions/workflows/cicd.yml)

# IDS 706 Mini Project 10 - PySpark Data Processing

### 🏗️ Requirements
- Use PySpark to perform data processing on a large dataset
- Include at least one Spark SQL query and one data transformation

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
│   └── lib.py
├── pyspark_output.md
├── requirements.txt
└── test_main.py
```

### 🛠️ Setup Instructions
#### 1. Clone the Repository
```
git clone git@github.com:nogibjj/MiniWeek10.git
cd MiniWeek10
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


+---+-------+-------------+-----------------+-----------------+------------------+----------------+
| ID|   name|        total|       male_share|     female_share|               gap| Gender_Category|
+---+-------+-------------+-----------------+-----------------+------------------+----------------+
|  1|  Casey|176544.328149|0.584286566204162|0.415713433795838| 0.168573132408324|  Primarily Male|
|  2|  Riley|154860.665173|0.507639071226889|0.492360928773111|0.0152781424537786|  Primarily Male|
|  3| Jessie|136381.830656| 0.47783426831522| 0.52216573168478|  0.04433146336956|Primarily Female|
|  4| Jackie| 132928.78874|0.421132601798505|0.578867398201495|  0.15773479640299|Primarily Female|
|  5|  Avery|121797.419516|0.335213073103216|0.664786926896784| 0.329573853793568|Primarily Female|
|  6|  Jaime| 109870.18729|0.561792900862907|0.438207099137093| 0.123585801725814|  Primarily Male|
|  7| Peyton| 94896.395216|0.433719376329487|0.566280623670513| 0.132561247341027|Primarily Female|
|  8|  Kerry|  88963.92625|0.483948843602212|0.516051156397788|0.0321023127955753|Primarily Female|
|  9|   Jody| 80400.519199|0.352068031749129|0.647931968250871| 0.295863936501742|Primarily Female|
| 10|Kendall| 79210.873961|0.372366742002144|0.627633257997856| 0.255266515995713|Primarily Female|
| 11| Payton| 64151.630388|0.334357683090347|0.665642316909653| 0.331284633819305|Primarily Female|
| 12| Skyler| 53486.390419|0.646053060924541|0.353946939075459| 0.292106121849082|  Primarily Male|
| 13|Frankie| 51288.068109|0.623671255310686|0.376328744689314| 0.247342510621372|  Primarily Male|
| 14|    Pat| 44781.602373|0.369034384641938|0.630965615358062| 0.261931230716124|Primarily Female|
| 15|  Quinn| 41920.940058|0.635741932197297|0.364258067802703| 0.271483864394595|  Primarily Male|
| 16| Harley| 41237.565743| 0.57170175193966| 0.42829824806034|  0.14340350387932|  Primarily Male|
| 17|  Reese| 36360.520613|0.361910288553326|0.638089711446674| 0.276179422893347|Primarily Female|
| 18| Robbie| 32636.047648|0.553156938754081|0.446843061245919| 0.106313877508162|  Primarily Male|
| 19| Tommie| 29528.793818|0.664437749808803|0.335562250191197| 0.328875499617605|  Primarily Male|
| 20|Justice|  27350.56457|0.528194955830851|0.471805044169149|0.0563899116617029|  Primarily Male|
+---+-------+-------------+-----------------+-----------------+------------------+----------------+
