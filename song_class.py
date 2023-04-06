# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:33:52 2023

@author: JCCarpenter
"""

from song_list import temp_songs




class Song:
    def __init__(self, name, #genre
                  bpm, hype, artist):
        
        #if type(genre) is str:                                        # verify Genre value
#            self._genre = genre
        #else:
         #   raise ValueError('Genre must be a string')
         
        
        if type(name) is str:                                          # verify BPM value
            self._name = name
        else:
            raise ValueError('Name must be a string')
            
        
        if type(bpm) is int:                                          # verify BPM value
            self._bpm = bpm
        else:
            raise ValueError('BPM must be an integer')
            
        if type(hype) is int:                                         # verify Hype value
            self._hype = hype
        else:
            raise ValueError('Hype must be an integer')
            
        if type(artist) is str:                                       # verify Artist value
            self._artist = artist
        else:
            raise ValueError('Artist must be a string')
            
            
            
    def __repr__(self):
        return str(self._bpm) +', ' + str(self._hype) + ', ' + self._artist # self._genre + '\n' +

        
        
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        