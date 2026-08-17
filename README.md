# PySpark API Project

A Python data-processing project that uses **Apache PySpark** to process customer data and **FastAPI** to expose the processed data through REST API endpoints.

## 🚀 Technologies

* Python 3
* PySpark
* FastAPI
* Uvicorn
* Pandas
* REST API
* Git / GitHub
* Python Virtual Environment

## 📁 Project Structure

```text
pyspark_api_project/
│
├── .venv/
├── data/
│   └── customers.csv
│
├── app.py
├── spark_job.py
├── requirements.txt
├── .gitignore
└── README.md
```

> `.venv/` should not be committed to Git.

## 📊 Sample Data

The project uses a customer CSV file:

```csv
id,name,age,country
1,John,30,USA
2,Sara,25,Canada
3,David,40,USA
4,Mei,35,China
5,Mila,22,USA
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd pyspark_api_project
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## ▶️ Run the API

Start the FastAPI application:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## 🔗 API Endpoints

### Health Check

```http
GET /
```

Example response:

```json
{
  "message": "PySpark API is running!"
}
```

### Get Customers by Country

```http
GET /customers/{country}
```

Example:

```text
GET /customers/USA
```

Example response:

```json
{
  "country": "USA",
  "customers": [
    {
      "id": 1,
      "name": "John",
      "age": 30,
      "country": "USA"
    },
    {
      "id": 3,
      "name": "David",
      "age": 40,
      "country": "USA"
    }
  ]
}
```

### Calculate Average Age

```http
GET /average-age
```

Example response:

```json
{
  "average_age": 30.4
}
```

## 🔥 PySpark Processing

The `spark_job.py` module creates a Spark session and performs data processing.

Test customer filtering:

```bash
curl http://127.0.0.1:8000/customers/USA
```

Test average age:

```bash
curl http://127.0.0.1:8000/average-age
```

You can also use **Postman** or the FastAPI Swagger UI at `/docs`.

```

## 🧠 What This Project Demonstrates

* Building data pipelines with PySpark
* Spark DataFrame transformations
* Reading CSV data
* Filtering and aggregating large datasets
* Building REST APIs with FastAPI
* Connecting a data-processing layer to an API
* Python virtual environment management
* API testing with Swagger/Postman/cURL
* Git/GitHub project organization

## 📌 Future Improvements

* Add PostgreSQL or MySQL integration
* Add unit tests with `pytest`
* Add API authentication
* Add Docker support
* Add Docker Compose
* Add CI/CD with GitHub Actions
* Process JSON and Parquet files
* Add Spark SQL queries
* Add logging and exception handling
* Add AWS S3 or Azure Blob Storage
* Add Kafka streaming
* Add data validation with Pydantic

## 👨‍💻 Author

**Mohammad Rahman**

Python | PySpark | Java | SDET | Test Automation | REST API
