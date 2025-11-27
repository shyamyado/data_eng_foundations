from pyspark.sql import SparkSession


def create_spark(app_name="TaxiETL"):
    spark = (
        SparkSession.builder.appName(app_name)
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )
    return spark
