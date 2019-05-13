import findspark
import os.path
import time

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc

from collections import namedtuple

# Path to spark & Init
my_path = os.path.abspath(os.path.dirname(__file__))
spark_path = os.path.join(my_path, "./spark")
findspark.init(spark_path)



if __name__ == "__main__":
    ## Start spark context
    conf = SparkConf().setMaster("local[*]").setAppName("PythonStreamingQueueStream")
    sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc, 1) ## spark context, seconds

    stream = ssc.queueStream([sc.parallelize([(1,"a"), (2,"b"),(1, "c"),(2,"d"),(1,"e"),(3, "f")],3)])

    maxstream = stream.reduce(max)
    maxstream.pprint()

    ssc.start()

    ssc.stop(stopSparkContext=True, stopGraceFully=True)



