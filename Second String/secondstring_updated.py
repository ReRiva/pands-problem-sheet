#A program that print a phrase when every second letter is printed in reverse order.
#Author : Renan Riva

print ('This program will print out every second character of your sentence in reverse order ')

#Asking for the phrase to the user and storing it as string
phrase = str(input('Please type a sentence '))

#Setting up the variable to store the reversed phrase
reversedPhrase= ""

reversedPhrase += phrase[::- 2] #Using negative indexes (Week 5) to add every second letter to the variable reversedPhrase .
print (reversedPhrase)
