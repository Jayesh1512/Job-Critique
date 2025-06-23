# 💼 Job Critique

**Job Critique** is a full-stack Data Engineering + Visualization project that automates the ETL of job listing data into Snowflake and delivers beautiful dashboards for insight discovery using Streamlit and Plotly.

It leverages **real-world job data (65,000+ rows)** scraped from **Google Jobs** and other job posting APIs/websites.

---

## 🚀 Features

✅ Extracts and loads job data from a CSV file (~65K rows)  
✅ Automatically sets up Snowflake warehouse, database, schema, and tables  
✅ Creates raw and analytical tables in Snowflake  
✅ Interactive dashboards with Plotly & Streamlit  
✅ Modular Python codebase and clean architecture

---

## 🏗️ Architecture

```plaintext
         [65K+ Row CSV File from Google Jobs & APIs]
                       |
                    Extract
                       |
             Load into Snowflake Tables
                       |
     ┌─────────────────┬──────────────────┬──────────────────┐
     │ raw_jobs        │ industry_analysis│ job_posting_trends
     └─────────────────┴──────────────────┴──────────────────┘
                       ↓
            Visualize with Streamlit Dashboard
