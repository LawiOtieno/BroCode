# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
#An empty line should be added at the end
"""
For Loop
    It executes a block of code limited number of times, 
    as long as a certain condition is met
"""
# Print numbers in a range
for i in range(10):
    print(i) # Put (i+1) for print to start by 1, 2, 3,...
print("#"*10) # Separate lines of codes
print("") # Blank line

# Print numbers in a range with a step
for i in range(50,100,2): # Print even numbers, for even numbers (51,100,2) 
    print(i)
print("#"*10) # Separate lines of codes
print("") # Blank line

# Print string
for i in "Lawrence Otieno":
    print(i)
print("#"*10) # Separate lines of codes
print("") # Blank line

# Print countdown
import time # Import time module
for sec in range(30,0,-1):
    print(sec)
    time.sleep(1) # Allow timed countdown
print("Happy birthday Lawrence")
print("#"*10) # Separate lines of codes
print("") # Blank line
