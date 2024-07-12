# Here we'll learn about if/elif/else statements.
# These can help us only execute certain lines of code if other conditions are met.
# Let's create a weather variable, and an if statement, that'll only execute if the weather variable is
# equal to a given value
# It's using the comparison operator, so it's really saying: if True -> do something!


weather = "Rainy"
if weather == "sunny":
    print("The sun is shining!")



# Indentatation is really important in python, it groups lines of code together.
# Here, we update our weather variable. The code inside the if statement won't run, but code out of it will!

weather = "rainy"
if weather == "sunny":
    print("It's so sunny!")
    print("I love the sun!")


# Sometimes, if a certain condition isn't met, you want to execute a different piece of code. 
# There, we would use an else block, after the if block.
# If the if block evaluate to False, the the code inside the else block will run.

weather = "rainy"
if weather == "sunny":
    print("Let's go to the beach!")
else:
    print("No beach today :(")


# We might also want to execute several different lines of code based on several different conditions.
# We use elif (short for else if) to do this. It comes after if, before else, and you can have as many as you want
# else statements aren't necessary after an elif statement, but if statements are necessary before.

weather = "cloudy"
if weather == "sunny":
    print("Summer is here!")
elif weather == "rainy":
    print("Bring out the umbrellas")
elif weather == "snowy":
    print("Let's built a snowman")
else:
    print("What's the weather?")


# We can combine if statements, comparison operators and logical operators all together!

a = 1
b = 3
weather = "cloudy"

# The brackets are optional, but I've added them here for clarity
if (a + b == 4) and (b > a) and (weather == "cloudy"):
    print("Wow!")


if (a + b == 100) or ( weather == "sunny"):
    print("Zoinks!")
else:
    print("Amazing!")
