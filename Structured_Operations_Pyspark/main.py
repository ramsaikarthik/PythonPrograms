from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pandas

spark = SparkSession.builder.appName("Structured Data").config("spark.driver.memory","4g").config("spark.executor.memory","4g").getOrCreate()

def schemaDefinition(path):
    dataFrame.printSchema()

def basicSQLOperations(path):
    dataFrame.select("IncidentNumber","ID").sort("IncidentNumber").show(5,False)

if __name__ == '__main__':
    path = str(input("Enter the path name: "))
    dataFrame = spark.read.csv(path, inferSchema=True, header=True)
    schemaDefinition(path)
    basicSQLOperations(path)
