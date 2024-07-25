# Functions and Loops
#
# Let's put a few different things you have learned together. In this exercise you will:
#
# - Create a list of numbers
# - Create a function that returns the square of a number - but put it in workshop_3/src/maths/maths.py
# - Loop through your list of numbers and call the function to get the square of each number, and print it

# 1) First, open up the workshop_3/src/maths.py file, and create a function in there that returns the square of a number passed to it.
#    Don't forget your docstring! Come back here when you are done!


# 2) Now that you have created your function, you need to import the file that it's in. Do that below:
#from workshop_3.src import maths

def square(number):
    return number ** 2


# 3) Now define a list of numbers. They can be any numbers:
list_of_numbers = (1,2,3,4,5,6,7,8,9,10)


# 4) Finally, update the code below so that you loop through list_of_numbers, get the square of each one using your function, and then print it:
square_numbers = [square(num) for num in list_of_numbers]
print(square_numbers)