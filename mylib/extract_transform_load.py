from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, when
import urllib.request


def extract_data(
    url="https://github.com/nogibjj/MiniWeek10/raw/refs/heads/main/data/unisex_names_table.csv",
    download_path="/dbfs/tmp/unisex_names_table.csv",
    file_path="/tmp/unisex_names_table.csv",
):
    """
    Extract data from a URL and return a PySpark DataFrame.
    """
    # Start a Spark session
    spark = SparkSession.builder.appName("unisexNamesPipeline").getOrCreate()
    
    # Download the file
    urllib.request.urlretrieve(url, download_path)
    print(f"File downloaded to {download_path}")
    
    # Read the CSV into a PySpark DataFrame
    return spark.read.csv(file_path, header=True, inferSchema=True)


def transform(df: DataFrame):
    """
    Perform transformations on the unisex names dataset.
    Adds a 'Gender_Category' column based on male_share and female_share values.
    """
    # Add a new column to categorize by gender share dominance
    df = df.withColumn(
        "Gender_Category",
        when(col("male_share") > 0.5, "Primarily Male")
        .when(col("female_share") > 0.5, "Primarily Female")
        .otherwise("Neutral"),
    )
    print("Transformation completed with new column 'Gender_Category'.")
    return df


def transform_load_data(df: DataFrame):
    """
    Transform column names and load the DataFrame into a Databricks Delta table.
    """
    spark = SparkSession.builder.appName("unisexNamesPipeline").getOrCreate()
    # Transform column names to remove spaces
    df = df.select([col(c).alias(c.replace(" ", "")) for c in df.columns])

    # Drop existing table if needed to avoid conflicts
    spark.sql("DROP TABLE IF EXISTS unisex_names_delta")

    # Enable schema merge and write to Delta table
    df.write.option("mergeSchema", "true").mode("overwrite").saveAsTable("unisex_names_delta")
    print("Data written to Databricks Delta table: 'unisex_names_delta'.")

    
    # Write the DataFrame as a Delta table
    df.write.option("mergeSchema", "true").mode("overwrite").saveAsTable("unisex_names_delta")
    print("Data written to Databricks Delta table: 'unisex_names_delta'.")
