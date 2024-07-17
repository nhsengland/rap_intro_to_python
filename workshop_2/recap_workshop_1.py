# This file will recap workshop 1, and cover how to run python files
# The order to go through the files is:
#   1. recap_workshop_1.py
#   2. conditional_logic.py
#   3. loops.py
#   4. homework.py


# This is a python file - we can tell this becasue of the .py at the end of the file name
# Running this file:
# We can run this file from the terminal
# Double check your terminal is in the correct area using commands like:
# pwd - to check your present directory
# ls - to see the list of files available in your current directory
# cd {folder_name} - to change your current directory
#
# To run this file:
# python {path/to/file}
# 
# If you're in the root directory of this repository your path/to/file will include the folder that this file sits in
# So therefore you would run:
# python workshop_2/recap_workshop_1.py
#
# Tip: If you start typing a folder or file, and press the Tab button, it should finish it for you (as long as you 
# don't have more files with similar names)

# Try running this file now.




# Nothing happened?
# That's because there's nothing currently in this file being executed.
# Everything has a # symbol in front of it
# In Python, this is how you would stop code from running, and how you would "comment" your code
# Writing comments on your code is useful because it can explain to others (and future you!) what your code is doing
# and often more importantly, why.
# Try deleting the # symbol from that print statement below. Make sure there is no space at the start of it.

print("Hello World")

# Once you've deleted the # symbol, try running the file again (after saving!)
# Now, your code is being executed and Hello World will print to your terminal.
# Let's refresh the last workshop, but writing all the code in this file
# As we go through, uncomment the code so it'll run.



# Storing variables and printing
#a = 10
#b = 20
#a + b
#print(a + b)

# Notice that the sum of a + b only printed once to the terminal
# Unlike when we used python in the terminal, we explicitly have to print things when we're running from files.

# String Manipulation, casting, and F-strings:
# Remember that numbers and strings don't mix, so we have to force the number to be a string (casting)
# Replace the ???

#lucky_number = ????
#sentence = "My lucky number is " + str(lucky_number)
#print(sentence)

# But we don't have to do that when using f-strings!
#print(f"My lucky number is {lucky_number}")


# Comparison Operators:
a = 1
b = 2

# Using , we can also print two different datatypes: strings and Boolean
#print("a == b: ", a == b)
#print("a != b: ", a != b)
#print("a >= b: ", a >= b)
#print("a <= b: ", a <= b)

# Logical Operators:
# These were and, or and not
print("a == 1 and b == 2: ", a == 1 and b == 2)#True
print("a == 10 or b == 2: ", a == 10 or b == 2)#True
print("not b == 2: ", not b == 2)#False
