# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:41:40 2023

@author: JCCarpenter
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ids import CLIENT_ID, CLIENT_SECRET
import base64
from requests import post, get
import json


PLAYLIST_ID = '37i9dQZF1EIgIwPJju1vhX'
#PLAYLIST_ID = '6UeSakyzhiEt4NB3UAd6NQ'



#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)



songs = []



def get_token():                                           # gets token from spotify development to use API
    auth_string = CLIENT_ID + ':' + CLIENT_SECRET
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')
    
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    data = {'grant_type': 'client_credentials'}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token



def get_playlist(token):                                    # retrieves the songs from a playlist
    url = f'https://api.spotify.com/v1/playlists/{PLAYLIST_ID}?country=US'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result
    
    

def get_auth_header(token):                                 # aquires auth header for retrieving songs and playlists
    return {'Authorization': 'Bearer ' + token}



def main():
    token = get_token()                                     # aquires token
    
    song_list = get_playlist(token)                         # pulls songs from playlist
        
        
    
    for i in range(len(song_list['items'])):                # builds custom list of dictionaries containing all pertinent information needed about each song
        rank = i + 1
        song_name = song_list['items'][i]['track']['name']
        artist_name = song_list['items'][i]['track']['artists'][0]['name']
        song_id = song_list['items'][i]['track']['id']
        
        song_data = sp.audio_features(song_id)[0]       # extracts song data from spotipy
        
        song_danceability = song_data['danceability']
        song_energy = song_data['energy']
        song_speechiness = song_data['speechiness']
        song_acousticness = song_data['acousticness']
        song_valence = song_data['valence']
        song_tempo = song_data['tempo']
        
        # adds all song data to a dictionary, and appends new dictionary to a list
        songs.append({'name': song_name, 'artist': artist_name, 'rank': rank, 'id': song_id,
                      'danceability': song_danceability, 'energy': song_energy, 'speechiness': song_speechiness,
                      'acousticness': song_acousticness, 'valence': song_valence, 'tempo': song_tempo
                      })
    
    
    for i in range(len(songs)):                             # prints list of songs
       print(f'{songs[i]["rank"]}. {songs[i]["name"]}\n    By: {songs[i]["artist"]}\n    {songs[i]["id"]}\n')
    




main()