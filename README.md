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

