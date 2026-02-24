import numpy as np
import pandas as pd

df_i = pd.read_csv(r"python\numpy_project\L3_Supply_Chain_Optimizer\data\inventory.csv")
df_t = pd.read_csv(r"python\numpy_project\L3_Supply_Chain_Optimizer\data\transactions.csv")

merged_df = pd.merge(df_i,df_t,on="Product_ID")
