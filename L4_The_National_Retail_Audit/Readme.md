# 📊 National Retail Audit & Inventory Optimizer

### 📌 Project Overview
This project performs a comprehensive audit of Sri Lankan retail sales data for 2025. It integrates disparate data sources (Sales, Product Master, and Regional Targets) to identify high-performing transactions and detect statistical anomalies. This serves as the **Data Engineering** foundation for future Machine Learning models.

### 🏗️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** * `Pandas`: For relational data mapping and time-series interpolation.
    * `NumPy`: For vectorized business logic and statistical outlier detection.

---

### ⚙️ Data Pipeline Logic

#### 1. Data Cleaning (Sanitization)
* **Time-Series Recovery:** Addressed missing timestamps in raw sales data using **linear interpolation** to maintain chronological integrity.
* **Return Filtering:** Removed negative quantity values to ensure the analysis focuses purely on successful revenue-generating transactions.

#### 2. Relational Mapping (Data Architecture)
* Performed a **three-way join** to consolidate `Sales`, `Product Specs`, and `Regional Sales Targets` into a single "Source of Truth" DataFrame.

#### 3. Feature Engineering
* **Revenue Calculation:** Derived `Transaction_Revenue` through vectorized multiplication ($Price \times Quantity$).
* **Performance Classification:** Categorized transactions as **"High Performer"** if they achieved $\geq 10\%$ of the category's regional target.

#### 4. Statistical Outlier Detection
* Implemented the **Interquartile Range (IQR)** method to identify **Wholesale Orders**.
* **Formula:** $Revenue > Q3 + (1.5 \times IQR)$
* This step prevents extreme outliers from biasing future predictive AI models.

