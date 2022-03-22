# A program that counts the amount of e's inside a document inputed by the user
# Author: Renan Riva

import sys

upperLetter = "e".upper() 
lowerLetter = "e"
        
with open(sys.argv[1], "r") as file:   # Opening a file as "file"(read mode) from the command line using argv from sys. Referrence(https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python)
        text = file.read()            # reading a file and storing its contents in a variable so I can use the coint function on it         
        totalUpperletters = text.count(upperLetter)  # Using Count to count Upper case "E" and storing it in a variable
        totalLowerletters = text.count(lowerLetter)  # Using Count to count lower case "e" and storing it in a variable
        totalLetters =  totalUpperletters + totalLowerletters #Adding up the lower and upper case letters as I decided to show both lower and upper case amount and also the total amount of "e" letters
        file.close() # Closing the file 


# Printing the amount of letters both lower and Upper case individually and the sum of both
print("The file has a total amount of {} ""E's""/""e's"". Divided into: \n{} ""E's"" and \n{} ""e's""".format(totalLetters, totalUpperletters, totalLowerletters)) 

