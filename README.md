# End-to-End Vendor Insights

This project analyzes vendor performance for a wholesale/retail business. The goal is to find which vendors and brands are profitable, where pricing or inventory issues are hurting the business, and how to fix them using data.

---

## What This Project Does

- Identifies top-performing and underperforming vendors
- Highlights slow-moving or stuck inventory
- Detects pricing inconsistencies
- Analyzes how bulk purchases affect margins
- Answers core business questions with clear data

---

## Why It Matters

Businesses need to know:
- Which vendors increase profits and which don’t
- Where money is being lost—through poor pricing or slow sales
- How to optimize vendor relationships and buying behavior

This project walks through that analysis with a structured, reproducible approach.

---

## How It Works

- **Data Ingestion**: Loads raw CSVs into SQLite using Python. Handles large files, logs every step.
- **Data Cleaning + Analysis**: Uses SQL and Pandas to clean, join, and explore data.
- **Insights**: Runs calculations and aggregations to answer key questions.
- **Dashboard**: Power BI shows vendor-level insights visually.

---

## What’s in the Data

The dataset contains:
- Beginning and end inventory
- Vendor purchases and prices
- Sales data
- Vendor invoices

All CSVs are loaded into a single SQLite database for analysis.

---

## Key Files

- `Ingestion.ipynb` — Loads CSVs into SQLite with logging
- `Exploratory Data Analysis.ipynb` — Cleans data and performs analysis
- `inventory.db` — Final SQLite database
- `Workflow.png` — Visual overview of the project

---

## Skills Covered

- SQL for joins, filters, aggregations
- Python scripting with logging and chunking
- Pandas for EDA and data transformation
- Power BI for dashboarding
- Turning business problems into code-based solutions

---

## Summary

This project is built to show how to handle real business data, ask the right questions, and extract meaningful insights. It's a complete example of data analysis from raw files to final visualizations.
