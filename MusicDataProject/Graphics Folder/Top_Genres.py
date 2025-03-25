import matplotlib.pyplot as plt

# Data for the pie chart
genres = [
    "rap", "hip hop", "trap", "underground hip hop", "pop",
    "melodic rap", "alt hip hop", "dance pop", "southern hip hop", "pluggnb"
]
percentages = [
    28, 16, 16, 7, 7,
    7, 6, 5, 4, 4
]

# Assigning colors to each genre from the previous palette
colors = [
    "tab:blue",    # rap
    "tab:orange",  # hip hop
    "tab:green",   # trap
    "tab:red",     # underground hip hop
    "tab:purple",  # pop
    "tab:brown",   # melodic rap
    "tab:pink",    # alt hip hop
    "tab:gray",    # dance pop
    "tab:olive",   # southern hip hop
    "tab:cyan"     # pluggnb
]

# Labels with percentages
genre_labels = [f"{genre} ({percentage}%)" for genre, percentage in zip(genres, percentages)]

# Plotting the pie chart
plt.figure(figsize=(10, 10))
plt.pie(percentages, labels=genre_labels, colors=colors, autopct='', startangle=140, wedgeprops={'edgecolor': 'black'}, labeldistance=1.05)
plt.title('Top Genres')
plt.axis('equal')  # Ensure pie chart is circular
plt.show()
