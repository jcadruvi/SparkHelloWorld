# SparkHelloWorld

This application gets the word count of each word in the tests/test_integration/test_file file. The file is a csv file that is split on |.

In order to get this application working you must first download spark here:

https://spark.apache.org/downloads.html

After you have downloaded and install spark you need to go into the settings.py file and set the SPARK_HOME variable which should
be the location of where installed spark.

After the SPARK_HOME variable you can run the application by opening a terminal and going to the SparkHelloWorld directory and doing the following:

$ pip install -r requirements.txt
$ pip install -r requirements_test.txt
$ ./run_tests_integration


Follow these instructions to get this project working on Windows:

Go to the following link:

http://spark.apache.org/downloads.html
In choose a package type select: Pre-built for Hadoop 2.6 and later
The click on the Download Spark link.
Then click on an HTTP server. 

Unzip the file and then follow the instructions on how to get this application working.

For windows do not run the following:

./run_tests_integration

Instead open up a command prompt browse to the SparkHelloWorld folder and typ in the following:

python spark_setup.py

After you run this you will have to look for the following output:

[(u'Profitability', 2), (u'438.72M', 1), (u'31-Dec', 2), (u'20070203', 3), (u'11.86%', 2), (u'Cash Flow Statement', 1),
(u'18.11%', 2), (u'Management Effectiveness', 2), (u'Fiscal Year Ends:', 2), (u'Operating Cash Flow (ttm):', 1),
(u'Profit Margin (ttm):', 2), (u'Most Recent Quarter (mrq):', 2), (u'185.26M', 1), (u'Fiscal Year', 2),
(u'20070106', 4), (u'Levered Free Cash Flow (ttm):', 1), (u'Return on Equity (ttm):', 2), (u'6.67%', 2),
(u'8.29%', 2), (u'Operating Margin (ttm):', 2), (u'Return on Assets (ttm):', 2), (u'30-Sep-06', 2)]


To verify that it worked. 
