# 📦 E-Commerce Supply Chain & Inventory Optimizer
**Level 3: Advanced Data Engineering & Forecasting Project**

## 📝 Project Summary
This project simulates a real-world retail environment (e.g., a Sri Lankan supermarket chain) where sales data and warehouse inventory are stored in separate silos. The system integrates these relational datasets to perform **Demand Forecasting** and **Automated Stock-Out Risk Detection**.

## 🚀 Technical Core
* **Relational Data Integration:** Performed an inner join using `pd.merge()` to link daily transactions with product metadata (Price, Category, Stock Level) using a common `Product_ID` key.
* **Inventory Valuation:** Implemented vectorized NumPy operations to calculate real-time revenue per transaction and total capital tied up in warehouse stock.
* **Predictive Stock-Out Modeling:** * Calculated **Daily Sales Velocity** by aggregating quantities over a 7-day temporal window.
    * Developed a "Days of Cover" algorithm: $\text{Current Stock} \div \text{Average Daily Sales}$.
* **Automated Alerting:** Used `np.where()` logic to flag "CRITICAL REORDER" status for products with less than a 7-day supply remaining.

## 🛠️ Tech Stack & Methods
* **Language:** Python 3.14
* **Libraries:** Pandas, NumPy
* **Key Pandas Methods:** `merge()`, `groupby()`, `pd.to_datetime()`, `nunique()`, `reset_index()`.
* **Key NumPy Methods:** `np.where()`, Vectorized multiplication.

## 📊 Business Insights Generated
1.  **Category Profitability:** Identified which product categories (Grains, Beverages, etc.) contribute the highest revenue.
2.  **Operational Risk:** Isolated products that are selling faster than the supply chain can replenish, preventing lost sales.
