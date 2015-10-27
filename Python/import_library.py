# Importing libraries

import random

print(random.randint(1,100))

def roll_dice(number_of_dice):
    for x in range(0,number_of_dice):
        print(random.randint(1,6))

roll_dice(5)
