# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:33:43 2023

@author: JCCarpenter
"""

from song_class import Song
from song_list import temp_songs

object_songs = []
g_rap = []
g_country = []
g_rock = []
g_softrock = []
g_pop = []


for i in range(len(temp_songs)):
    name = Song(temp_songs[i][0], temp_songs[i][1], temp_songs[i][2], temp_songs[i][3])
    
    object_songs.append(name)
    
print(object_songs)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
