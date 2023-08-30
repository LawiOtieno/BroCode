# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
# An empty line should be added at the end
"""
Logical Operators (and, or, not, ...)
    Used to check if two or more conditional statements are true
"""
temp = int(input("What is the temperature (*C) outside? "))
if temp >= 10 and temp <= 30:  # Both conditions must be true
    print("The temperature is good. \nYou can go outside.")
elif temp < 10 or temp > 30:  # One of the conditions must be true
    print("The temperature is bad. \nYou can't go outside.")
elif not(temp >= 10 and temp <= 30):  # Flips conditions from true to false, false to true
    print("The temperature is too bad! \nYou can't go outside.")
