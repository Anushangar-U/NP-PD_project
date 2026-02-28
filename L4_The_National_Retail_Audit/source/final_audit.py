import numpy as np
import pandas as pd

sales_df = pd.read_csv(r"python\numpy_project\L4_The_National_Retail_Audit\data\sales_2025.csv")

#DATA CLEANING
#Filling the NA values with existing data using linear interpolate
sales_df["Timestamp"] = pd.to_datetime(sales_df["Timestamp"])
sales_df["Timestamp"] = sales_df["Timestamp"].interpolate(method="linear") 

#Filtering out the returns(negative quantity)
sales_df["Quantity"] = pd.to_numeric(sales_df["Quantity"])
sales_df = sales_df[sales_df["Quantity"] >= 0]


#MERGING
#connecting product master and sales 2025
product_df = pd.read_csv(r"python\numpy_project\L4_The_National_Retail_Audit\data\product_master.csv")
sales_product_merge = pd.merge(sales_df,product_df,on="Product_ID")

#connecting product sales merge df to the regional targets
targets_df = pd.read_csv(r"python\numpy_project\L4_The_National_Retail_Audit\data\regional_targets.csv")
Final_merge = pd.merge(sales_product_merge,targets_df,on="Category")

#checking shapes of the DF to ensure no data lose
if(sales_df.shape[0] == Final_merge.shape[0]):
    print("Shapes are same")
else:
    print("data lose")
    
    
#BUSINESS LOGIC
#revenue calculation
Final_merge["Transaction_Revenue"] = Final_merge["Price"]*Final_merge["Quantity"]

#Performance analysis
Final_merge["Revenue_Status"] = np.where(Final_merge["Transaction_Revenue"] >=  Final_merge["Target_Revenue"]*0.10,"High Performer","Under Performer" )

#STATISTICAL OUTLIER DETECTION
#calculating IQR
IQR = Final_merge["Transaction_Revenue"].quantile(0.75) - Final_merge["Transaction_Revenue"].quantile(0.25)

#identifying bulk orders
bulk_orders = np.where(Final_merge["Transaction_Revenue"] > (Final_merge))

print(Final_merge.sample(10))
