from pyspark.sql import SparkSession


def sql_query(spark: SparkSession):
    """
    Perform a Spark SQL query on the unisex_names_delta table.
    """
    # Run a SQL query to filter and process the data
    result = spark.sql(
        """
        SELECT name, total, Gender_Category
        FROM unisex_names_delta
        WHERE total > 10000 AND Gender_Category = 'Primarily Male'
        ORDER BY total DESC
        """
    )
    
    # Display the results
    print("Query results:")
    result.show()
