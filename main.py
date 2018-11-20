# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:28:49 2018

@author: rahulm99
"""

import dataframe
import squats_resting
import peak_bounds
import count_phone_usage
import blue_light_effect
import stairs
import sound
import total_calories
import calories

FLAG = True
WEIGHT = float(input("Introduce your weight in Kg:"))

sound.sound_file()

print("\n\n-----------------------------------------------\n")
(X, Y, SQUATS, T1, T2, T3) = squats_resting.squats_and_resting(dataframe.ACC_Y,
                                                               dataframe.TIME)

#squads_rest_project2.squats_and_resting()
print("\nNumber of squats perfornmed:", len(SQUATS))
print("Squats time in seconds: ", T1)
print("Time resting in seconds after squats: ", T2)
print("Time resting in seconds after stairs: ", T3)


print("\n\n-----------------------------------------------\n")
BLUE_LIGHT_TIME = blue_light_effect.blue_light()
print("Light is low for %d seconds that means darkness around the mobile." %BLUE_LIGHT_TIME)
print("Turned ON the blue light filter for this duration.")
NO_STAIRS = stairs.find_stairs()
print("Number of stairs taken: ", NO_STAIRS)


print("\n\n-----------------------------------------------\n")
PHONE_TIMES, OCCURANCES = count_phone_usage.phone_usage(dataframe.PROXIMITY)

T_JUMPS_START = Y                           # Second rest period end
T_JUMPS_END = OCCURANCES[2]                # Time jumps end

PEAKS = peak_bounds.peak_bounds_funct(T_JUMPS_START, T_JUMPS_END,
                                      'ACC_RMS', 20.4)

print("Total number of jumps: {}".format(len(PEAKS)))
print("The user used the phone: {} times.".format(PHONE_TIMES))

CALORIES = total_calories.total_calories_calculation(WEIGHT, T1, T2, X,
                                                     Y, T_JUMPS_START, T_JUMPS_END)
print("You burned: %.2f Calories total during your exercise session\n" %(CALORIES))
if CALORIES < 200:
    print("If you want to burn more Calories, you need to exercise for a ",
          "longer time\n")
print("\n\n-----------------------------------------------\n")

while FLAG:
    print("Do you want to know the calories burned during the different ",
          "activities your preformed")
    while True:
        USER = input("YES (Y) or NOT (N): ")
        if USER.lower() not in ('y', 'n'):
            print('Not a valid choise, TRY AGAIN')
        else:
            break
    if USER == 'y':
        print("In this option you are able to look how many calories your ",
              "burned per Activity")
        M = input("Choose your activity: \n1)Squats \n2)Stairs \n3)Jumps\n")
        while M not in ('1', '2', '3'):
            print("You introduced a Wrong value *** Please Try Again***\n")
            M = input("Choose your activity: \n1)Squats \n2)Stairs \n3)Jumps\n")
        MET = calories.define_met(M)

        if M == '1':
            TIME = T1
        elif M == '2':
            TIME = (dataframe.TIME[Y] - dataframe.TIME[X])*0.001 - T2
        else:
            TIME = (dataframe.TIME[T_JUMPS_END] - dataframe.TIME[T_JUMPS_START])*0.001

        CALORIES = calories.calories_calculation(MET, WEIGHT, TIME)
        print("You burned: %.2f Calories\n" %CALORIES)
        if CALORIES < 200:
            print("If you want to burn more Calories, you need to exercise ",
                  "for a longer time\n")
    else:
        print("Have a good Day")
        FLAG = False
