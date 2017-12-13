from __future__ import print_function

from pyspark.sql import SparkSession

if __name__ == "__main__":
   spark = SparkSession.builder.appName("Spark Version").getOrCreate()

   print("The current version of spark is: " + spark.version);

   spark.stop()
