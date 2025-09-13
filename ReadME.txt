# US Housing Market Analysis – Income, Mortgage & Affordability

## 📌 Overview
This project analyzes housing prices, household income, and mortgage rates across US states and cities.  
The focus is on **housing affordability**, **state-wise trends**, and **income vs house price correlation**.  

The workflow combines **Python (synthetic dataset generation)**, **Google BigQuery (SQL-based aggregation & analysis)**,  
and **Power BI (interactive dashboard visualization)**.

---

## ⚙️ Workflow

1. **Data Generation (Python)**  
   - Created synthetic datasets for housing prices, demographics, and mortgage rates.  
   - Saved them as CSV files for import into BigQuery.  

2. **Data Aggregation (BigQuery)**  
   - Imported CSVs into Google BigQuery.  
   - Wrote SQL queries to compute:  
     - State-wise average house price trends  
     - Top 10 most expensive cities  
     - Correlation between income & house prices  
     - Mortgage rate impact  
     - Housing affordability index  

3. **Visualization (Power BI)**  
   - Connected BigQuery tables directly to Power BI.  
   - Built an **interactive dashboard** with KPIs, scatter plots, line charts, and drillthrough analysis.  

---

## 📊 Key Insights
- States like **California** and **New York** have the highest housing prices with low affordability.  
- Affordable states include **Texas** and **Florida**, where income-to-price ratio is better.  
- Higher mortgage rates reduce affordability significantly.  

---

## 🛠️ Tools & Technologies
- **Python** → Synthetic data generation  
- **Google BigQuery** → Data aggregation & SQL analysis  
- **Power BI** → Interactive dashboard visualization  

---

## 🚀 How to Run

### 1. Generate Synthetic Data
```bash
python generate_data.py
2. Upload to BigQuery

Import CSVs into us_housing dataset.

Run SQL queries from /queries folder in BigQuery Sandbox.

3. Power BI

Connect Power BI to BigQuery.

Use the dashboard file /dashboard/housing_dashboard.pbix.

📂 Project Structure
├── data/                  # Synthetic CSV datasets
├── queries/               # BigQuery SQL queries
├── dashboard/             # Power BI files & screenshots
├── generate_data.py       # Python script to create synthetic data
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

👤 [Tanmay Sharma]
Data Analyst | SQL | Power BI | Python
LinkedIn: https://www.linkedin.com/in/tanmay-sharma-800599373/
Git hub: https://github.com/Tanu272004
Project Link: US Mortgage Housing Analytics With Affordability Index 


