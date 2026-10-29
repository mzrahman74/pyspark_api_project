from pyspark.sql import SparkSession
from pyspark.sql.functions import col

class SparkProcessor:
    def __init__(self):
        self.spark = (
            SparkSession.builder
            .appName("PySparkAPIExample")
            .master("local[*]")
            .config("spark.jars.packages",
                    "com.databricks:spark-xml_2.13:0.18.0")
            .getOrCreate()
        )
    #csv
    def load_csv(self):
        return self.spark.read.csv(
            "data/customers.csv",
            header=True,
            inferSchema=True,
       )
    # JSON
    def load_json(self):
        return self.spark.read.option("multiline", "true").json("data/customers.json")

    #XML
    def load_xml(self, row_tag="customer"):
        return (
            self.spark.read
             .format("com.databricks.spark.xml")
             .option("rowTag", row_tag)
             .load("data/customers.xml")
        )

    def filter_json_by_country(self, country):
        df = self.load_json()
        return df.filter(col("country") == country)

    def filter_xml_by_country(self, country):
        df = self.load_xml()
        return df.filter(col("country") == country)

    def filter_csv_by_country(self, country):
        df = self.load_csv()
        return df.filter(col("country") == country)

    def get_average_age(self):
        df = self.load_csv()
        return df.groupBy().avg("age").first()[0]
