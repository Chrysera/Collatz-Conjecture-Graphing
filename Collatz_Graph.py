# -*- coding: utf-8 -*-

# import numpy and pandas and assign shorthands
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#variable to loop the program until user wants to stop
cont = True

#while loop that continues until cont is false
while cont == True:
    
    #user input assigned to val variable
    val = input("Enter a positive integer: ")
    val = int(val)

    #create lists to represent x and y respectivley and a count variable to keep 
    #track of # of times calulated
    steps = []
    hailstones = []
    count = 0

    #Collatz Conjecture
    #continues until val=1 starts by adding the original value and number of steps
    #to their respective lists
    while val != 1:
        hailstones.append(val)
        steps.append(count)
        count += 1
        
        if val % 2 == 0:
            val = val / 2
        else:
            val = 3*val+1
    
    #create the data frame to show the graph for the hailstone numbers and # of calulations
    df_conj = pd.DataFrame({'# of Calulations' : steps, 'Values' : hailstones})

    df_conj.plot('# of Calulations', 'Values', kind='line')
    
    #setting tick rate and range to avoid half intervals on the x-axis
    if count <= 20:
        x_axis_ticks = np.arange(0, (count+1), 2)
        plt.xticks(x_axis_ticks)
    elif count > 20 and count <= 50:
        x_axis_ticks = np.arange(0, (count+1), 5)
        plt.xticks(x_axis_ticks)
    else:
        x_axis_ticks = np.arange(0, (count+1), 10)
        plt.xticks(x_axis_ticks)
        
    #show the data frame
    plt.show()
    
    #Ask user if they want to continue
    ask = input('Continue? (Y/N): ')
    
    #set cont to false breaking the loop if user doesn't want to continue
    if ask == 'N':
        cont = False