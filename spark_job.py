from pyspark.sql import SparkSession
from pyspark.sql.functions import col

class SparkProcessor:
    def __init__(self):
        self.spark = (
            SparkSession.builder
            .appName("PySparkAPIExample")
            .master("local[*]")
            .getOrCreate()
        )

    def load_data(self, path="data/customers.csv"):
        df = self.spark.read.csv(path, header=True, inferSchema=True)
        return df

    def filter_by_country(self, country):
        df = self.load_data()
        return df.filter(col("country") == country)

    def get_average_age(self):
        df = self.load_data()
        return df.groupBy().avg("age").first()[0]
