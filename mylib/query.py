from pyspark.sql import SparkSession


def sql_query(spark: SparkSession):
    """
    Perform a Spark SQL query on the unisex_names_delta table and return the result.
    """
    # Query the Delta table
    result = spark.sql(
        """
        SELECT name, total, Gender_Category
        FROM unisex_names_delta
        WHERE total > 10000 AND Gender_Category = 'Primarily Male'
        ORDER BY total DESC
        """
    )

    # Print results (optional)
    print("Query results:")
    result.show()

    # Return the resulting DataFrame for further validation
    return result