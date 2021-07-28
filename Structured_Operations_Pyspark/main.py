from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pandas

spark = SparkSession.builder.appName("Structured Data").config("spark.driver.memory","4g").config("spark.executor.memory","4g").getOrCreate()

dataFrame = spark.read.csv("C:\\Learning\\Python_Projects\\PySpark\\fire-incidents.csv", inferSchema=True, header=True)

def schemaDefinition():
    dataFrame.printSchema()

def basicSQLOperations():
    dataFrame.select("IncidentNumber","ID").sort("IncidentNumber").show(5,False)

if __name__ == '__main__':
    print("In main method")
    schemaDefinition()
    basicSQLOperations()
