import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

clientID = 'your-client-id'
clientSecret = 'your-client-secret'
redirect_uri = 'http://127.0.0.1:9090'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 

if not os.path.exists(os.path.join(os.getcwd(), 'trackcsvs')):
    os.mkdir(os.path.join(os.getcwd(), 'trackcsvs'))
for playlist in spotifyObject.current_user_playlists()['items']:
    p_id, p_name = playlist['id'], playlist['name']
    with open(os.path.join(os.getcwd(), 'trackcsvs', f'{p_name}.csv'), 'w') as file:
        for track in spotifyObject.playlist_items(p_id)['items']:
            file.write(f'{track['track']['name']}, {track['track']['album']['name']}, {track['track']['artists'][0]['name']}\n')