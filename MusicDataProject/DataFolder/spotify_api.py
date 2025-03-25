import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
import os

# Spotify API credentials
CLIENT_ID = "" # Add your own Spotify API client ID
CLIENT_SECRET = "" # Add your own Spotify API client secret
REDIRECT_URI = "http://localhost:8888/callback"

# List of artists to search
artist_names_to_search = ["ian", "Don Toliver", "Yeat", "Chief Keef", "Travis Scott", "Lil Yachty", "Tyler The Creator", "Kodak Black", "Playboi Carti", "Young Thug"]

# Function to run the Spotify data collection
def collect_spotify_data():
    # Authentication with Spotify API
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope="user-read-recently-played"))

    # Fetch recently played tracks from the past 24 hours
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=1)

    results = []

    # Fetch recently played tracks for the past 24 hours
    try:
        recently_played = sp.current_user_recently_played(limit=50, after=int(start_date.timestamp() * 1000))
        items = recently_played['items']
        results.extend(items)
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error occurred: {e}")

    # Extract listening time per artist from the past 24 hours
    data = {
        'Date': [],
        'Total Minutes Listened': []
    }
    artist_minutes = {artist: 0 for artist in artist_names_to_search}

    for item in results:
        track = item['track']
        artist_names = [artist['name'].lower() for artist in track['artists']]
        played_at = datetime.datetime.strptime(item['played_at'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
        minutes_listened = track['duration_ms'] / 60000
        
        for artist in artist_names_to_search:
            if artist.lower() in artist_names:
                artist_minutes[artist] += minutes_listened

    # Prepare data for output
    current_date = start_date
    for artist, minutes in artist_minutes.items():
        artist_file_path = rf'MusicDataProject\DataFolder\{artist}_Listening_Time_Per_Day.csv'
        if os.path.exists(artist_file_path):
            artist_df = pd.read_csv(artist_file_path, parse_dates=['Date'])
        else:
            artist_df = pd.DataFrame(columns=['Date', 'Total Minutes Listened'])
        
        # Update or append the new data
        if current_date.strftime('%Y-%m-%d %H:%M:%S') in artist_df['Date'].astype(str).values:
            artist_df.loc[artist_df['Date'] == current_date, 'Total Minutes Listened'] = minutes
        else:
            new_data = pd.DataFrame({'Date': [current_date.strftime('%Y-%m-%d %H:%M:%S')], 'Total Minutes Listened': [minutes]})
            artist_df = pd.concat([artist_df, new_data], ignore_index=True)
        
        # Save back to CSV
        artist_df.drop_duplicates(subset=['Date'], keep='last', inplace=True)
        artist_df.to_csv(artist_file_path, index=False)

    # Output the minutes listened to each artist in the past 24 hours in the desired format
    for artist, minutes in artist_minutes.items():
        print(f"{artist}: {minutes} minutes")

# Run the Spotify data collection function immediately
collect_spotify_data()
