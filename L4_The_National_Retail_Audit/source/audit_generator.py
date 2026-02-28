import pandas as pd
import numpy as np
import os

# Define the target directory based on your path
target_dir = r"python\numpy_project\L4_The_National_Retail_Audit\data"

# Create the directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 1. Generate Sales Data (2025 Transactions)
np.random.seed(42)
# Using lowercase "2h" to avoid the Frequency Error
dates = pd.date_range(start="2025-01-01", periods=500, freq="2h")

sales_data = {
    'Order_ID': np.arange(1000, 1500),
    'Product_ID': np.random.choice([101, 102, 103, 104, 105], 500),
    'Quantity': np.random.randint(-5, 50, 500), # Includes returns (negatives)
    'Timestamp': dates
}

df_sales = pd.DataFrame(sales_data)

# Introduce 20 random missing timestamps for the "Recovery" task
missing_indices = np.random.choice(df_sales.index, 20, replace=False)
df_sales.loc[missing_indices, 'Timestamp'] = np.nan

# Save Sales Data
df_sales.to_csv(os.path.join(target_dir, 'sales_2025.csv'), index=False)

# 2. Generate Product Master
products = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Price': [1500, 2500, 500, 4500, 1200],
    'Category': ['Grains', 'Dairy', 'Spices', 'Electronics', 'Dairy']
}
pd.DataFrame(products).to_csv(os.path.join(target_dir, 'product_master.csv'), index=False)

# 3. Generate Regional Targets
targets = {
    'Category': ['Grains', 'Dairy', 'Spices', 'Electronics'],
    'Target_Revenue': [50000, 80000, 20000, 150000]
}
pd.DataFrame(targets).to_csv(os.path.join(target_dir, 'regional_targets.csv'), index=False)

print(f"✅ Success! Files generated in: {target_dir}")