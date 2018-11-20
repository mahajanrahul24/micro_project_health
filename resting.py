# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:57:05 2018

@author: anggyemmanuc
"""

def rest(search_in, start):
    """Calculate the time when the user start resting
        Inputs:
            search_in: datafield
            start: no. sample to start searching
        Return:
            acum2: sample number where resting starts  """
    acum = 0
    acum2 = 0
    for values in search_in:
        if acum2 > start:
            if -11 < values < -9:
                acum += 1
                if acum == 10:
                    break
            else:
                acum = 0
        acum2 += 1
    return acum2
