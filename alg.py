# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:47:27 2023

@author: JCCarpenter
"""

import random
from statistics import stdev, mean
from main import songs
from tabulate import tabulate



total_selected_songs = []                           # declaring all lists for song selection storage
selected_songs = []

danceability = []
energy = []
speechiness =[]
acousticness = []
valence = []
tempo = []

avg_values = {}

sel_danceability = []
sel_energy = []
sel_speechiness =[]
sel_acousticness = []
sel_valence = []
sel_tempo = []



def pre_gen():
    NUM_OF_INPUT_SONGS = 2                              # minimum 10 songs
    
    chosen_song_index = []                                   # so the chosen songs can be removed before the alg starts
    
    print('type "user guide" if you need help')
    
    for i in range(NUM_OF_INPUT_SONGS):                 # function to retrieve chosen songs
        chosen_song = input(f'enter song {i + 1} out of {NUM_OF_INPUT_SONGS}: ')
        
        
        if chosen_song == 'user guide':                 # prints the user guide if 'user guide' is typed
            u_guide = open('USER GUIDE.txt', 'r')
            file_contents = u_guide.read()
            print(f'\n\n{file_contents}\n')
            
            chosen_song = input(f'enter song {i + 1} out of {NUM_OF_INPUT_SONGS}: ')    # console song selector
        
        chosen_song = int(chosen_song)                              # gathers chosen songs into an index to remove them from the possible recommendations
        chosen_song_index.append(chosen_song - 1)
        
        
        total_selected_songs.append(songs[(chosen_song - 1)])       # combines all pertinent information about the songs into a list of dicts
        
        selected_songs.append(songs[(chosen_song - 1)]['name'])
        
        sel_danceability.append(songs[(chosen_song - 1)]['danceability'])
        sel_energy.append(songs[(chosen_song - 1)]['energy'])
        sel_speechiness.append(songs[(chosen_song - 1)]['speechiness'])
        sel_acousticness.append(songs[(chosen_song - 1)]['acousticness'])
        sel_valence.append(songs[(chosen_song - 1)]['valence'])
        sel_tempo.append(songs[(chosen_song - 1)]['tempo'])
        
        
        
    avg_values = {'danceability': mean(sel_danceability),       # averages all the inputted song values
                  'energy': mean(sel_energy),
                  'speechiness': mean(sel_speechiness),
                  'acousticness': mean(sel_acousticness),
                  'valence': mean(sel_valence),
                  'tempo': mean(sel_tempo)
                  }
    
        
    
    for i in range(NUM_OF_INPUT_SONGS):                         # removes the selected songs from the algorithm
        songs.remove(songs[chosen_song_index[i - 1]])
    


def closest_value(list_a, k):
  return list_a[min(range(len(list_a)), key=lambda i: abs(list_a[i]-k))]


    
def alg():

    for i in range(len(songs)):
        danceability.append(songs[i]['danceability'])
        energy.append(songs[i]['energy'])
        speechiness.append(songs[i]['speechiness']) 
        acousticness.append(songs[i]['acousticness'])  
        valence.append(songs[i]['valence'])
        tempo.append(songs[i]['tempo'])

    
    
    rec_danceability = []                                   # rec = recommended
    rec_energy = []
    rec_speechiness = []
    rec_acousticness = []
    rec_valence = []
    rec_tempo = []
    
    for i in range(len(total_selected_songs)):                      # finds which other songs have the closest value to a chosen song per category    
        rec_danceability.append(closest_value(danceability, sel_danceability[i]))
        rec_energy.append(closest_value(energy, sel_energy[i]))
        rec_speechiness.append(closest_value(speechiness, sel_speechiness[i]))
        rec_acousticness.append(closest_value(acousticness, sel_acousticness[i]))
        rec_valence.append(closest_value(valence, sel_valence[i]))
        rec_tempo.append(closest_value(tempo, sel_tempo[i]))
        
    rec_danceability = [closest_value(rec_danceability)]
        

    
    sd_danceability = stdev(danceability) 
    sd_energy = stdev(energy)
    sd_speechiness = stdev(speechiness)
    sd_acousticness = stdev(acousticness)
    sd_valence = stdev(valence)
    sd_tempo = stdev(tempo)


    
 
pre_gen()    
    
    
    
    
    
    

#display = [['Selected Songs', selected_songs[0], selected_songs[1]],
#           ['Danceability', danceability[0], danceability[1]],
#           ['Energy', energy[0], energy[1]],
#           ['Speechiness', speechiness[0], speechiness[1]],
#           ['Acousticness', acousticness[0], acousticness[1]],
#           ['Valence', valence[0], valence[1]],
#           ['Tempo', tempo[0], tempo[1]]
#          ]

#print(f'\n{tabulate(display)}')















