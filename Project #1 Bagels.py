# In Bagels, a deductive logic game, you must guess a secret 3-digit number based on clues.
# The game offers one of the following hints in response to your guess:
# "Pico" --> When your guess has one correct digit in the wrong place.
# "Fermi" --> When your guess has a correct digit in the right place.
# "Bagels" --> When your guess has no correct digits.
# You have 10 tries to guess the secret number.

import random

print("Welcome to the game Bagels! A deductive logic game.")
print()
print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I say: \t That means:")
print("   Pico \t One digit is correct but in the wrong place.")
print("   Fermi \t One digit is correct and in the correct place.")
print("   Bagels \t No digit is correct.")
print("I have thought of a number.")
print(" You have 10 guesses to get it correct!")

# Generating our Random Number
random_num = str(random.randint(100, 999))

# Setting and increment counter to control the While Loop
count = 1
# Using a While Loop to allow for attempts!
while count < 11:
    print(f"This is attempt number {count}:")
    user_num = input("Please guess a 3-digit number: ")

    # Getting the individual values for our Random Number
    random_num_first_val = random_num[0]
    random_num_sec_val = random_num[1]
    random_num_third_val = random_num[2]

    # Getting the inidividual values for the User Number
    user_num_first_val = user_num[0]
    user_num_sec_val = user_num[1]
    user_num_third_val = user_num[2]

    # These if conditions Determine whether, Fermi, Pico, or Bagels appears.
    if random_num_first_val == user_num_first_val:
        result1 = "Fermi"
    elif (user_num_first_val in random_num) and (random_num_first_val != user_num_first_val):
        result1 = "Pico"
    else:
        result1 = "Bagels"
    if random_num_sec_val == user_num_sec_val:
        result2 = "Fermi"
    elif (user_num_sec_val in random_num) and (random_num_sec_val != user_num_sec_val):
        result2 = "Pico"
    else:
        result2 = "Bagels"
    if random_num_third_val == user_num_third_val:
        result3 = "Fermi"
    elif (user_num_third_val in random_num) and (random_num_third_val != user_num_third_val):
        result3 = "Pico"
    else:
        result3 = "Bagels"

    # Seeing the output of our number results
    print(result1, result2, result3)
    # If the user guesses the correct number, then we want to end the loop
    if result1 == "Fermi" and result2 == "Fermi" and result3 == "Fermi":
        print("Great job! you guessed the correct number!")
        break
    # If the user does not guess the correct number, then we keep going!
    else:
        count = count + 1
