"""
library functions
"""

import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType,
)

LOG_FILE = "pyspark_output.md"


def log_output(operation, output, query=None):
    """Adds output to a markdown file."""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query:
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is:\n\n")
        file.write(output)
        file.write("\n\n")


def start_spark(appName="UnisexNamesApp"):
    """Start Spark session."""
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark


def end_spark(spark):
    """Stop Spark session."""
    spark.stop()
    return "Stopped Spark session"


def extract(
    url="",
    file_path="data/unisex_names_table.csv",
    directory="data",
):
    """Extract a URL to a file path only if the file is a CSV."""
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Download content from the URL
    with requests.get(url) as r:
        content = r.text

        # Check if the content is valid CSV
        if "name" in content and "total" in content:
            with open(file_path, "w") as f:
                f.write(content)
            print(f"File successfully downloaded as {file_path}")
        else:
            print("Error: The downloaded content is not a valid CSV file.")
            raise ValueError("The downloaded file is not a valid CSV.")

    return file_path


def load_data(spark, data="data/unisex_names_table.csv", name="unisexdb"):
    """Load data into a Spark DataFrame."""
    schema = StructType(
        [
            StructField("ID", IntegerType(), True),
            StructField("name", StringType(), True),
            StructField("total", IntegerType(), True),
            StructField("male_share", DoubleType(), True),
            StructField("female_share", DoubleType(), True),
            StructField("gap", DoubleType(), True),
        ]
    )

    df = spark.read.option("header", "true").schema(schema).csv(data)

    # Register DataFrame as a temporary view
    df.createOrReplaceTempView(name)
    log_output("load data", df.limit(10).toPandas().to_markdown())

    return df


def query(spark, df, query, name="unisexdb"):
    """Run a Spark SQL query."""
    df.createOrReplaceTempView(name)
    result_df = spark.sql(query)
    log_output("query data", result_df.limit(10).toPandas().to_markdown(), query)
    return result_df.show()


def describe(df):
    """Describe statistics of the DataFrame."""
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)
    return df.describe().show()


def example_transform(df):
    """Example transformation for the unisex names dataset."""
    # Create a new column to categorize by gender share dominance
    df = df.withColumn(
        "Gender_Category",
        when(col("male_share") > 0.5, "Primarily Male")
        .when(col("female_share") > 0.5, "Primarily Female")
        .otherwise("Neutral"),
    )

    log_output("transform data", df.limit(10).toPandas().to_markdown())
    return df.show()
