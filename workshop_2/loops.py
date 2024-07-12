# Loops are a way we can easily repeat tasks in python
# There are two types: for and while


# While:
# A While loop will repeat itself until a certain condition is satisfied
# This can make them tricky, because if you're not careful they will never end!
# To cancel, use ctr+c

count = 74
while count <= 5:
    count = count #+ 1
    print(count)



# We can use break to make the loop stop. Otherwise, this loop would go on forever as the condition for it (1 + 1 == 2) is always True.

count = 0
while 1 + 1 == 2:
    count = count + 1
    print("count:", count)
    if count == 10:
        print("STOP!")
    break


# For:
# For loops are much more commonly used
# They are used to loop through an iterable
# This has iterated through the list of numbers included in the range 0-10 (this excludes 10)
# and printed something for each one.
"""
for number in range(0, 10):
    print(f"I have {number} ice creams!")
"""


# This is a list, it uses square brackets and each item is separated by a comma
# We frequently loop through lists in python
"""
languages = ["Python", "JavaScript", "R", "Ruby", "C++"]

for language in languages:
    print(f"I love to program in {language}!")
"""


# Combining loops and conditions:
"""
fruits = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]
for fruit in fruits:
    if fruit == "cherry":
        print(f"I love {fruit}!")
    else:
        print(f"Bleh! I hate {fruit}!")
"""


# Appending (adding to the end) on to lists
# Syntax: list_we_are_adding_to.append(item_we_are_adding)

numbers = [] # Empty list
for i in range(0, 11):
    numbers.append(i)
print(numbers)
numbers.append("Ready Player One")
print(numbers)

# % (Modulus) Operator - returns the remainder after a division
# We can use it to return only the even numbers (numbers which have no remainder after dividing by two)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
