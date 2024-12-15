import requests
from bs4 import BeautifulSoup
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Billboard scraping
date_entry = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date_entry}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(URL, headers=header)
datas = response.text

# Parse HTML for song titles
soup = BeautifulSoup(datas, "html.parser")
top_songs = soup.select("li ul li h3")
songs = [song.getText().strip() for song in top_songs]

# Spotify OAuth
Client_ID = "YOUR_CLIENT_ID"
Client_secret = "YOUR_CLIENT_SECRET"
REDIRECT_URI = "YOUR_REDIRECT_URI"

sp = Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=Client_ID,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Get user ID
user_id = sp.current_user()["id"]

# Search for song URIs on Spotify
song_uris = []
year = date_entry.split("-")[0]
for song in songs:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Could not find {song} on Spotify. Skipping...")

# Create playlist and add songs
playlist = sp.user_playlist_create(user=user_id, name=f"{date_entry} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"Playlist created successfully: {playlist['external_urls']['spotify']}")

