from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

if __name__ == "__main__":

    spark = SparkSession.builder.appName("Learning Spark").getOrCreate()

    df = spark.read.format('csv')\
        .option('inferSchema',True)\
        .option('header',True)\
        .load('C:/Users/harya/Documents/HSA/superstore.csv')
    
    df_json = spark.read.format('json')\
        .option('inferSchema',True)\
        .option('header',True)\
        .option('multiLine',False)\
        .load('C:/Users/harya/Documents/HSA/Mahadata/drivers.json')
    
    # df.show(5)
    # df_json.show(5)

    my_ddl_schema = '''
                        row_id integer,
                        order_id string,
                        order_date date,
                        ship_date date,
                        ship_mode string,
                        customer_id string,
                        customer_name string,
                        segment string,
                        country string,
                        city string,
                        state string,
                        postal_code STRING,
                        region string,
                        product_id string,
                        category string,
                        subcategory string,
                        product_name string,
                        sales string,
                        quantity string,
                        discount double,
                        profit double
                    '''
    
    df_ddl = spark.read.format('csv')\
        .option('header',True)\
        .schema(my_ddl_schema)\
        .load('C:/Users/harya/Documents/HSA/superstore.csv')

#     df.printSchema()
    df_ddl.printSchema()

    # df_ddl.select("order_id", "order_date", "ship_date", "customer_name").show(5)
    
    df_ddl_select = df_ddl.select(col("order_id").alias("OrderID")\
                , col("order_date").alias("OrderDate")\
                , col("ship_date").alias("ShipDate")\
                , col("customer_name").alias("CustomerName")\
                , col("ship_mode").alias("ShipMode")\
                , col("country").alias("Country")\
                , col("city").alias("City")\
                , col("category").alias("Category"))
    
    # df_ddl_select.select(col("ShipMode")).distinct().show()

    df_ddl_select_filtered = df_ddl_select.filter((lower(col("ShipMode")) == "second class") & (lower(col("City")) == "auburn"))
    df_ddl_select_filtered.show(45)

    # df_ddl_select_filtered.select(col("City")).groupBy(col("City")).count().show()

    # Stop the SparkSession
    spark.stop()