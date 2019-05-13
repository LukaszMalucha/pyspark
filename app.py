## App Utilities
import os
import env

from flask import Flask, render_template, request
from flask_restful import Api
from flask_bootstrap import Bootstrap
from twitter import twitter_api

from tweepy import Stream
from tweepy.streaming import StreamListener

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



@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## APP INITIATION
if __name__ == '__main__':

    app.run(debug=True)

