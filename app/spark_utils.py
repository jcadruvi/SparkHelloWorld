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


class SparkUtils(object):
    def get_spark_context(self, master=None, app_name=None):
        spark_conf = SparkConf()
        if master:
            spark_conf.setMaster(master)
        if app_name:
            spark_conf.setAppName(app_name)
        return SparkContext(conf=spark_conf)