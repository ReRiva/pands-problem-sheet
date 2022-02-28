# This Program calculates the BMI by reading user inputs
# Author: Renan Riva

# Asking for inputs and recording it in the variables.
# And setting the type of variables
# Referrence (https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792#:~:text=input%20%3D%20input('Do%20you,bmi%2C'which%20means%20you%20are)
weight = int(input('Please enter your weight in Kilograms '))
height = float(input('Please enter your height in Meters (Decimals) '))

# Calculating the BMI using the formula and saving it in the BMI variable...
bmi = weight / (height**2)

# Rouding the BMI Value and printing it.
#Referrence (https://blog.finxter.com/limit-floats-to-two-decimal-points-python/)
print('Your BMI is (Kg/m²)', round(bmi,2))
