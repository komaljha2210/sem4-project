import pandas as pd

# Load the uploaded CSV file
file_path = 'C:/Users/Komal Jha/Documents/BITS Sem 4/Dataset/Sales_Profit_Data_Electrical_Appliances.csv'
data = pd.read_csv(file_path)

# Display basic information and the first few rows
data_info = data.info()
data_head = data.head()

print(data_info)
print(data_head)

# Step 1: Convert 'Order Date' to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')

# Step 2: Check for missing values
missing_values = data.isnull().sum()

# Step 3: Check for duplicates
duplicates_count = data.duplicated().sum()

# Step 4: Summary statistics for numerical columns to check for anomalies
numerical_summary = data.describe()

# Display preprocessing insights
missing_values, duplicates_count, numerical_summary

import matplotlib.pyplot as plt
import seaborn as sns

# Define numerical columns for visualization
numerical_columns = ['Unit Cost', 'Price', 'Order Qty', 'Cost of Sales', 'Sales', 'Profit']

# Create boxplots for numerical columns to visualize outliers
plt.figure(figsize=(16, 12))
for i, col in enumerate(numerical_columns, start=1):
    plt.subplot(3, 2, i)
    sns.boxplot(data[col])
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)

plt.tight_layout()
plt.show()


