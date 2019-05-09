import findspark
import os.path
import time

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc

from collections import namedtuple

# Path to spark & Init
my_path = os.path.abspath(os.path.dirname(__file__))
spark_path = os.path.join(my_path, "./spark")
findspark.init(spark_path)



if __name__ == "__main__":
    sc = SparkContext()
    ssc = StreamingContext(sc, 1)

    rddQueue = []
    for i in range(5):
        rddQueue += [ ssc.sparkContext.parallelize([j for j in range(1, 1001)], 10)]

    inputStream = ssc.queueStream(rddQueue)
    mappedStream = inputStream.map(lambda x: (x % 10, 1))
    reducedStream = mappedStream.reduceByKey(lambda a, b: a+b)
    reducedStream.pprint()

    ssc.start()
    time.sleep(6)
    ssc.stop(stopSparkContext=True, stopGraceFully=True)

