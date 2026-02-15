import pandas as pd
import numpy as np

df = pd.read_csv(r"python\numpy_project\L2_Srilanka_Temperature\data\climate_data.csv")

#working with colombo city
colombo_df = df[df["city"] == "Colombo"].copy()

#cleaning time column
colombo_df["time"] = pd.to_datetime(colombo_df["time"])
time_filling = colombo_df["time"].ffill().bfill()
colombo_df = colombo_df.fillna({"time":time_filling})

#cleaning rain column
rain_filling = colombo_df["rain"].ffill().bfill().mean()
colombo_df = colombo_df.fillna({"rain":rain_filling})

#cleaning temperature column
temp_filling = colombo_df["temperature"].ffill().bfill().mean()
colombo_df = colombo_df.fillna({"temperature":temp_filling})

#cleaning windspeed column
windspeed_filling = colombo_df["windspeed"].ffill().bfill().mean()
colombo_df = colombo_df.fillna({"windspeed":windspeed_filling})

#volatility score with temperature
temp_arr = colombo_df["temperature"].to_numpy()
avg_temp = temp_arr.mean()
std_temp = temp_arr.std()
volatility_score = abs(temp_arr - avg_temp)

print(volatility_score)

#filtering volatility status
volatility_Risk_status = np.where(volatility_score < abs(std_temp),"NO","YES")

#creating rolling average
rolling_avg = colombo_df["temperature"].rolling(window=30).mean()

#making finalized dataframe
colombo_df["VolatilityScore"] = volatility_score
colombo_df["VolatilityRiskStatus"] = volatility_Risk_status
colombo_df["30_day_avg"] = rolling_avg

#Risk in recent years
colombo_risk_df = colombo_df[(colombo_df["VolatilityRiskStatus"] == "YES") &  (colombo_df["time"] > "2020-01-01")].copy()

#average temp by year
colombo_df['year'] = colombo_df['time'].dt.year
colombo_temp_avg_byYear_df = colombo_df.groupby('year')['temperature'].mean().reset_index()
colombo_temp_avg_byYear_df.columns = ['year', 'Avg_temp_by_year']

#analyzed datas
print(f"----Colombo Temperature Analysis ----")
print(colombo_df.sample(10))
print()

print(f"----Colombo Temperature Volatility_Risk Dates ----")
print(colombo_risk_df.sample(10))
print()

print(f"----Colombo Average Temperature by year ----")
print(colombo_temp_avg_byYear_df.sample(10))
print()


#changing df to csv and saving them
colombo_df.to_csv(r"python\numpy_project\L2_Srilanka_Temperature\data\colombo_data.csv")
colombo_risk_df.to_csv(r"python\numpy_project\L2_Srilanka_Temperature\data\colombo_risk_data.csv")
colombo_temp_avg_byYear_df.to_csv(r"python\numpy_project\L2_Srilanka_Temperature\data\colombo_temp_avg.csv")