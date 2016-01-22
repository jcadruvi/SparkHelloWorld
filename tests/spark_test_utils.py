import unittest

from app.spark_utils import SparkUtils
from tests.spark_test_types import SparkTestTypes


class SparkTestUtils(object):

    @staticmethod
    def get_spark_context():
        return SparkUtils().get_spark_context(master=SparkTestTypes.Master,
                                              app_name=SparkTestTypes.AppName)

    @staticmethod
    def tear_down_spark_context(spark_context):
        if spark_context:
            spark_context.stop()