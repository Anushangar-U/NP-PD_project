import numpy as np
import pandas as pd

#importing csv into dataframe
df_i = pd.read_csv(r"python\numpy_project\L3_Supply_Chain_Optimizer\data\inventory.csv")
df_t = pd.read_csv(r"python\numpy_project\L3_Supply_Chain_Optimizer\data\transactions.csv")

#merging 2 df into 1
merged_df = pd.merge(df_i,df_t,on="Product_ID").copy()

#adding total revenue column
merged_df["Total_revenue"] = merged_df["Unit_Price"]*merged_df["Quantity"]
print(merged_df)

