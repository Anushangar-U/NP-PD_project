import numpy as np
import pandas as pd

# 1. Import CSVs into DataFrames
df_i = pd.read_csv(r"python\numpy_project\L3_Supply_Chain_Optimizer\data\inventory.csv")
df_t = pd.read_csv(r"python\numpy_project\L3_Supply_Chain_Optimizer\data\transactions.csv")

# 2. Ensure Date is recognized by Pandas
df_t["Date"] = pd.to_datetime(df_t["Date"])

# 3. Merging 2 DFs into 1 
merged_df = pd.merge(df_i, df_t, on="Product_ID").copy()

# 4. Adding Total Revenue Column 
merged_df["Total_revenue"] = merged_df["Unit_Price"] * merged_df["Quantity"]

# 5. Grouping by Category for the "Big Picture" report
category_df = merged_df.groupby("Category")[["Total_revenue", "Quantity"]].sum().reset_index()

# 6. Predicting "Stock-Out" Risk 
total_days = df_t['Date'].nunique()

# Sum quantity sold per product name
product_sales = merged_df.groupby("Product_Name")["Quantity"].sum().reset_index()

# Re-attach Current_Stock to the sales summary
product_stats = pd.merge(product_sales, df_i[['Product_Name', 'Current_Stock']], on="Product_Name")

# Calculate Days left until stock hits zero
product_stats["Avg_Daily_Sales"] = product_stats["Quantity"] / total_days
product_stats["Days_to_Run_Out"] = product_stats["Current_Stock"] / product_stats["Avg_Daily_Sales"]

# Using np.where to flag items needing immediate attention
product_stats["Risk_Status"] = np.where(product_stats["Days_to_Run_Out"] < 7, "CRITICAL", "OK")

# 7. Saving the analyzed data to CSV
category_df.to_csv(r"python\numpy_project\L3_Supply_Chain_Optimizer\data\category.csv", index=False)
product_stats.to_csv(r"python\numpy_project\L3_Supply_Chain_Optimizer\data\Product_stats.csv", index=False)

# Final Print for verification
print("--- ANALYSIS COMPLETE ---")
print(product_stats[['Product_Name', 'Days_to_Run_Out', 'Risk_Status']])