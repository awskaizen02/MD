import json
filename = 'userName.json'
name = ""

# Check for a history file
try:
    with open(filename, 'r') as r:
      name = json.load(r)

except FileNotFoundError:
    print("First-time login")

if name != "":
    print("Welcome Back," + name + "!")
else:
    name = input("Hello! Whats your name?")
    print("Welcome, " + name + "!")
try:    
    with open(filename, 'w') as f:
        f.write("saving user data")
except IOError:
    print("There was a problem writing to the history file.")
        