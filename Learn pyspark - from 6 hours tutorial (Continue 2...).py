from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark SQL Example").getOrCreate()

    data1 = [('1','kad'),('2','sid')]
    schema1 = 'id STRING, name STRING' 

    df1 = spark.createDataFrame(data1,schema1)

    data2 = [('3','rahul'),('4','jas')]
    schema2 = 'id STRING, name STRING' 

    df2 = spark.createDataFrame(data2,schema2)

    df1.show()
    df2.show()
    
    df1.union(df2).show()
    df1.unionByName(df2).show()

    spark.stop()