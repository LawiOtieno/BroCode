# The first line in Python code 👉🏼 #!/usr/bin/python

# Second line 👆🏼 should be blank
#An empty line should be added at the end
'''
String Indexing/Slicing
    Creating a substring by extracting elements from another string
    indexing operator [] or slice()
    👉🏼 [start:stop:step], slice(start,stop)
'''

# 1 - Indexing
full_name = "Lawrence Otieno"
print(f"Characters length is {len(full_name)}")
# print(f"Get position of {full_name.index[e]}")
print() # Blank line, also print("")

first_name = full_name[0:8] # first_name = full_name[:8]
print(first_name)
print() # Blank line, also print("")

last_name = full_name[9:15] # last_name = full_name[9:] or first_name = full_name[-6:] # Count from last as -1
print(last_name)
print() # Blank line, also print("")

# Using step
s_name = full_name[::1] # Normal stepping - All characters are included hence no start and stop
print(s_name)
print() # Blank line, also print("")

x_name = full_name[::2] # Jumping one/next character - All characters are included hence no start and stop
print(x_name)
print() # Blank line, also print("")

rev_name = full_name[::-1] # Reverse full name - All characters are included hence no start and stop
print(rev_name)
print() # Blank line, also print("")

# 2 - Slicing
web1 = "http://streetgrandmaster.com"
web2 = "http://freecodecamp.org"
web3 = "http://python.org"
web4 = "http://google.com"

slice = slice(7,-4)

# Names in Title Case
print(web1[slice].capitalize())
print(web2[slice].capitalize())
print(web3[slice].capitalize())
print(web4[slice].capitalize())
