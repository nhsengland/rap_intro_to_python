# Loops are a way we can easily repeat tasks in python
# There are two types: for and while


# While:
# A While loop will repeat itself until a certain condition is satisfied
# This can make them tricky, because if you're not careful they will never end!
# To cancel, use ctr+c
"""
count = 0
while count <= 5:
    count = count #+ 1
    print(count)
"""


# For:
# For loops are much for commonly used
# They are used for doing things a certain number of times
# This has iterated through the list of numbers included in the range 0-10 (this excludes 10)
# and printed something for each one.
"""
for i in range(0, 10):
    print(f"I have {i} ice creams!")
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
        print("I love cherries!")
    else:
        print(f"Bleh! I hate {fruit}!")
"""