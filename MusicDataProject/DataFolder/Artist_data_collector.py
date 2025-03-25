import json
import pandas as pd

# List of artists to search
artist_names_to_search = ["ian", "Don Toliver", "Yeat", "Chief Keef", "Travis Scott", "Lil Yachty", "Tyler, The Creator", "Kodak Black", "Playboi Carti", "Young Thug"]

# Load data from the JSON file
file_path = rf'MusicDataProject\DataFolder\StreamingHistory_Music_09_02_2024.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate through each artist in the list
for artist_name_to_search in artist_names_to_search:
    # Initialize a dictionary to store total listening time per day for the specified artist
    listening_data = {}

    # Iterate through the data and calculate total listening time for the artist
    for entry in data:
        if artist_name_to_search.lower() in entry['artistName'].lower() or artist_name_to_search.lower() in entry['trackName'].lower():
            date = entry['endTime'].split()[0]  # Extract the date part of endTime
            listening_time_minutes = round(entry['msPlayed'] / 60000, 2)  # Convert milliseconds to minutes
            # Accumulate listening time per day
            if date in listening_data:
                listening_data[date] += listening_time_minutes
            else:
                listening_data[date] = listening_time_minutes

    # Convert the listening data per day to a DataFrame for easier processing and saving
    listening_df = pd.DataFrame(list(listening_data.items()), columns=['Date', 'Total Minutes Listened'])

    # Save the listening data per day to a new CSV file
    output_summary_file_path = rf'MusicDataProject\DataFolder\{artist_name_to_search}_Listening_Time_Per_Day.csv'
    listening_df.to_csv(output_summary_file_path, index=False)

    print(f"Total listening data per day for {artist_name_to_search} has been saved to {output_summary_file_path}")
