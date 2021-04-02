import random

# Functions to help with the rest of the app

# Generate 10 random numbers for the winning and losing team's score
def random_numbers():
    list = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(list)
    return list

