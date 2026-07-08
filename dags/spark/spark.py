# from pyspark.sql import SparkSession

# spark = SparkSession.builder().appName("PruebaSpark").getOrCreate()

# df = spark.range(0,10)

# df.show()

# spark.stop()
from pyspark.sql import SparkSession
 
#Crear sesion Spark
spark = SparkSession.builder.appName("JobSparkEjemplo").getOrCreate()
 
#Dataframe
df=spark.range(0,10)
 
#mostrar datos
df.show()
 
spark.stop()