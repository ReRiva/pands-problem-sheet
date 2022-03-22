# This program calculate the square root from numbers imputed by the user
# Author: Renan Riva


def squareRoot (number, error= 0.001):   #Setting up a function to calculate the square root.
    guessSqrRoot = (number * 0.5)         # Allocation the square root "guess" to se it in the Newton Method
    aproSqrRoot = ((guessSqrRoot + number)/ guessSqrRoot) *0.5
    diff = 99999                        # Allocating a value to diff to set it agains the variable error as base for the loop and to get the as close as possible to the square root
    while diff >= error :                # Looping until the difference is less the the variable error 
        guessSqrRoot = aproSqrRoot       # Applying the Newton method and allocating the aproximated square root to the guessSqrRoot variable until the difference between both 
        aproSqrRoot = guessSqrRoot - ((guessSqrRoot**2 - number) / (2 * guessSqrRoot))   # are equal or less than the error variable
        diff = abs(guessSqrRoot - aproSqrRoot)  # Calculating the differene between the guess and the aproximated square root and allocating the absolute value to diff variable
    return (aproSqrRoot)    # Returning the clossest value to the number square root using the Newton method

# Referrences https://www.youtube.com/watch?v=tUFzOLDuvaE


def readNumber(): # Creating a function to stop the user to enter any amount that is not a number and asking for input to the number that will be used to calculate the sqaure root as shown this week
    number = False
    while (number == False):
        try:
            number = float(input ('Please enter a number positive number to calculate its square root: '))
        except ValueError:
            print("That is not a number. Please enter a valid number (Positive number)")
    return number



number = readNumber() # Allocating the function to the vaariable number

print ("The square root of ","%.1f" %number, "is ", "%.1f" %squareRoot(number)) # printing and formating the results to one decimal 

