# Sales Dashboard Analysis
# Author: Yue Dai

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Load dataset
# ---------------------------
df = pd.read_csv("sales_data.csv")

print("Dataset Preview:")
print(df.head())

# ---------------------------
# Total Revenue
# ---------------------------
df["Revenue"] = df["Price"] * df["Quantity"]
total_revenue = df["Revenue"].sum()

print("\nTotal Revenue:", total_revenue)

# ---------------------------
# Top Products
# ---------------------------
top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop Products:")
print(top_products)

# ---------------------------
# Monthly Trend
# ---------------------------
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

monthly = df.groupby("Month")["Revenue"].sum()

# Plot
monthly.plot(title="Monthly Revenue Trend", figsize=(8,5))
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
