import sys

sys.path.append("/opt/spark/work-dir/src")

from common.spark_session import create_spark
from transformations import clean, add_features

spark = create_spark("TaxiETL2020")

input_path = "/data/raw/2020_Yellow_Taxi_Trip_Data.csv"
output_path = "/data/processed/taxi_2020"

# Step 1: Read CSV
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Step 2: Clean
df = clean(df)

# Step 3: Add features
df = add_features(df)

# Step 4: Write to Parquet
df.write.mode("overwrite").parquet(output_path)

spark.stop()
