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

# Highlight the top song of the week every Monday
mondays_df = filtered_df[filtered_df['Date'].dt.weekday == 0]
for i, row in mondays_df.iterrows():
    if pd.notna(row['Top Song Of the Week (Monday)']):
        plt.plot([row['Date'], row['Date']], [0, filtered_df['Time (minutes)'].max()], color='red', linestyle='--', label='Top Song of the Week' if i == mondays_df.index[0] else "")
        plt.text(row['Date'], filtered_df['Time (minutes)'].max() + 10, row['Top Song Of the Week (Monday)'], color='red', fontsize=7, ha='center')

# Highlight the maximum point
max_point = filtered_df['Time (minutes)'].idxmax()

plt.scatter(filtered_df.loc[max_point, 'Date'], filtered_df.loc[max_point, 'Time (minutes)'], color='#00b7c7', s=100, label='Peak', zorder=5)

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
