from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, approx_count_distinct, expr, window, to_timestamp
from pyspark.sql.types import StructType, StringType, IntegerType

# Initialize Spark session with Kafka package
spark = SparkSession.builder \
    .appName("KafkaPySparkStream") \
    .master("local[*]") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1") \
    .getOrCreate()

# Define schema for user activity data
schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("action", StringType()) \
    .add("timestamp", IntegerType())  # The timestamp is initially an integer (epoch time)

# Read stream from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "user-activity") \
    .load()

# Parse Kafka stream and convert to structured format
parsed_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Convert the integer timestamp (epoch) to TimestampType
parsed_df = parsed_df.withColumn("timestamp", to_timestamp(col("timestamp")))

# Perform transformations (e.g., calculate active users per minute using approx_count_distinct)
active_users_df = parsed_df \
    .withWatermark("timestamp", "1 minute") \
    .groupBy(window(col("timestamp"), "1 minute"), "action") \
    .agg(approx_count_distinct("user_id").alias("active_users"))

# Show active users on the console in real-time
query = active_users_df.writeStream \
    .outputMode("update") \
    .format("console") \
    .start()

# Await termination
query.awaitTermination()

