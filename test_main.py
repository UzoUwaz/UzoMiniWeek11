import os
import pytest
from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


# Pytest fixture for Spark session
@pytest.fixture(scope="module")
def spark():
    spark = start_spark("TestApp")
    yield spark
    end_spark(spark)


def test_extract():
    file_path = extract()
    assert os.path.exists(file_path) is True


def test_load_data(spark):
    df = load_data(spark, data="data/unisex_names_table.csv", name="unisexdb")
    assert df is not None
    assert df.count() > 0  # Ensure data is loaded


def test_describe(spark):
    df = load_data(spark, data="data/unisex_names_table.csv", name="unisexdb")
    result = describe(df)
    assert result is None  # `describe()` function does not return a value


def test_query(spark):
    df = load_data(spark, data="data/unisex_names_table.csv", name="unisexdb")
    result = query(
        spark,
        df,
        "SELECT * FROM unisexdb WHERE total > 10000 AND male_share > 0.5;",
        "unisexdb",
    )
    assert result is None  # `query()` function does not return a value


def test_example_transform(spark):
    df = load_data(spark, data="data/unisex_names_table.csv", name="unisexdb")
    result = example_transform(df)
    assert result is None  # `example_transform()` function does not return a value


if __name__ == "__main__":
    pytest.main()
