import matplotlib.pyplot as plt

# Data for the pie chart
artists = [
    "ian", "Don Toliver", "Young Thug", "Travis Scott", "Yeat",
    "Tyler, The Creator", "Kodak Black", "Chief Keef", "Playboi Carti", "Lil Yachty"
]
minutes = [
    1035.66, 957.61, 946.07, 901.20, 900.30,
    817.33, 729.93, 706.11, 530.44, 475.54
]

# Assigning colors to each artist
colors = [
    "tab:blue",    # ian
    "tab:orange",  # Don Toliver
    "tab:green",   # Young Thug
    "tab:red",     # Travis Scott
    "tab:purple",  # Yeat
    "tab:brown",   # Tyler, The Creator
    "tab:pink",    # Kodak Black
    "tab:gray",    # Chief Keef
    "tab:olive",   # Playboi Carti
    "tab:cyan"     # Lil Yachty
]

# Calculating percentages
total_minutes = sum(minutes)
percentages = [(minute / total_minutes) * 100 for minute in minutes]
labels = [f"{artist} ({percentage:.1f}%)" for artist, percentage in zip(artists, percentages)]

# Plotting the pie chart
plt.figure(figsize=(10, 10))
plt.pie(minutes, labels=labels, colors=colors, autopct='', startangle=140, wedgeprops={'edgecolor': 'black'}, labeldistance=1.05)
plt.title('Listening Time Distribution by Artist (%)')
plt.axis('equal')  # Ensure pie chart is circular
plt.show()
