
import requests
import spotipy
import pprint
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

#To export variable to environment: TERMINAL >>> SPOTIPY_CLIENT_ID=""
SPOTIPY_TOKEN = "BQBwBtKSSCdGKj2-ECwCTCY7lUQFmjltV_ZBpKxMS_16Xb0bmS_yZmOzVrdmi-IbFwc0kaCuDvs_-0p4iiIb-zBiPz0MMv44ZveXDgEdPMnIQD4IF2acamnOCSdz-d6nE7QtDw_q2jeUOfweRuc-uTeZIuc8XyKAkY1fyMGj6W31mIebTt0s9cDuZoDNj2Wo3pKSIw"

SPOTIFY_CLIENT_ID = "8dce6f9fbc8f487095703c83eb351fea",
SPOTIFY_CLIENT_SECRET = "f15154addeda46acb9fabd44a7603fa0",
SPOTIFY_REDIRECT_URI="http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

spotipy.client.Spotify(
    auth=SPOTIPY_TOKEN,
    requests_session=True,
    client_credentials_manager=None,
    oauth_manager=None,
    auth_manager=None,
    proxies=None,
    requests_timeout=5,
    status_forcelist=None,
    retries=3,
    status_retries=3,
    backoff_factor=0.3
)

date = input("For what year you would like to travel to? [YYYY-MM-DD]:\n")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
website_date = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

songs_uris = []
for music in website_date:
    songs_uris.append(music.get_text())

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(songs_uris)

playlist = sp.user_playlist_create(
    user_id=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description="A playlist created by a Python code that gather the 100 top music of a user-selected day in the past 20 years. The info comes from Billboard Hot 100."
)

sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)