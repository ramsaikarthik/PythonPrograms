from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


spark = SparkSession.builder.appName("Structured Data").config("spark.driver.memory","4g").config("spark.executor.memory","4g").getOrCreate()
spark.sparkContext.addPyFile("C:\\Softwares\\Spark\\pyspark\\jars\\org.apache.spark_spark-avro_2.12-3.1.2.jar")

dataFrame = spark.read.format("avro").load("C:\\Users\\Ram Sai Karthik\\Desktop\\userdata1.avro")

dataFrame.show()
