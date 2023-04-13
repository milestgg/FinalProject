# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:47:27 2023

@author: JCCarpenter
"""

import random
from statistics import mean
from main import songs



NUM_OF_INPUT_SONGS = 2                              # minimum 10 songs



total_selected_songs = []                           # declaring all lists for song selection storage
selected_songs = []
danceability = []
energy = []
speechiness =[]
acousticness = []
valence = []
tempo = []
avg_values = {}



for i in range(NUM_OF_INPUT_SONGS):
    chosen_song = int(input(f'enter song {i + 1} out of {NUM_OF_INPUT_SONGS}: '))
    total_selected_songs.append(songs[(chosen_song - 1)])
    
    selected_songs.append(songs[(chosen_song - 1)]['name'])
    
    danceability.append(songs[(chosen_song -1)]['danceability'])
    energy.append(songs[(chosen_song -1)]['energy'])
    speechiness.append(songs[(chosen_song -1)]['speechiness'])
    acousticness.append(songs[(chosen_song -1)]['acousticness'])
    valence.append(songs[(chosen_song -1)]['valence'])
    tempo.append(songs[(chosen_song -1)]['tempo'])
    

print(selected_songs)
print(danceability)
print(energy)
print(speechiness)
print(acousticness)
print(valence)
print(tempo)





