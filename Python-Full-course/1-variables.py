# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
# An empty line should be added at the end

# Variable 👉🏼 A container for a value.

#1 String data type (str)
print("###str###")
name = "Lawrence is a lazy coder."
print(name) #print variable
print(type(name)) #Print data type
print("Hello, " + name) #CONCATENATE - string variable with another string (String literal)
print("") # Blank line

#2 Integer data type (int)
print("###int###")
age = 29
age += 1 # Increment age by 1
print(age) #print variable
print(type(age)) #Print data type
print("Lawrence is " + str(age) + " years old.") #CONCATENATE - (integer must be converted to string)
print("") # Blank line

#3 Float data type () - Floating point number / a decimal number.
print("###float###")
weight_kg = 59.6
print(weight_kg) #print variable
print(type(weight_kg)) #Print data type
print("Lawrence weighs " + str(weight_kg) + " Kgs.") #CONCATENATE - (float must be converted to string)
print("") # Blank line

#4 Boolean data type (bool) - Stores True/False statements. Useful in if else statements. 
print("###bool###")
coder = True
no_coder = False
print(coder, no_coder) #print variables
print(type(coder)) #Print data type
print("Lawrence is coder? " + str(coder) + ". Thank you.") #CONCATENATE - (bool must be converted to string)
