# Take input from user

name = raw_input("What's your name? ")

if len(name) > 10:
    print("Your name is too long!")
else:
    print("Nice name!")
