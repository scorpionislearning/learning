from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    sparkconf = SparkConf().setAppName("word count").setMaster("local[3]")
    sc = SparkContext(conf = sparkconf)
    sc.setLogLevel("ERROR")
    
    lines = sc.textFile("C:/Users/harya/Documents/HSA/GitHub/python-spark-tutorial/in/word_count.text")
    
    words = lines.flatMap(lambda line: line.split(" "))
    
    wordCounts = words.countByValue()
    
    for word, count in wordCounts.items():
        print(f"{word} : {count}")