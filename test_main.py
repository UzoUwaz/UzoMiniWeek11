import os
import pytest
from pyspark.sql import SparkSession
from mylib.extract_transform_load import extract_data, transform, transform_load_data
from mylib.query import sql_query


# Pytest fixture for Spark session
@pytest.fixture(scope="module")
def spark():
    """Fixture to initialize and tear down a Spark session."""
    session = SparkSession.builder.appName("TestApp").getOrCreate()
    yield session
    session.stop()


@pytest.fixture(scope="module")
def setup_data(spark):
    """Fixture to extract and transform data, ensuring data is available for all tests."""
    # Adjust file paths to avoid issues with /dbfs/tmp
    download_path = "/tmp/unisex_names_table.csv"
    file_path = "/tmp/unisex_names_table.csv"

    # Extract data
    df = extract_data(
        url="https://github.com/nogibjj/MiniWeek10/raw/refs/heads/main/data/unisex_names_table.csv",
        download_path=download_path,
        file_path=file_path,
    )
    
    # Transform data
    transformed_df = transform(df)

    # Load into Delta table
    transform_load_data(transformed_df)

    return transformed_df


def test_extract_data():
    """Test the data extraction process."""
    download_path = "/tmp/unisex_names_table.csv"
    file_path = "/tmp/unisex_names_table.csv"
    df = extract_data(
        url="https://github.com/nogibjj/MiniWeek10/raw/refs/heads/main/data/unisex_names_table.csv",
        download_path=download_path,
        file_path=file_path,
    )
    assert df is not None
    assert df.count() > 0  # Ensure the DataFrame contains data


def test_transform(setup_data):
    """Test the data transformation process."""
    df = setup_data
    assert "Gender_Category" in df.columns  # Ensure the new column is added
    assert df.count() > 0  # Ensure no rows are lost during transformation


def test_transform_load_data(spark):
    """Test the loading of transformed data into a Delta table."""
    # Ensure the Delta table is created
    result = spark.sql("SELECT COUNT(*) AS count FROM unisex_names_delta")
    assert result.collect()[0]["count"] > 0


def test_sql_query(spark):
    """Test the SQL query execution."""
    # Ensure the query runs successfully
    result = sql_query(spark)
    assert result is not None
    assert result.count() > 0  # Ensure the query returns results


if __name__ == "__main__":
    pytest.main()

