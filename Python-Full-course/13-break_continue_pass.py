# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
#An empty line should be added at the end
"""
Loop Control Statements
    Change loop execution from it's normal sequence 
    break - Terminate loop
    continue - Skips to the next iteration of loop
    pass - Act as a placeholder, does nothing
"""
while True:
    name = input("Enter your first name: ")
    if name != "":
        break
        print("Hi " + name) # Code after break cannot be executed

print("#"*10) # Separate lines of codes
print("") # Blank line

my_phone = "254-708-581-688" # Only WhatsApp
for i in my_phone:
    if i == "-":
        continue
    print(i, end="") # end="" removes newline

print("") # Blank line
print("#"*10) # Separate lines of codes
print("") # Blank line

for i in ("Lawrence ", "Odhiambo", "Otieno"):
    if i == "Odhiambo":
        pass
    else:
        print(i + " ", end="") # end="" removes newline