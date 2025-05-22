# 🛠️ ELT Data Pipeline + BigQuery API

This project demonstrates a complete ELT data pipeline using Python, Apache Spark, Google BigQuery, and Django REST Framework. It extracts data from a CSV file, transforms it using PySpark, loads the result into BigQuery, and exposes the processed data through a public API hosted on Render.

---

## 📊 Overview

**Goal**: Build an end-to-end ELT pipeline that processes Netflix title data and serves it via a REST API.

- 🔹 **Source data**: `netflix_titles_nov_2019.csv`
- 🔹 **Transformations**: filters and aggregations by release year
- 🔹 **Destination**: Google BigQuery
- 🔹 **API**: Django + DRF to serve transformed data

---

## 🚀 Technologies Used

| Layer           | Technology                      |
|------------------|----------------------------------|
| Processing       | Python + PySpark                |
| Storage          | Google BigQuery                 |
| Backend API      | Django + Django REST Framework  |
| Deployment       | Render (free plan)              |
| Security         | Environment variable (GCP JSON) |

---

## 📁 Project Structure

bq_api/ # Django project
├── api/ # Main app (API views)
├── bq_api/ # Django settings and URLs
├── manage.py # Django management script
├── Procfile # For Render deployment
├── requirements.txt # Python dependencies


---

## 🔗 Live API (Render)

> https://elt-project.onrender.com
Returns a JSON summary of movie counts by release year from BigQuery.

---

## 📌 How It Works

1. **Extract** data from a local CSV file using PySpark.
2. **Transform** it with filters and groupBy (e.g. movies by year).
3. **Load** the result into a Google BigQuery table.
4. **Expose** the table via a Django REST endpoint.

---

## 🧪 Local Setup (optional)

git clone https://github.com/mathorita/ELT-Project
cd your-repo
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py runserver
🛑 Don't forget to place your GCP service account .json locally and use:

python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hopeful-timing-460610-c6-394d9f1c4714.json"
📌 Environment Variables (used on Render)
GOOGLE_CREDENTIALS_JSON – contains your GCP service account key as a JSON string

🧠 What I Learned
How to structure a real data pipeline using Spark and BigQuery

How to securely deploy Django APIs with cloud credentials

How to expose analytical data through a REST API

How to combine tools for backend + data engineering workflows

