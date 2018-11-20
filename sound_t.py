# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:43:52 2018

@author: marabetaniav
"""

def sound_time(sound):
    """Sound_time is used to analysed the time on selected section of the SOUND"""
    cont = 0
    for i in sound:
        if  70 < i < 80:
            cont += 1
        if i > 80:
            cont += 1
    return cont
