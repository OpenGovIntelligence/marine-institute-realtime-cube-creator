import findspark
#findspark.init()

# Or the following command
#findspark.init("/path/to/spark_home")
findspark.init("/usr/local/spark")


from pyspark import SparkContext, SparkConf

