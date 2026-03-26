import re
from pyspark import SparkContext, SparkConf

def splitComma(line: str):
    splits = COMMA_DELIMITER.split(line)
    return f"{splits[1]}, {splits[6]}"

if __name__ == "__main__":

    COMMA_DELIMITER = re.compile(''',(?=(?:[^"]*"[^"]*")*[^"]*$)''')

    sparkconf = SparkConf().setAppName("airports").setMaster("local[3]")
    sc = SparkContext(conf = sparkconf)

    airports = sc.textFile("C:/Users/harya/Documents/HSA/GitHub/python-spark-tutorial/in/airports.text")
    airportsByLatitude = airports.filter(lambda line : float(COMMA_DELIMITER.split(line)[6]) > 40)

    airportsNameAndCityNames = airportsByLatitude.map(splitComma)
    print(airportsNameAndCityNames.take(20))
    # airportsNameAndCityNames.saveAsTextFile("out/airports_in_usa.text")
