import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ['SPOTIPY_CLIENT_ID'] = "437a2286592543f1b7fcbfcad5d8a6e0"
os.environ['SPOTIPY_CLIENT_SECRET'] = "09390197fc4349d68fe51be19bb0c66e"

# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)

# print(sp.current_user_playlists())
clientID = '437a2286592543f1b7fcbfcad5d8a6e0'
clientSecret = '09390197fc4349d68fe51be19bb0c66e'
redirect_uri = 'http://127.0.0.1:9090'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 

if not os.path.exists(os.path.join(os.getcwd(), 'trackcsvs')):
    os.mkdir(os.path.join(os.getcwd(), 'trackcsvs'))
# print(os.path.join(os.getcwd(), 'trackcsvs'))
for playlist in spotifyObject.current_user_playlists()['items']:
    p_id, p_name = playlist['id'], playlist['name']
    with open(os.path.join(os.getcwd(), 'trackcsvs', f'{p_name}.csv'), 'w') as file:
        for track in spotifyObject.playlist_items(p_id)['items']:
            file.write(f'{track['track']['name']}, {track['track']['album']['name']}, {track['track']['artists'][0]['name']}\n')