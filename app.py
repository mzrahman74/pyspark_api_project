from fastapi import FastAPI
from spark_job import SparkProcessor

app = FastAPI()
spark_processor = SparkProcessor()

@app.get("/")
def root():
    return {"message": "PySpark API is running!"}

@app.get("/customers/{country}")
def get_customers_by_country(country: str):
    df = spark_processor.filter_by_country(country)
    data = df.toPandas().to_dict(orient="records")
    return {"country": country, "customers": data}

@app.get("/average-age")
def get_average_age():
    avg_age = spark_processor.get_average_age()
    return {"average_age": avg_age}
