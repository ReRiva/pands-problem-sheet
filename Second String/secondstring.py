#A program that print a phrase when every second letter is printed in reverse order.
print ('This program will print out every second character of your sentence in reverse order ')

#Asking for the phrase to the user and storing it as string
phrase = str(input('Please type a sentence '))

#Setting up the variable to store the reversed phrase and creating the index variable
reversePhrase= ""
index = len(phrase)

# Using while to create a loop using the index variable which is the lenght of the original phrase
while index > 0:
    reversePhrase += phrase[index - 1] #decreasing 1 from the index variable to store each item of the phrase backwards.
    index = index - 2 # Updating the index variable as we want every second letter to be printed
print (reversePhrase)
