import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# List of artists to search
artist_names_to_search = ["ian", "Don Toliver", "Yeat", "Chief Keef", "Travis Scott", "Lil Yachty", "Tyler The Creator", "Kodak Black", "Playboi Carti", "Young Thug"]

# Load data from CSV files for each artist
listening_dataframes = []
for artist in artist_names_to_search:
    file_path = rf'MusicDataProject\DataFolder\{artist}_Listening_Time_Per_Day.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df['Artist'] = artist
        listening_dataframes.append(df)

# Concatenate all dataframes into one
df = pd.concat(listening_dataframes, ignore_index=True)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Get the list of artists and dates
dates = df['Date'].unique()
artists = df['Artist'].unique()

# Pivot data for easier plotting
pivot_df = df.pivot(index='Date', columns='Artist', values='Total Minutes Listened').fillna(method='ffill').fillna(0)
cumulative_df = pivot_df.cumsum()

# Create figure and axis for animation
fig1, ax1 = plt.subplots(figsize=(10, 6))

# Set up initial line plots for each artist
lines = []
for artist in artists:
    line, = ax1.plot([], [], label=artist, linewidth=2)
    lines.append(line)

# Set up the axes
ax1.set_xlim(cumulative_df.index.min(), cumulative_df.index.max())
max_listened = cumulative_df.max().max()
initial_ylim_upper = ((max_listened // 1000) + 1) * 1000
ax1.set_ylim(0, 1100)
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Minutes Listened')
ax1.set_title('Cumulative Artist Listening Over Time')
artist_totals = cumulative_df.iloc[-1].sort_values(ascending=False)
ax1.legend([artist for artist in artist_totals.index], loc='upper left', bbox_to_anchor=(1, 1), frameon=False, title='Artists', prop={'size': 9})
ax1.yaxis.set_major_locator(plt.MultipleLocator(100))
ax1.yaxis.set_minor_locator(plt.MultipleLocator(500))

# Update function for animation
def update(num):
    start_index = 0
    end_index = num
    for i, artist in enumerate(artists):
        lines[i].set_data(cumulative_df.index[:num], cumulative_df[artist][:num])
    
    # Adjust the x-axis limit to keep the data in the middle
    if num > 7:
        start_index = max(0, num - 7)
        end_index = min(len(cumulative_df.index) - 1, num + 7)
        ax1.set_xlim(cumulative_df.index[start_index], cumulative_df.index[end_index])
    
    # Update the x-axis labels dynamically with a week's worth of labels
    ax1.set_xticks(cumulative_df.index[start_index:end_index])
    ax1.set_xticklabels([date.strftime('%b %d') for date in cumulative_df.index[start_index:end_index]], rotation=45)
    ax1.figure.canvas.draw()  # Force a redraw of the figure to update the x-axis labels
    
    return lines

# Create the animation
ani = animation.FuncAnimation(fig1, update, frames=len(dates), blit=True, repeat=True)

# Show the animation in a separate window
plt.figure(fig1.number)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=False)

# Show the final plot with full data in a separate window
fig2, ax2 = plt.subplots(figsize=(10, 6))
for i, artist in enumerate(artist_totals.index):
    ax2.plot(cumulative_df.index, cumulative_df[artist], label=artist, linewidth=2)
ax2.set_xlim(pd.Timestamp('2024-09-02'), pd.Timestamp('2024-12-02'))
ax2.set_ylim(0, 1100)
ax2.xaxis.set_major_locator(plt.MultipleLocator(7))
ax2.set_xticks(pd.date_range(start='2024-09-02', end='2024-12-02', freq='7D'))
ax2.set_xticklabels([date.strftime('%b %d') for date in pd.date_range(start='2024-09-02', end='2024-12-02', freq='7D')])
ax2.set_xlabel('Date')
ax2.set_ylabel('Total Minutes Listened')
ax2.set_title('Cumulative Artist Listening Over Time - Full Data')
ax2.legend([artist for artist in artist_totals.index], loc='upper left', bbox_to_anchor=(1, 1), frameon=False, title='Artists', prop={'size': 9})
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
