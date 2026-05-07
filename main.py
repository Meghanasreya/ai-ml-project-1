import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Total sales
print("Total Sales:", data["Sales"].sum())

# Best selling product
print("\nSales by Product:")
print(data.groupby("Product")["Sales"].sum())

# Profit by category
print("\nProfit by Category:")
print(data.groupby("Category")["Profit"].sum())

# Graph
sales_by_product = data.groupby("Product")["Sales"].sum()

sales_by_product.plot(kind="bar")

plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales by Product")
plt.show()