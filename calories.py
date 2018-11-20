# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:20:19 2018

@author: marabetaniav
"""

def define_met(m_user):
    """Function used to assign the MET for each activity preformed for the user """
    if m_user == '1':
        met = 3.5
        #print("You choose Squats as your activity")
    elif m_user == '2':
        met = 8
        #print("You choose Walking on Stairs as your activity")
    elif m_user == '3':
        met = 8.8
        #print("You choose Jumps as your activity")
    else:
        met = 0
        #print("Wrong activity")
    return met

def calories_calculation(met_u, weight, time):
    """Ecuation for calculate the Calories Burned for the user"""
    calories = (met_u * weight)*(time/3600)
    return calories
