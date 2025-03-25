import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet data into a DataFrame
sheet1_data = pd.read_excel('MusicDataProject\Music Data.xlsx', sheet_name='Sheet1')

# Convert 'Date' column to datetime
sheet1_data['Date'] = pd.to_datetime(sheet1_data['Date'])

# Filter data for September to November
filtered_data = sheet1_data[(sheet1_data['Date'].dt.month >= 9) & (sheet1_data['Date'].dt.month <= 11)]

# Extract month information and sum the listening time per month
filtered_data['Month'] = filtered_data['Date'].dt.month
monthly_sum = filtered_data.groupby('Month')['Time (minutes)'].sum()

# Plotting total listening time per month from September to November
plt.figure(figsize=(8, 5))

# Bar chart for total listening time by month
plt.bar(monthly_sum.index, monthly_sum.values, color='darkblue', alpha=1.0, zorder=3)

# Formatting the plot
plt.xlabel('Month')
plt.ylabel('Total Time (minutes)')
plt.title('Total Listening Time per Month (September to November)')
plt.xticks(ticks=[9, 10, 11], labels=['September', 'October', 'November'])
plt.grid(axis='y', zorder=0)

# Show the plot
plt.tight_layout()
plt.show()