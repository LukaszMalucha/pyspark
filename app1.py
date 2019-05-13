## App Utilities
import os
import env

from flask import Flask, render_template, request
from flask_restful import Api
from flask_bootstrap import Bootstrap

import findspark
import os.path
import time

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

from collections import namedtuple

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['DEBUG'] = True
api = Api(app)

Bootstrap(app)

# Path to spark & Init
my_path = os.path.abspath(os.path.dirname(__file__))
spark_path = os.path.join(my_path, "./spark")
findspark.init(spark_path)



# sc = SparkContext('local')
#
spark = SparkSession.builder.appName("Flask PySpark").getOrCreate()


#
# # Main View
# @app.route('/', methods=['GET', 'POST'])
# def dashboard():
#
#
#     stream = spark.sparkContext.parallelize([(1, "a"), (2, "b"), (1, "c"), (2, "d"), (1, "e"), (3, "f")], 3)
#
#     maxstream = stream.reduce(max)
#
#
#
#     return render_template("dashboard.html", maxstream = maxstream)


# Main View
@app.route('/', methods=['GET', 'POST'])
def dashboard():


    rddQueue = []
    for i in range(5):
        stream = spark.sparkContext.parallelize([j for j in range(1, 1001)], 10)
        stream2 = stream.map(lambda x: (x % 10, 1))
        maxstream =  stream2.reduceByKey(lambda a, b: a + b)
        maxstream = maxstream.collect()
        rddQueue.append(maxstream)

    return render_template("dashboard.html", maxstream=rddQueue)


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## APP INITIATION
if __name__ == '__main__':

    app.run(debug=True)

