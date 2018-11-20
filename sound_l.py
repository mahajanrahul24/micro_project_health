# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:26:45 2018

@author: marabetaniav
"""

def sound_levels(sound):
    """Sound_level function is used to analyse the colum SOUND in the DATASET"""
    flag = 0
    for i in sound:
        if 70 < i < 80:
            flag = 1
        if  30 < i < 40:
            flag = 2
        if i > 80:
            flag = 3
    return flag
