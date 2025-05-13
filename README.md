# 🛒 Supermarket Sales Analysis

This project provides a comprehensive analysis of supermarket sales data using Python and Jupyter Notebook. It includes data cleaning, feature engineering, outlier handling, and insightful visualizations to uncover key patterns and trends.

---

## 📁 Project Structure

super_market_sales_analysis/
│
├── supermarket_sales_mock.csv # Raw dataset
├── supermarket_sales_analysis.ipynb # Jupyter notebook with complete analysis
└── output/
└── city_sales.png # Saved visualization of sales by city


---

## 🧪 Dataset

The dataset contains records of customer transactions in a supermarket, including:
- Invoice ID
- Branch and City
- Customer type and Gender
- Product line
- Total sales
- Payment method
- Date and Time of purchase

---

## 📊 Key Objectives

- Clean and preprocess the data
- Perform summary statistics
- Engineer new features (e.g., Month, Day)
- Identify outliers and trends
- Visualize total sales by city

---

## ✅ Features Implemented

| Feature                                     | Description                                                  |
|--------------------------------------------|--------------------------------------------------------------|
| 🔍 Data Cleaning & Missing Values           | Handled nulls and ensured consistency                        |
| 🏗 Feature Engineering                      | Extracted `Month`, `Day` from transaction dates              |
| 📈 Data Integrity                           | Converted data types and removed corrupt entries             |
| 📊 Summary Statistics                       | Descriptive stats and value distribution checks              |
| 🔍 Outlier Detection                        | Used IQR method to filter sales outliers                     |
| 📉 Visualization                            | Bar plot of total sales by city (saved to `/output`)         |

---

## 📦 Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

Install requirements using:

```bash
pip install pandas matplotlib seaborn notebook
