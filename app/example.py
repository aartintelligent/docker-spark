from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('Save DataFrame to database') \
    .config('spark.jars', '/opt/spark/jars/postgresql-42.7.4.jar') \
    .getOrCreate()

data = [
    (1, 'Alice'     , 28),
    (2, 'Bob'       , 35),
    (3, 'Charlie'   , 61)
]

columns = ['id', 'name', 'age']

df = spark.createDataFrame(data, columns)

db_url = 'jdbc:postgresql://database:5432/postgres'

db_properties = {
    'user'      : 'spark',
    'password'  : 'password',
    'driver'    : 'org.postgresql.Driver'
}

table_name = 'example_table'

df.write.jdbc(url=db_url, table=table_name, mode='overwrite', properties=db_properties)

spark.stop()
