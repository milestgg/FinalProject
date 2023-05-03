# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:41:45 2023

@author: JCCarpenter
"""

from main import songs
from alg import pre_gen
from statistics import stdev

danceability = []
energy = []
speechiness =[]
acousticness = []
valence = []
tempo = []

for i in range(len(songs)):
    danceability.append(songs[i]['danceability'])
    energy.append(songs[i]['energy'])
    speechiness.append(songs[i]['speechiness']) 
    acousticness.append(songs[i]['acousticness'])  
    valence.append(songs[i]['valence'])
    tempo.append(songs[i]['tempo'])  
    

print(f'danceability:\n{sorted(danceability["num"])}\n{stdev(danceability)}\n')
print(f'energy:\n{sorted(energy)}\n{stdev(energy)}\n')
print(f'speechiness:\n{sorted(speechiness)}\n{stdev(speechiness)}\n')
print(f'acousticness:\n{sorted(acousticness)}\n{stdev(acousticness)}\n')
print(f'valence:\n{sorted(valence)}\n{stdev(valence)}\n')
print(f'tempo:\n{sorted(tempo)}\n{stdev(tempo)}\n')
   