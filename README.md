## 🛒 Grocery Analysis Dashboard
A Python + SQL project that extracts, cleans, and stores Costco grocery order data, then visualizes trends, forecasts demand, and identifies anomalies using Tableau dashboards.

---

## Why?
While analyzing fraternity grocery orders, I noticed inefficiencies in planning and tracking weekly spending. Some items were over-ordered, others under-ordered, and canceled orders were frequent. To make the process more data-driven, I extracted historical order data, categorized items, and built Tableau dashboards to track spending, demand, and category performance. This allows for smarter ordering, better inventory management, and clear visibility into trends over time.

---

## 🚀 Features

- **PDF Parsing & Data Cleaning:** Extracts structured data from weekly invoices using Python (pdfplumber + pandas).   
 
- **SQL Database Integration:** Stores item orders, categories, quantities, and weekly spend in PostgreSQL.   

- **Demand Forecasting:** Estimates upcoming weekly demand per item.  

- **Spending & Category Analysis:** Tracks total weekly cost, top items, and category performance.   
  
- **Tableau Visualization:** Interactive dashboards with line charts, scatter plots, pie charts, and heatmaps for insights.   

- **Export for Analytics:** CSV export for Tableau or other analytics tools. 

---

## 🧰 Tech Stack

- **Languages:** Python, SQL   

- **Database:** PostgreSQL    

- **Libraries:** pandas, pdfplumber, psycopg2    
  
- **Visualization:** Tableau   

---

## 📈 Workflow

1. Extract weekly order data from PDFs.   

2. Clean, categorize, and store data in PostgreSQL (costco_orders).   

3. Aggregate and calculate metrics: weekly spend, top items, category totals, inventory fill rates.   

4. Export data to CSV for Tableau dashboards.      
 
5. Visualize insights with filters, forecasts, and trend lines.   

---

## 📊 Tableau Dashboard    
[View Here](https://public.tableau.com/views/GroceryData_17614263618620/Dashboard2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
Visualizes weekly spending, item demand forecasts, and category trends.   
Highlights top items, and spending patterns.     

---

## 💡 Future Improvements

Automate weekly PDF extraction and Tableau data refresh.   

Implement advanced machine learning models for demand forecasting.   

Add an interactive web front-end for easier exploration.   

---

## 👨‍💻 Author
Jacob Sandau   
University of Minnesota   
[https://www.linkedin.com/in/jacob-sandau-204743233/] | jsandau@sandau.com
