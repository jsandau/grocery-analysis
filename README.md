## 🛒 Grocery Analysis Dashboard
A Python + SQL project that extracts, cleans, and stores Costco grocery order data, then visualizes trends, forecasts demand, and identifies anomalies using Tableau dashboards.

---

## Why?
While analyzing fraternity grocery orders, I noticed inefficiencies in planning and tracking weekly spending. Some items were over-ordered, others under-ordered, and canceled orders were frequent. To make the process more data-driven, I extracted historical order data, categorized items, and built Tableau dashboards to track spending, demand, and category performance. This allows for smarter ordering, better inventory management, and clear visibility into trends over time.

---

## 🚀 Features

PDF Parsing & Data Cleaning: Extracts structured data from weekly invoices using Python (pdfplumber + pandas).   
 
SQL Database Integration: Stores item orders, categories, quantities, and weekly spend in PostgreSQL.   

Demand Forecasting: Estimates upcoming weekly demand per item and flags potential anomalies.   

Spending & Category Analysis: Tracks total and per-member weekly costs, top items, and category performance.   
  
Tableau Visualization: Interactive dashboards with line charts, scatter plots, pie charts, and heatmaps for insights.   

Export for Analytics: CSV export for Tableau or other analytics tools. 

---

## 🧰 Tech Stack

Languages: Python, SQL   

Database: PostgreSQL    

Libraries: pandas, pdfplumber, psycopg2    
  
Visualization: Tableau   

---

## 📈 Workflow

Extract weekly order data from PDFs.   

Clean, categorize, and store data in PostgreSQL (costco_orders).   

Aggregate and calculate metrics: weekly spend, top items, category totals, inventory fill rates.   

Export data to CSV for Tableau dashboards.    

Visualize insights with filters, forecasts, and trend lines.

---

## 📊 Tableau Dashboard   

Weekly Spending: Line chart showing total and per-member spend.

Item Demand: Forecast weekly quantities per item.

Category Trends: Compare spending across categories over time.

Top Items Analysis: Highlight top 10 items by total spend.

Price vs Spending Scatter Plot: Shows correlation between unit price and total spend per item.

Cancelled Orders & Fill Rate: Identify inefficiencies and anomalies.

---

## 💡 Future Improvements

Automate weekly PDF extraction and Tableau data refresh.

Implement advanced machine learning models for demand forecasting.

Add an interactive web front-end for easier exploration.

---

## 👨‍💻 Author
Jacob Sandau
University of Minnesota
📬 LinkedIn: [https://www.linkedin.com/in/jacob-sandau-204743233/]

📧 Email: jsandau@sandau.com
