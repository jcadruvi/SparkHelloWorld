import os
import sys

from app.settings import SPARK_HOME

spark_home =  SPARK_HOME
# Path for spark source folder
os.environ['SPARK_HOME']= spark_home

# Append pyspark  to Python Path
sys.path.append(spark_home + "/python/")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    print ("Successfully imported Spark Modules")

except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)

sc = SparkContext('local')
words = sc.parallelize(["scala","java","hadoop","spark","akka"])
print "word count = {}".format(words.count())