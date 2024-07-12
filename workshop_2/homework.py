# Programming is best learnt through doing!
# This is some homework to complete before the next session.
# Uncomment the code and replace the ???? with the correct piece of code to obtain the expected output
# Run it after you complete each exercise to make sure you got it correct


# Conditionals

# Expected Output: Good morning
time_of_day = "morning"
if time_of_day == "morning":
    print("Good morning!")



"""
# Expected Output: Relax at home
day = "Saturday"
if day == "Monday":
    print("Go to work")
elif ????:
    print("Relax at home")
"""


"""
# Expected Output: Have a sandwich
meal = "lunch"
if meal == "breakfast":
    print("Eat some cereal")
elif ?????:
    print("Have a sandwich")
else:
    print("Enjoy a nice dinner")
"""


"""
# Expected Output: You can enter the concert
age = 20
has_ticket = True
if (???? >= 18) and ???? == ????:
    print("You can enter the concert")
elif (???? >= 18) and ???? == ????:
    print("Please buy a ticket!")
????:
    print("You can't enter!")
"""

"""
# Expected Output: money_in_bank = 100, has_paid_rent = True
money_in_bank = 1000
has_paid_rent = False
rent_amount = 900
# We want to check if we have paid rent already, and if we have enough money to pay it
if ????(has_paid_rent) and ???? >= ????:
    money_in_bank = money_in_bank - rent_amount
    has_paid_rent = True

print(money_in_bank)
print(has_paid_rent)
"""


"""
# Fix the mistake:
a = 1
b = 2
if a + b == 3
    print("I love maths!")
"""


"""
# Fix the mistakes
name == Rachel
if name == Kyle
print I love baseball!
else name == Lilidh
print I love hockey
else
print I love sports!
"""


"""
# Using if/elif/else statements, update the clothing variable
# For swimming and diving, you will need a swimsuit
# For gymnastics, you will need a leotard
# For any other, you will need shorts

clothing = None
activity = "swimming"

# Replace this
# With your
# if/elif/else statements

# Try replacing the activity variable at the top, so you can check it your code is working as expected
print(f"For {activity}, I will need to wear {clothing}")
"""



# Loops
"""
# Expected Output: Print numbers 1-11
count = 0
while count ???? 10:
    count = count + ????
    print(count)
"""

"""
# Expected Output: Print numbers 1-5, breaking after 5..
count = 0
my_name = ????
while my_name == ????:
    count = count + 1
    print(count)
    if count == ????:
        ????
"""

"""
# Expected output: Print the sentence up to and including "I have 10 candies"
for i in range(1, ????):
    print(f"I have {i} candies!")
"""

"""
Expected Output: A sentence for each sport in the list
sports = ["Soccer", "Basketball", "Tennis", "Baseball", "Hockey"]
for ???? in sports:
    print(f"I like to play {????}!")
"""

"""
# Expected Output: 1 sentence for each vegetable
vegetables = ["potato", "carrot", "broccoli", "spinach"]
for vegetable in ????:
    if vegetable == "????":
        print("Carrots are my favorite!")
    else:
        print(f"I don't like {vegetable} that much.")
""" 


"""
# This is a nested loop, see if you can understand what it's doing
# Expected Output: Every combination of colours and clothing
colours = ["red", "blue", "green"]
clothing = ["shirt", "trousers", "hat"]

for colour in ???? :
    for item in ????:
        print(f"A {color} {item}")
"""

"""
# Expected Output: A total of 15
numbers = [1, 2, 3, 4, 5]
total = 0
for ???? in ???? :
    total = total + ????
print("The total is:", total)
"""

"""
# Expected Output: The longest word is: dragonfruit
words = ["apple", "banana", "cherry", "dragonfruit"]
longest = ""
for word in ???? :
    if len(word) > len(????):
        longest = ????
print("The longest word is:", longest)
"""

"""
# Expected Ouput: doubled_numbers is a list containing the doubled amount of the number in numbers.
# Syntax of append method: list.append(element)
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
for number in numbers:
    ????.append(???? * 2)

print(doubled_numbers)
"""



"""
# Fix the mistakes:
# Expected Output: A list of numbers from 0 - 10
for i in range(0, 10)
print i
"""

"""
# Task: FizzBuzz
# A classic learning to code challenge: For the numbers 1-15, recreate the game FizzBuzz
# Aim: Count up to 15
# Rules:
# If the number is divisible by 3, say Fizz
# If the number is divisible by 5, say Buzz
# If the number is divisible by 3 AND 5, say FizzBuzz
# Else, just say the number
# You will need to use a combination of loops, and conditional statements
# Tip: the % operator (modulus) will give you the remainder of a division
# 3 % 3 = 0 (3 divided by 3 would give no remainder)
# 31 % 5 = 1 (31 divided by 5 would give 1 as a remainder)
# If you're stuck, go to file "fizzbuzz_help.py" to see a suggested layout - you'll still need to fill it in!

# Write your code here
#
#
#
"""


# Make sure to add your changes to your branch and push them. If this is the first time you're pushing your branch you might need to tell git which remote branch you are pushing to, but it'll let you know the command to run.
# Use commands:
# git add .
# git commit -m "completed homework"
# git push

# Once you're done with that, here's some webpages to continuing revising these skills:
# Access Items on a list: https://www.w3schools.com/python/python_lists_access.asp
# Change items in List: https://www.w3schools.com/python/python_lists_change.asp
# Adding to Lists: https://www.w3schools.com/python/python_lists_add.asp
# Removing from Lists: https://www.w3schools.com/python/python_lists_remove.asp
# Loops + Lists: https://www.w3schools.com/python/python_lists_loop.asp
# Conditions: https://www.w3schools.com/python/python_conditions.asp
# While Loops: https://www.w3schools.com/python/python_while_loops.asp
# For Loops: https://www.w3schools.com/python/python_for_loops.asp
