import random

feet_in_mile = 5280
metres_in_km = 1000

beatles = ["John Lemon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1]

    # function tells the file extensions of the file 

def roll_dice(num):
    return random.randint(1, num)