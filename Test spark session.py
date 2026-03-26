import pyspark
print("PySpark file:", pyspark.__file__)

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkTest") \
    .master("local[*]") \
    .getOrCreate()

print("Spark version:", spark.version)

df = spark.range(10)
df.show()

spark.stop()