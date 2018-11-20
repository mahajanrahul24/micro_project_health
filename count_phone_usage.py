# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:48:48 2018

@author: andrease
"""

def phone_usage(prox):
    """ Identifies how many times the phone is being used based on proximity
        sensor """
    counter = 0
    occurances = []
    times = 0
    while True:
        if counter < len(prox)-1:
            if prox[counter] == 1 and prox[counter+1] == 0:
                occurances.append(counter)
                times += 1
            counter += 1
        else:
            break
    # Substract the first one because it is the initial placement of the mobile
    return times-1, occurances
