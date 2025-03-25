import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet data into a DataFrame
sheet1_weekly_data = pd.read_excel('MusicDataProject\Music Data.xlsx', sheet_name='Sheet1')

# Convert 'Date' column to datetime
sheet1_weekly_data['Date'] = pd.to_datetime(sheet1_weekly_data['Date'])

# Extract day of the week information
sheet1_weekly_data['DayOfWeek'] = sheet1_weekly_data['Date'].dt.day_name()

# Group data by day of the week and calculate the average listening time
average_listening_per_day = sheet1_weekly_data.groupby('DayOfWeek')['Time (minutes)'].mean()

# Define the order of days for plotting
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Sort the average listening time data by the correct day order
average_listening_per_day = average_listening_per_day.reindex(days_order)

# Plotting average listening time per day of the week
plt.figure(figsize=(10, 6))

# Line chart for average listening time by day of the week
plt.plot(average_listening_per_day.index, average_listening_per_day.values, marker='o', color='navy', linestyle='-', linewidth=2)

# Formatting the plot
plt.xlabel('Day of the Week')
plt.ylabel('Average Time (minutes)')
plt.title('Average Listening Time by Day of the Week')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()