from pyspark.sql.functions import col, hour, dayofweek


def clean(df):
    """Remove trips with zero distance or amount"""
    return df.filter((col("trip_distance") > 0) & (col("total_amount") > 0))


def add_features(df):
    """Remove trips with zero distance or amount"""
    return df.withColumn("pickup_hour", hour(col("tpep_pickup_datetime"))).withColumn(
        "pickup_weekday", dayofweek(col("tpep_pickup_datetime"))
    )
