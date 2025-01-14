import pandas as pd

# Load the uploaded CSV file
file_path = 'C:/Users/Komal Jha/Documents/BITS Sem 4/Dataset/Sales_Profit_Data_Electrical_Appliances.csv'
data = pd.read_csv(file_path)

# Display basic information and the first few rows
data_info = data.info()
data_head = data.head()

print(data_info)
print(data_head)
