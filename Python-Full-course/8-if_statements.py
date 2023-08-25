# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
#An empty line should be added at the end
'''
if - Statement
    A block of code that will be be executed if a particular condition is met
'''
age = int(input("What is your age? "))

if age == 100:
    print("You are a century old.")
elif age >= 18:
    print("You are an adult.")
elif age == 0:
    print("You are a new born child. Happy birthday!!!")
elif age < 0:
    print("Please enter valid age! Unborn don't live.")
else:
    print("You are a child.")
