from pyspark import SparkConf, SparkContext

if __name__ == "__main__":
    sparkconf = SparkConf().setAppName("Test pyspark").setMaster("local[*]")
    sc = SparkContext(conf=sparkconf)
    sc.setLogLevel("ERROR")

    primenum = sc.textFile("C:/Users/harya/Documents/HSA/GitHub/python-spark-tutorial/in/prime_nums.text")
    print(f"Total prime numbers = {primenum.count()}")
    # print(primenum.collect())
    
    primenum2 = primenum.flatMap(lambda x : x.split("\t"))
    # print(primenum2.collect())
    
    primenum3 = primenum2.filter(lambda x : x)

    primenum4 = primenum3.map(lambda x : int(x))

    primenum5 = primenum4.reduce(lambda x,y : x+y)
    print(f"Sum of prime numbers = {primenum5}")

sc.stop()