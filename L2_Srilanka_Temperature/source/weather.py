import pandas as pd
import numpy as np

df = pd.read_csv(r"python\numpy_project\L2_Srilanka_Temperature\data\climate_data.csv")

colombo_df = df[df["city"] == "Colombo"].copy()
colombo_df["time"] = pd.to_datetime(colombo_df["time"])
print(colombo_df.sample(5))
