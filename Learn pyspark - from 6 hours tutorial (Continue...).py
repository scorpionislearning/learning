from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

if __name__ == "__main__":

    spark = SparkSession.builder.appName("Learning Spark").getOrCreate()

    df = spark.read.format('csv')\
        .option('inferSchema',True)\
        .option('header',True)\
        .load('C:/Users/harya/Documents/HSA/Mahadata/BigMart Sales.csv')
    
    df.printSchema()

    df.select(col("item_identifier"), upper(col("item_fat_content")).alias("Uppercase_Fat_Content")).show()

    df.withColumn("Current_Date", current_date()).show()

    spark.stop()
    