from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from spark_job import SparkProcessor
import  xml.etree.ElementTree as ET


app = FastAPI()
spark_processor = SparkProcessor()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    # This renders your HTML UI instead of returning JSON
    return templates.TemplateResponse(request, "country.html")

@app.get("/customers/{country}")
def get_cvs_customers_by_country(request: Request, country: str):
    df = spark_processor.filter_csv_by_country(country)
    data = df.toPandas().to_dict(orient="records")
    return templates.TemplateResponse(request, "country.html")

@app.get("/json/customers/{country}")
def get_json_customers_by(country: str):
    df = spark_processor.filter_json_by_country(country)
    data = df.toPandas().to_dict(orient="records")
    return {"data_type": "JSON", "country": country, "customers": data}

@app.get("/xml/customers/{country}")
def get_xml_customers_by(country: str):
    df = spark_processor.filter_xml_by_country(country)
    data = df.toPandas().to_dict(orient="records")

    root_el = ET.Element("customers")
    for row in data:
        customer_el = ET.SubElement(root_el, "customer")
        for key, value in row.items():
            child = ET.SubElement(customer_el, str(key))
            child.text = "" if value is None else str(value)
    xml_bytes = ET.tostring(root_el, encoding="utf-8", xml_declaration=True)
    return Response(content=xml_bytes, media_type="application/xml")