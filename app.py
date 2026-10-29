from fastapi import FastAPI
from spark_job import SparkProcessor

app = FastAPI()
spark_processor = SparkProcessor()

@app.get("/")
def root():
    return {"message": "PySpark API is running!"}

@app.get("/customers/{country}")
def get_cvs_customers_by_country(country: str):
    df  = spark_processor.filter_csv_by_country(country)
    data = df.toPandas().to_dict(orient="records")
    return {
        "data_type": "CSV",
        "country": country,
        "customers": data
    }

@app.get("/average-age")
def get_average_age():
    avg_age = spark_processor.get_average_age()
    return {"average_age": avg_age}

@app.get("/json/customers/{country}")
def get_json_customers_by(country: str):
    df = spark_processor.filter_json_by_country(country)
    data = df.toPandas().to_dict(orient="records")
    return {"data_type": "JSON",
            "country": country,
            "customers": data}

@app.get("/xml/customers/{country}")
def get_xml_customers_by(country: str):
    df = spark_processor.filter_xml_by_country(country)
    data = df.toPandas().to_dict(orient="records")
    return {"data_type": "XML",
             "country": country,
             "customers": data}

