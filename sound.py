# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:45:41 2018

@author: marabetaniav
"""
import dataframe
import sound_t
import sound_l

def sound_file():
    """Sound function will let know the user if the area around him/her
    is ok or not for exercising"""
    flag = sound_l.sound_levels(dataframe.SOUND)
    cont = sound_t.sound_time(dataframe.SOUND)
    if flag == 1:
        print("After observing the data, You were expoused to a loud area")
        print("not good for your exercise during: %.2f seg\n"%(cont*0.1))
    if flag == 2:
        print("Analysing the sound around you, There is a quiet area for doing Yoga and meditation")
    if flag == 3:
        print("You were for: %.2f in a very loud area can cause you ear damage"%(cont*0.1))
        print("LEAVE THAT AREA")
        