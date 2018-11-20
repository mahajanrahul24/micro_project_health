# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:59:23 2018

@author: anggyemmanuc
"""

from scipy.signal import find_peaks
import dataframe

def peak_bounds_funct(lower_bound, upper_bound, column, threshold):
    """Calculate peak points within given range and threshold.
        Inputs:
            lower_bound: integer, starting of data to analize
            upper_bound: integer, ending of data to analize
            column: string, name of the column in the csv file
            threshold: integer, range in amplitud to analize
        Return:
            peak: list of peaks within the given range """
    filtered_data = dataframe.DATA_FIELD[column].iloc[lower_bound:upper_bound]
    peak, _ = find_peaks(filtered_data, height=threshold)
    return peak
