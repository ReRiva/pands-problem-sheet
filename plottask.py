# A program that display a plot for the Functions f(x)=x, g(x)=x2 and h(x)=x3
# Author: Renan Riva

import numpy as np                          #Importing numpy
import matplotlib.pyplot as plt                #importing matplotlib

minRange = 0                #Setting variables for minimun range 
maxRange = 4                # Setting variable for max range
numberOfEntries = 15      # Setting variable for the amount of items

xValue = np.linspace(minRange,maxRange, numberOfEntries) # Use Linspace to generate evenly spaced numbers between the range [0,4] so you can increase or decrease the amount of items you want to include in the plot (https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
fFunction = xValue            #Setting variables for each function according with what is asked in the exercise F(x)=X
gFunction = xValue**2          #Setting variables for each function according with what is asked in the exercise G(x)=X**2 
hFunction = xValue**3          #Setting variables for each function according with what is asked in the exercise H(x)=X**3

plt.style.use('seaborn-whitegrid')                                                                                      # Using one of the grid styles to change the plot 
plt.plot(xValue, fFunction, color="green", linestyle="dashed", marker="o", markerfacecolor="green",  label="F(x)= x")  # Changing the style of the color and style of the lines and add markers 
plt.plot(xValue, gFunction, color="red", linestyle="dashed", marker="o", markerfacecolor="red", label="G(x)= x**2")     # using the information on MATPLOT ref documentation https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(xValue, hFunction, color="blue",linestyle="dashed", marker="o", markerfacecolor="blue", label="H(x)= x**3")
plt.yticks(np.arange(0, 70, step=4))    # Changing the start and beggining of the grid ticks and setting the space between then to 4. Using np.arange to create a ord array as yticks takes arrays as paramenters (https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.yticks.html)
plt.legend()
plt.xlabel("Value of X")                #Adding label to x line
plt.ylabel("Function of X")             # Adding label to y line
plt.show()                                 #Dispalying the plot 
