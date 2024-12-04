import json

from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark_session = SparkSession.builder \
    .appName('Save DataFrame to database') \
    .getOrCreate()

schemas = {
    'example': StructType([
        StructField('id', IntegerType()),
        StructField('name', StringType()),
        StructField('age', IntegerType())
    ])
}

schemas_data = [(name, schema.json()) for name, schema in schemas.items()]

schemas_df = (
    spark_session.
    createDataFrame(schemas_data, [
        'resource',
        'json'
    ])
)

schemas_df.write.jdbc(
    url='jdbc:postgresql://database:5432/postgres',
    table='_schemas',
    mode='overwrite',
    properties={
        'user': 'spark',
        'password': 'password',
        'driver': 'org.postgresql.Driver'
    }
)

schemas = {row['resource']: StructType.fromJson(json.loads(row['json'])) for row in schemas_df.collect()}

exemple_data = [
    (1, 'Alice', 28),
    (2, 'Bob', 35),
    (3, 'Charlie', 61)
]

df = spark_session.createDataFrame(exemple_data, schemas['example'])

df.write.jdbc(
    url='jdbc:postgresql://database:5432/postgres',
    table='table_example',
    mode='overwrite',
    properties={
        'user': 'spark',
        'password': 'password',
        'driver': 'org.postgresql.Driver'
    }
)

spark_session.stop()
