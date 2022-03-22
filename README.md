# pands-problem-sheet - Weekly Activities

This repository contains the weekly activities assigned during the week 2 to week 8 of the course.

 * ### Week 2

For week 2 a small program was created to calculate the BMI of a person. By reading user inputs the program calculates the BMI using the height(in centimetres)  and the weight ( in Kilograms) of the user using the following formula “weight/height**2” and outputting the result in Kg/m2.


* ### Week 3

For week 3 a small program was created to print out every second character of your sentence, provided by the user, in reverse order. This was achieve by setting a variable to receive the reverse result and setting it to the original phrase[::-2], getting every second letter from the end of the phrase.


* ### Week 4

For week 4 a small program was created to simulate the [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) using an integer provided by the user. Where any positive integer after run through certain arithmetic operations (if the integer is even it will be divided by 2 and and the integer is odd it will be multiplied by 3 and add 1) will eventually result in 1.
The program did that by checking a if the number was not 1 to begin with. If not then module of 2 was used to check if the number was even or odd to apply the corresponding arithmetic function and repeating that and printing the results until the result was equal to 1.

* ### Week 5
For week 5 a small program was created to show the user if today is a week day or a weekend. This was achieved by creating an array containing the name os the days of the week,  then using the function date time.now from date time module, to check the system date then assigning it to the today variable. And using the today variable with the weekday function with return a number from 0 to 6 which match Monday to Sunday and assigning it to the index variable. Finally creating a if statement that will print a message according to the index variable value 

* ### Week 6

For week 6 a small program was created to calculated the square root of a number provided by the user using the [Newton’s method](https://en.wikipedia.org/wiki/Newton%27s_method). That was achieved by creating two functions. One that apply the Newton method were we make a guess to the value of the square root of the number and passing it to the guessSqrRoot variable. Then using the Newton method function we calculate the approximate value of the square root, subtract it from our initial guess and return the absolute value of it. If this value is equal or bigger than our margin of error, this operation will loop until we get the most approximate value for the square root of the number provided according with our margin of error.


 * ### Week 7

For week 7, small program was created to count the amount of letters “e” in a file provided by the user. The program used a function in the sys module (sys.argv) to make it possible to the user to import the document through the system command line. Both lower case and upper case “e’s were assigned to variables and these variables were used with the text.count function to count the amount of letters on the text. After that the amount of both upper and lower cases letter were printed (individually and added for a grand total) 

* ### Week 8
For week 8 a small program was created to produce a plot for the Functions: F(x)=x, G(x)=x2 and H(x)=x3, for X ranging from 0 to 4. Numpy module was used to with the functions linspace to generate every spaced ascending numbers between the range of X. Styles were applied to the plot such as line colour, line style, markers.


