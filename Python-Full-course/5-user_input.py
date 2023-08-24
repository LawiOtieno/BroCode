# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
#An empty line should be added at the end
'''
User Input
    Allow user to input data
'''
name = input("What is your first name? ") # Request and assign user input
age = int(input("How old are you now? "))
weight_kg = float(input("How heavy (Kgs) are you? "))

# Using type casting
print() # Blank line, also print("")
print(name.capitalize() + " is " +str(age)+ " years old, and weighs " +str(weight_kg)+ "Kgs.")

# Using f string
print(f"{name.capitalize()} is {age} years old, and weighs {weight_kg}Kgs.")
# 👉🏼 Run code in terminal by typing: python 5-user_input.py
