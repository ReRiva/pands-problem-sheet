# A program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# #Author : Renan Riva

number = int(input(' Please enter a positive integer: '))
print ('{}'.format(number)) # Printing the number chosen by the user before starting the calculations


while number != 1: # Continue to repeat the code while the result is different than 1(Referrence week 4 Lecture)

    if (number % 2)==0: # If the number is even it will run the code below
        number = (number/2)
        print ('{:01.0F}'.format(number)) #Formating got from (https://stackoverflow.com/questions/32013276/python-integer-formatting) to match the formating in the exercise example
    else: # and if the number is not even it will run this code
        number = ((number*3)+1)
        print ('{:01.0F}'.format(number))

