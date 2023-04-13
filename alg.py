# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:47:27 2023

@author: JCCarpenter
"""

import random
from statistics import mean
from main import songs
from tabulate import tabulate



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

print('type "user guide" if you need help')

for i in range(NUM_OF_INPUT_SONGS):
    chosen_song = input(f'enter song {i + 1} out of {NUM_OF_INPUT_SONGS}: ')
    
    if chosen_song == 'user guide':
        u_guide = open('USER GUIDE.txt', 'r')
        file_contents = u_guide.read()
        print(f'\n\n{file_contents}\n')
        
        chosen_song = input(f'enter song {i + 1} out of {NUM_OF_INPUT_SONGS}: ')
    
    chosen_song = int(chosen_song)
    
    total_selected_songs.append(songs[(chosen_song - 1)])
    
    selected_songs.append(songs[(chosen_song - 1)]['name'])
    
    danceability.append(songs[(chosen_song - 1)]['danceability'])
    energy.append(songs[(chosen_song - 1)]['energy'])
    speechiness.append(songs[(chosen_song - 1)]['speechiness'])
    acousticness.append(songs[(chosen_song - 1)]['acousticness'])
    valence.append(songs[(chosen_song - 1)]['valence'])
    tempo.append(songs[(chosen_song - 1)]['tempo'])
    

display = [['Selected Songs', selected_songs[0], selected_songs[1]],
           ['Danceability', danceability[0], danceability[1]],
           ['Energy', energy[0], energy[1]],
           ['Speechiness', speechiness[0], speechiness[1]],
           ['Acousticness', acousticness[0], acousticness[1]],
           ['Valence', valence[0], valence[1]],
           ['Tempo', tempo[0], tempo[1]]
          ]

print(f'\n{tabulate(display)}')
