# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
# An empty line should be added at the end

# String Methods 👉🏼 Strings have methods, which represent common functionality...
# that has been implemented by Python developers, so we can use it in our programs directly.
name = "Lawrence"
print(len(name)) # General characters count, including spaces
print(name.count("e")) # Specific characters count, case sensitive
print(name.find("r")) # Location of character, case sensitive
print(name.capitalize()) # Write in Title Case
print(name.upper()) # Write in Upper Case
print(name.lower()) # Write in Lower Case
print(name.isalpha()) # Check if characters are alphabets, False - if space is present
print(name.isdigit()) # Check if characters are digits
print(name.replace("w", "u")) # Replacing one (first) character with another one (second)
