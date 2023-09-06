# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
#An empty line should be added at the end
"""
Nested Loop
    It allows "inner loop" to complete a block of code iterations, 
    before complete one iteration of "outer loop"
"""
print("Let's create a Rectangle!")
length = int(input("Enter length: "))
width = int(input("Enter width: "))
symbol = input("Enter symvol (eg X): ")

perimeter = (length+width)*2 # Perimeter
area = length*width # Area

for i in range(length):
    for j in range(width):
        print(symbol, end="")
    print("") # Blank line
    
print("") # Blank line
print("Perimeter is: " + str(perimeter)) # Print Perimeter
print("Area is: " + str(area)) # Print Area
