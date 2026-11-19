from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat_ws


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

    def load_csv(self):
        return self.spark.read.csv(
            "data/customers.csv",
            header=True,
            inferSchema=True,
        )

    def load_json(self):
        return self.spark.read.option("multiline", "true").json("data/customers.json")

    def load_xml(self, row_tag="customer"):
        return (
            self.spark.read
            .format("com.databricks.spark.xml")
            .option("rowTag", row_tag)
            .load("data/customers.xml")
        )

    def filter_json_by_country(self, country):
        df = self.load_json()
        return (
            df.filter(col("country") == country)
            # Combine first_name and last_name into a single 'name' column
            .withColumn("name", concat_ws(" ", col("first_name"), col("last_name")))
            .select("id", "name", "age", "country")
        )

    def filter_xml_by_country(self, country):
        df = self.load_xml()
        return (
            df.filter(col("country") == country)
            .withColumn("name", concat_ws(" ", col("first_name"), col("last_name")))
            .select("id", "name", "age", "country")
        )

    def filter_csv_by_country(self, country):
        df = self.load_csv()
        # If your CSV also has first_name/last_name, apply it here too.
        # If your CSV already has a 'name' column, you can leave it as is or add .withColumn() if needed.
        return df.filter(col("country") == country).select("id", "name", "age", "country")

    def get_average_age(self):
        df = self.load_csv()
        return df.groupBy().avg("age").first()[0]