# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:34:13 2018

@author: anggyemmanuc
"""

import resting
import peak_bounds


def squats_and_resting(acc_y, time):
    """Find the peaks and calculate the performing time for squats and resting
        Inputs:
            acc_y: Accelerometer axis-Y from database
            time: Recording time from database
        Return:
            end_of_break: point where the user stop resting
            end_of_break2: point where the user stop resting (second time)
            squats: peaks with the squats performed
            time_squats: time performing squats
            time_rest_1: time resting (first time)
            time_rest_2: time resting (second time)
            """
    rest_break = resting.rest(acc_y, 0)
    squats = peak_bounds.peak_bounds_funct(0, rest_break, 'ACCELEROMETER Y', (-1.5, 2))
    time_squats = (time[squats[len(squats)-1]]-time[squats[0]])/1000
    peak1 = peak_bounds.peak_bounds_funct(rest_break, len(acc_y), 'ACCELEROMETER Y', -8)
    end_of_break = peak1[0] + rest_break
    time_rest_1 = (time[end_of_break]-time[rest_break])/1000
    rest_break2 = resting.rest(acc_y, end_of_break)
    peak2 = peak_bounds.peak_bounds_funct(rest_break2, len(acc_y), 'ACCELEROMETER Y', -8)
    end_of_break2 = peak2[0] + rest_break2
    time_rest_2 = (time[end_of_break2]-time[rest_break2])/1000
    return (end_of_break, end_of_break2, squats, time_squats, time_rest_1, time_rest_2)
