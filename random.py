# Importing the 'random' module to use random number generation functions
import random

# Display a welcome message to the user
print("Welcome to the Random Number Generator!")

# Ask the user to enter the lower bound of the random number range
# The input is converted from string to integer using int()
lower = int(input("Enter the lowest number in the range: "))

# Ask the user to enter the upper bound of the random number range
upper = int(input("Enter the highest number in the range: "))

# Generate a random integer between the lower and upper bounds (inclusive)
random_number = random.randint(lower, upper)

# Display the randomly generated number to the user
print("Here is your random number:", random_number)
