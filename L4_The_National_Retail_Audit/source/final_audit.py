import numpy as np
import pandas as pd

# Load Paths
path = r"python\numpy_project\L4_The_National_Retail_Audit\data\\"

sales_df = pd.read_csv(path + "sales_2025.csv")
product_df = pd.read_csv(path + "product_master.csv")
targets_df = pd.read_csv(path + "regional_targets.csv")

# 1. DATA CLEANING
sales_df["Timestamp"] = pd.to_datetime(sales_df["Timestamp"]).interpolate(method="linear") 
sales_df = sales_df[sales_df["Quantity"] >= 0].copy()

# 2. MERGING
sales_product_merge = pd.merge(sales_df, product_df, on="Product_ID")
final_merge = pd.merge(sales_product_merge, targets_df, on="Category")

# 3. BUSINESS LOGIC
final_merge["Transaction_Revenue"] = final_merge["Price"] * final_merge["Quantity"]
final_merge["Revenue_Status"] = np.where(
    final_merge["Transaction_Revenue"] >= final_merge["Target_Revenue"] * 0.10,
    "High Performer", "Under Performer"
)

# 4. STATISTICAL OUTLIER DETECTION
Q1 = final_merge["Transaction_Revenue"].quantile(0.25)
Q3 = final_merge["Transaction_Revenue"].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + (1.5 * IQR)

# Flagging Wholesale Orders
final_merge["Is_Wholesale"] = np.where(final_merge["Transaction_Revenue"] > upper_bound, True, False)
wholesale_count = final_merge["Is_Wholesale"].sum()

# 5. SAVE THE "SILVER" DATASET
final_merge.to_csv(r"python\numpy_project\L4_The_National_Retail_Audit\data\final_audit.csv", index=False)

# --- FINAL REPORT ---
print("--- AUDIT SUMMARY ---")
print(f"✅ Cleaned Sales Records: {len(final_merge)}")
print(f"🚨 Wholesale Outliers Detected: {wholesale_count}")
print(f"💰 Total Revenue: LKR {final_merge['Transaction_Revenue'].sum():,.2f}")