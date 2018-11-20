# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:25:58 2018

@author: rahulm99
"""
import dataframe

def blue_light():
    '''
    Blue light effect function check the luminance around it.
    If surrounding is dark then it turns on the Blue Light effect.
    '''
    count = 0
    for i in range(0, len(dataframe.DATA_FIELD)):
        if  dataframe.DATA_FIELD.iloc[i]['LIGHT'] == 0:
            count += 1
    # Each interval is 100 msec.
    # Calculating Total duration in seconds.
    time_dur = (count*100)/1000
    return time_dur
