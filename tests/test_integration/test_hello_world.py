import unittest

from tests.spark_test_utils import SparkTestUtils


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.spark_context = SparkTestUtils.get_spark_context()

    def tearDown(self):
        SparkTestUtils.tear_down_spark_context(self.spark_context)

    def test_hello_world(self):
        print "here"
        rdd = self.spark_context.textFile("tests/test_integration/test_file")
        words = rdd.flatMap(lambda line: line.split("|"))
        pairs = words.map(lambda word: (word, 1))
        wordCounts = pairs.reduceByKey(lambda x, y: x + y)
        print wordCounts.collect()