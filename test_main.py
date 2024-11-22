import pytest
from mylib.extract_transform_load import extract_data, transform, transform_load_data
from mylib.query import sql_query
from pyspark.sql import SparkSession


# Pytest fixture for Spark session
@pytest.fixture(scope="module")
def spark():
    """Fixture to initialize and tear down a Spark session."""
    session = SparkSession.builder.appName("TestApp").getOrCreate()
    yield session
    session.stop()


def test_extract_data(spark):
    """Test the data extraction process."""
    df = extract_data(
        url="https://github.com/nogibjj/MiniWeek10/raw/refs/heads/main/data/unisex_names_table.csv",
        download_path="/dbfs/tmp/unisex_names_table.csv",
        file_path="/tmp/unisex_names_table.csv",
    )
    assert df is not None
    assert df.count() > 0  # Ensure the DataFrame contains data


def test_transform(spark):
    """Test the data transformation process."""
    df = extract_data(
        url="https://github.com/nogibjj/MiniWeek10/raw/refs/heads/main/data/unisex_names_table.csv",
        download_path="/dbfs/tmp/unisex_names_table.csv",
        file_path="/tmp/unisex_names_table.csv",
    )
    transformed_df = transform(df)
    assert transformed_df is not None
    assert "Gender_Category" in transformed_df.columns  # Ensure new column is added
    assert transformed_df.count() == df.count()  


def test_transform_load_data(spark):
    """Test the loading of transformed data into a Delta table."""
    df = extract_data(
        url="https://github.com/nogibjj/MiniWeek10/raw/refs/heads/main/data/unisex_names_table.csv",
        download_path="/dbfs/tmp/unisex_names_table.csv",
        file_path="/tmp/unisex_names_table.csv",
    )
    transformed_df = transform(df)
    transform_load_data(transformed_df)

    # Check if the Delta table is created and contains data
    result = spark.sql("SELECT COUNT(*) AS count FROM unisex_names_delta")
    assert result.collect()[0]["count"] > 0


def test_sql_query(spark):
    """Test the SQL query execution."""
    # Ensure the Delta table exists before running the query
    spark.sql("SELECT * FROM unisex_names_delta").collect()

    # Run the SQL query
    result = sql_query(spark)
    assert result is not None
    assert result.count() > 0  # Ensure the query returns results


if __name__ == "__main__":
    pytest.main()

