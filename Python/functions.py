# Defining functions

# Make the even-odd program above into a function

def check_if_even(number):
    if number % 2 == 0:
        print("%s is even" % number)
    else:
        print("%s is odd" % number)

check_if_even(9)
check_if_even(34)
check_if_even(101)
check_if_even(1000000)
