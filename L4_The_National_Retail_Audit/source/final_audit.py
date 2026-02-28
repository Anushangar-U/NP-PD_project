import numpy as np
import pandas as pd

sales_df = pd.read_csv(r"python\numpy_project\L4_The_National_Retail_Audit\data\sales_2025.csv")

#Filling the NA values with existing data using linear interpolate
sales_df["Timestamp"] = pd.to_datetime(sales_df["Timestamp"])
sales_df["Timestamp"] = sales_df["Timestamp"].interpolate(method="linear") 

#Filtering out the returns(negative quantity)
sales_df["Quantity"] = pd.to_numeric(sales_df["Quantity"])
sales_df = sales_df[sales_df["Quantity"] >= 0]

print(sales_df.sample(10))