from pyspark import SparkConf, SparkContext

if __name__ == "__main__":
    confspark = SparkConf().setAppName("Collect Example").setMaster("local[*]")
    sc = SparkContext(conf=confspark)
    sc.setLogLevel("ERROR")

    wordlist = ["spark", "hadoop", "spark", "hive", "pig", "cassandra", "hadoop"]
    wordlistRDD = sc.parallelize(wordlist)

    result = wordlistRDD.collect()
    print(f"Original element = {result}")    
    print(f"Total elements = {wordlistRDD.count()}")
    
    for x in result:
        print(x)

    resultperelement = wordlistRDD.countByValue()
    for x, y in resultperelement.items():
        print(f"Total words per element = {y} for {x}")

    wordlistRDDTake3 = wordlistRDD.take(3)
    print(f"Take 3 elements = {wordlistRDDTake3}")

    for z in wordlistRDDTake3:
        print(z)


    integerlist = [1, 2, 3, 4, 5]
    integerlistRDD = sc.parallelize(integerlist)

    z = integerlistRDD.reduce(lambda a, b: a * b)
    print(f"Sum of all elements in integerlistRDD = {z}")

sc.stop()