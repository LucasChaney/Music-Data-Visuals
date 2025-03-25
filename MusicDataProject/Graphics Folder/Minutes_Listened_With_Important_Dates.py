import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

# Load the dataset
file_path = r'MusicDataProject\Music Data.xlsx'

# Use openpyxl engine to handle .xlsx files
xls = pd.ExcelFile(file_path, engine='openpyxl')
df = pd.read_excel(xls, sheet_name='Sheet1')

# Convert 'Date' to datetime for proper plotting
df['Date'] = pd.to_datetime(df['Date'])

# Filter out rows without 'Time (minutes)' to avoid plotting NaN values
filtered_df = df.dropna(subset=['Time (minutes)'])

# Create the line plot for minutes listened per day
plt.figure(figsize=(12, 6))
plt.plot(filtered_df['Date'], filtered_df['Time (minutes)'], marker='o', linestyle='-', color='#1a53ff', label='Minutes Listened')

# Highlight the maximum point
max_point = filtered_df['Time (minutes)'].idxmax()

plt.scatter(filtered_df.loc[max_point, 'Date'], filtered_df.loc[max_point, 'Time (minutes)'], color='#00b7c7', s=100, label='Peak', zorder=5)

# Add lines and labels for specific dates and events
plt.axvline(pd.to_datetime('2024-11-22'), color='green', linestyle='--', label='GNX')
plt.text(pd.to_datetime('2024-11-22'), filtered_df['Time (minutes)'].max() + 10, 'GNX', color='green', fontsize=8, ha='center')

plt.axvline(pd.to_datetime('2024-10-28'), color='purple', linestyle='--', label='Chromakopia')
plt.text(pd.to_datetime('2024-10-28'), filtered_df['Time (minutes)'].max() + 10, 'Chromakopia', color='purple', fontsize=8, ha='center')

# Mark and connect dates for Road Trip (October 30th to November 1st)
plt.plot([pd.to_datetime('2024-10-30'), pd.to_datetime('2024-11-01')], [filtered_df['Time (minutes)'].max() + 20, filtered_df['Time (minutes)'].max() + 20], color='orange', linestyle='-', label='Road Trip')
plt.text(pd.to_datetime('2024-10-31'), filtered_df['Time (minutes)'].max() + 30, 'Road Trip', color='orange', fontsize=8, ha='center')

# Mark and connect dates for Road Trip (November 27th to November 29th)
plt.plot([pd.to_datetime('2024-11-27'), pd.to_datetime('2024-11-29')], [filtered_df['Time (minutes)'].max() + 20, filtered_df['Time (minutes)'].max() + 20], color='red', linestyle='-', label='Road Trip')
plt.text(pd.to_datetime('2024-11-28'), filtered_df['Time (minutes)'].max() + 30, 'Road Trip', color='red', fontsize=8, ha='center')

# Set labels and title
plt.xlabel('Date', fontsize=12)
plt.ylabel('Minutes Listened', fontsize=12)
plt.title('Music Listening Trends Since September (2024)', fontsize=16)
plt.xticks(pd.date_range(start='2024-09-02', end='2024-12-02', freq='7D'), labels=pd.date_range(start='2024-09-02', end='2024-12-02', freq='7D').strftime('%b %d'), rotation=45, fontsize=10)

# Customize grid
plt.grid(visible=True, linestyle='--', linewidth=0.5)

# Set minor ticks on y-axis every 25
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(25))
plt.gca().tick_params(axis='y', which='minor', length=4, color='gray')

# Set a subtle background color
plt.gca().set_facecolor('#f9f9f9')

# Show the plot
plt.tight_layout()
plt.show()
