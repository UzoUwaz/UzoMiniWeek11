"""
Main CLI or app entry point
"""

from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


def main():
    # Extract data
    extract()  # Downloads the unisex names CSV file

    # Start Spark session
    spark = start_spark("unisex_names_app")

    # Load data into DataFrame
    df = load_data(spark, data="data/unisex_names_table.csv", name="unisexdb")

    # Describe data to show summary statistics
    describe(df)

    # Example query (adjusted for unisex names dataset)
    query(
        spark,
        df,
        "SELECT * FROM unisexdb WHERE total > 10000 AND male_share > 0.5;",
        "unisexdb",
    )

    # Example transform
    example_transform(df)

    # End Spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
