import pandas as pd
import numpy as np

df = pd.read_csv(r"python\numpy_project\L2_Srilanka_Temperature\data\climate_data.csv")

#working with colombo city
colombo_df = df[df["city"] == "Colombo"].copy()

#data cleaning 
colombo_df["time"] = pd.to_datetime(colombo_df["time"])

time_filling = colombo_df["time"].ffill().bfill()
colombo_df = colombo_df.fillna({"time":time_filling})



