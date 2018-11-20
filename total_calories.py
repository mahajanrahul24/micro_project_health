# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:03:04 2018

@author: marabetaniav
"""
#LON_2 = LONGITUD[len(LONGITUD)-1]
import dataframe
import calories


def total_calories_calculation(weight, time1, time2, x_index, y_index, tstart, tend):
    """Calculation of total calories burned"""
    total_calories = 0
    for m_var in ('1', '2', '3'):
        if m_var == '1':
            time = time1
        elif m_var == '2':
            time = (dataframe.TIME[y_index] - dataframe.TIME[x_index])*0.001 - time2
        else:
            time = (dataframe.TIME[tend] - dataframe.TIME[tstart])*0.001
        met = calories.define_met(m_var)
        temp = calories.calories_calculation(met, weight, time)
        total_calories += temp
    return total_calories
