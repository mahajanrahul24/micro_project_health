# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:41:14 2018

@author: rahulm99
"""

import pandas as pd
import numpy as np

DATA_FIELD = pd.read_csv('Sensor_record_AndroSensor.csv')
#DATA_FIELD = pd.read_csv('Sensor_record_AndroSensor_Set_2.csv')

ACC_X = DATA_FIELD['ACCELEROMETER X']
ACC_Y = DATA_FIELD['ACCELEROMETER Y']
ACC_Z = DATA_FIELD['ACCELEROMETER Z']

LIGHT = DATA_FIELD['LIGHT']
PROXIMITY = DATA_FIELD['PROXIMITY (m)']
TIME = DATA_FIELD['Time']
SOUND = DATA_FIELD['SOUND LEVEL']


DATA_FIELD['ACC_RMS'] = np.sqrt(ACC_X **2 + ACC_Y ** 2 + ACC_Z **2)
ACC_RMS = DATA_FIELD['ACC_RMS']
