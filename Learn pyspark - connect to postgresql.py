from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Connect to PostgreSQL").getOrCreate()

url = "jdbc:postgresql://localhost:5432/mydatabase"

properties = {
    "user": "myusername",
    "password": "mypassword",
    "driver": "org.postgresql.Driver"
}               