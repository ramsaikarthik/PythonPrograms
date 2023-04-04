from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


spark = SparkSession.builder.appName("Structured Data").config("spark.driver.memory","4g").config("spark.executor.memory","4g").getOrCreate()
spark.sparkContext.addPyFile("C:\\Softwares\\Spark\\pyspark\\jars\\org.apache.spark_spark-avro_2.12-3.1.2.jar")

dataFrame = spark.read.format("avro").load("C:\\Users\\Ram Sai Karthik\\Desktop\\userdata1.avro")
print("Total number of rows in dataFrame are: ",dataFrame.count())
dataFrame.printSchema()
print("AVRO dataframe is: ")
dataFrame.show(5,False)

#Coalesce is to have the number of output files
dataFrame.limit(50).coalesce(1).write.mode("overwrite").csv("D:\\PythonPrograms\\Structured_Operations_Pyspark\\OutputFiles\\AvroFile1", header=True)
csvDataFrame = spark.read.csv("D:\\PythonPrograms\\Structured_Operations_Pyspark\\OutputFiles\\AvroFile1\\*.csv", inferSchema=True, header=True)
print("Total record count in csv file is: ",csvDataFrame.count())

#Added a column for timeStamp

csvDataFrameTimeStamp = csvDataFrame.withColumn("processed_date_time", to_utc_timestamp(current_timestamp(),"IST"))
csvDataFrameTimeStamp.printSchema()
print("CSV dataframe is: ")
csvDataFrameTimeStamp.show(5,False)