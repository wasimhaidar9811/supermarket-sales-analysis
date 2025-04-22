import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv(r'C:\Users\Wasim\Desktop\supermarket_sales_mock.csv')

# Basic data analysis
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Example of some analysis (total sales by city)
sales_by_city = df.groupby('City')['Total'].sum().reset_index()

# Plot the results
plt.figure(figsize=(10, 6))
plt.bar(sales_by_city['City'], sales_by_city['Total'], color='skyblue')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.title('Total Sales by City')

# Ensure the 'output' folder exists
output_folder = 'C:/Users/Wasim/Desktop/data analytics project/output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save the plot to the 'output' folder
plt.savefig(f'{output_folder}/city_sales.png')

# Display the plot
plt.show()
