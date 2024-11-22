from mylib.extract_transform_load import extract_data, transform, transform_load_data
from mylib.query import sql_query
from pyspark.sql import SparkSession
from databricks.sdk.runtime import spark


if __name__ == "__main__":
    # Start a Spark session
    session = SparkSession.builder.appName("unisexNamesPipeline").getOrCreate()

    # Extract data
    df = extract_data()
    
    # Transform the data
    df = transform(df)
    print("Transformed DataFrame with new column 'Gender_Category':")
    df.show()
    
    # Load transformed data into a Delta table
    transform_load_data(df)
    
    # Run a SQL query on the Delta table
    print("Result of the SQL query:")
    sql_query(session)
