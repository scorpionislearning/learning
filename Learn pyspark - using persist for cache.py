from pyspark import SparkConf, SparkContext, StorageLevel

if __name__ == "__main__":
    spark_conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=spark_conf)
    sc.setLogLevel("ERROR")

    num = [1, 2, 3, 4, 5]
    rdd = sc.parallelize(num)
    rdd.persist(StorageLevel.MEMORY_ONLY)

    rdd_sum = rdd.reduce(lambda x, y: x + y)
    print(f"Sum: {rdd_sum}")

    sc.stop()