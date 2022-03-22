from datetime import datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Fryday", "Saturday", "Sunday"]

today = datetime.now() # Will assing the local date, time, etc from the time the program is executed. (https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday)
index = today.weekday() # Will assing to index the value of corresponding to the week day(From 0 to 6) I am using this as it matches the zero index instead of using 


# Printing the name of the day to use lists for week 5. If you only want to know if its weekday or not you can remove the weekdays variable from the program. 
if index <= 4:
    print ("Today is", weekdays[index],"Unfortunately today is a weekday.") 
else:
    print("Today is", weekdays[index], "It is the weekend, yay!") 