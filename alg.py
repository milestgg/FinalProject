# -*- coding: utf-8 -*-

# ..... ALGORITHM SUMMARY ..... #

# 1. Retrieves the selected playlist from Spotify
#
# 2. Gathers all metadata about songs in playlist and creates a list
#
# 3. Matches a song with the closest metadata to a selected song for every category
#    of metadata
#
# 4. Averages out all the metadata values for each song and selects song with the
#    closest metadata to the averages for each value
#
# 5. Combine all the songs into a list

# ..... ALGORITHM SUMMARY ..... #



import random
from statistics import stdev, mean
from main import songs
from tabulate import tabulate
import numpy as np


total_selected_songs = []                           # declaring all lists for song selection storage
selected_songs = []
recommended_songs = []

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



NUM_OF_INPUT_SONGS = 10                             # minimum 10 songs



def test(lsts, key):
  return [x.get(key) for x in lsts]



def pre_gen(playid, song_choices):
    
    chosen_song_index = []                                   # so the chosen songs can be removed before the alg starts
    
    #print('type "user guide" if you need help')
    
    #for i in range(NUM_OF_INPUT_SONGS):                 # function to retrieve chosen songs
    #    chosen_song = input(f'enter song {i + 1} out of {NUM_OF_INPUT_SONGS}: ')
        
        
     #   if chosen_song == 'user guide':                 # prints the user guide if 'user guide' is typed
    #        u_guide = open('USER GUIDE.txt', 'r')
    #        file_contents = u_guide.read()
     #       print(f'\n\n{file_contents}\n')
            
            #chosen_song = input(f'enter song {i + 1} out of {NUM_OF_INPUT_SONGS}: ')    # console song selector
        
    chosen_song = 0
    for i in range(NUM_OF_INPUT_SONGS):
        chosen_song = int(song_choices[i])                              # gathers chosen songs into an index to remove them from the possible recommendations
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
    
        
    chosen_song_index.sort(reverse = True)              # removes the selected songs from the list so they arent recommended
    for i in range(len(chosen_song_index)):
        del songs[chosen_song_index[i]]
    
 

def closest_value(list_a, k):                                   # value to calc the closest value of all entries in a list
  return list_a[min(range(len(list_a)), key=lambda i: abs(list_a[i]-k))]



def algorithm():
    for i in range(len(songs)):
        danceability.append({'name': songs[i]['name'], 'value': songs[i]['danceability']})
        energy.append({'name': songs[i]['name'], 'value': songs[i]['energy']})
        speechiness.append({'name': songs[i]['name'], 'value': songs[i]['speechiness']}) 
        acousticness.append({'name': songs[i]['name'], 'value': songs[i]['acousticness']})  
        valence.append({'name': songs[i]['name'], 'value': songs[i]['valence']})
        tempo.append({'name': songs[i]['name'], 'value': songs[i]['tempo']})

    
    rec_danceability = []                                   # rec = recommended
    avg_danceability = mean(sel_danceability)
    rec_energy = []
    avg_energy = mean(sel_energy)
    rec_speechiness = []
    avg_speechiness = mean(sel_speechiness)
    rec_acousticness = []
    avg_acousticness = mean(sel_acousticness)
    rec_valence = []
    avg_valence = mean(sel_valence)
    rec_tempo = []
    avg_tempo = mean(sel_tempo)
    
    for i in range(NUM_OF_INPUT_SONGS):                      # finds which other songs have the closest value to a chosen song per category 
        random.shuffle(danceability)
        vals = [a_dict['value'] for a_dict in danceability]
        random.shuffle(vals) 
        dan = closest_value(vals, sel_danceability[i])      # added all the closest values to a list and difference between their number and the closest one
        rec_danceability.append({'name': danceability[i]['name'], 'closest song value': dan, 'difference': abs(dan - sel_danceability[i])})
        
        random.shuffle(energy)
        vals = [a_dict['value'] for a_dict in energy]
        random.shuffle(vals) 
        ene = closest_value(vals, sel_energy[i])
        rec_energy.append({'name': energy[i]['name'], 'closest song value': ene, 'difference': abs(ene - sel_energy[i])})
        
        random.shuffle(speechiness)
        vals = [a_dict['value'] for a_dict in speechiness]
        random.shuffle(vals) 
        spe = closest_value(vals, sel_speechiness[i])
        rec_speechiness.append({'name': speechiness[i]['name'], 'closest song value': spe, 'difference': abs(spe - sel_speechiness[i])})
        
        random.shuffle(acousticness)
        vals = [a_dict['value'] for a_dict in acousticness]
        random.shuffle(vals) 
        aco = closest_value(vals, sel_acousticness[i])
        rec_acousticness.append({'name': acousticness[i]['name'], 'closest song value': aco, 'difference': abs(aco - sel_acousticness[i])})
        
        random.shuffle(valence)
        vals = [a_dict['value'] for a_dict in valence]
        random.shuffle(vals) 
        val = closest_value(vals, sel_valence[i])
        rec_valence.append({'name': valence[i]['name'], 'closest song value': val, 'difference': abs(val - sel_valence[i])})
        
        random.shuffle(tempo)
        vals = [a_dict['value'] for a_dict in tempo]
        random.shuffle(vals) 
        tem = closest_value(vals, sel_tempo[i])
        rec_tempo.append({'name': tempo[i]['name'], 'closest song value': tem, 'difference': abs(tem - sel_tempo[i])})
        
      
        
    random.shuffle(rec_danceability)  
    rec_danceability = min(rec_danceability, key=lambda x:x['difference'])           # computes the actual closest number
    recommended_songs.append({'name': danceability[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(rec_energy)  
    rec_energy = min(rec_energy, key=lambda x:x['difference'])
    recommended_songs.append({'name': energy[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(rec_speechiness)  
    rec_speechiness = min(rec_speechiness, key=lambda x:x['difference'])
    recommended_songs.append({'name': speechiness[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(rec_acousticness)  
    rec_acousticness = min(rec_acousticness, key=lambda x:x['difference'])
    recommended_songs.append({'name': acousticness[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(rec_valence)  
    rec_valence = min(rec_valence, key=lambda x:x['difference'])
    recommended_songs.append({'name': valence[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(rec_tempo)  
    rec_tempo = min(rec_tempo, key=lambda x:x['difference'])
    recommended_songs.append({'name': tempo[NUM_OF_INPUT_SONGS]['name']}) 

    
    ### CLOSEST NEW SONG VALUES TO AVERAGED VALUES ###
    random.shuffle(danceability) 
    vals = [a_dict['value'] for a_dict in danceability]
    avg_danceability = closest_value(vals, avg_danceability)           # computes the actual closest number
    recommended_songs.append({'name': danceability[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(energy)  
    vals = [a_dict['value'] for a_dict in energy]
    avg_energy = closest_value(vals, avg_energy)           # computes the actual closest number
    recommended_songs.append({'name': energy[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(speechiness) 
    vals = [a_dict['value'] for a_dict in danceability]
    avg_speechiness = closest_value(vals, avg_acousticness)           # computes the actual closest number
    recommended_songs.append({'name': speechiness[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(acousticness) 
    vals = [a_dict['value'] for a_dict in acousticness]
    avg_acousticness = closest_value(vals, avg_acousticness)           # computes the actual closest number
    recommended_songs.append({'name': acousticness[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(valence)  
    vals = [a_dict['value'] for a_dict in valence]
    avg_valence = closest_value(vals, avg_valence)           # computes the actual closest number
    recommended_songs.append({'name': valence[NUM_OF_INPUT_SONGS]['name']})
    
    random.shuffle(tempo)  
    vals = [a_dict['value'] for a_dict in tempo]
    avg_tempo = closest_value(vals, avg_tempo)           # computes the actual closest number
    recommended_songs.append({'name': tempo[NUM_OF_INPUT_SONGS]['name']})
    

    
    return recommended_songs
    

#pre_gen()    
#algorithm()
    
    
    
    
    
    



