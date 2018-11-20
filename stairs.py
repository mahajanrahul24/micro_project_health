    # -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:47:43 2018

@author: rahulm99
"""
import squats_resting as myfilter
import dataframe as df
import peak_bounds as peaks


def find_stairs():
    """
    find_stairs find the peak values above the threshold.
    return:
        number of stairs
    """
    (lower, upper, squats, time1, time2, time3) = myfilter.squats_and_resting(df.ACC_Y, df.TIME)
    return len(peaks.peak_bounds_funct(lower, upper, 'ACC_RMS', 15))
