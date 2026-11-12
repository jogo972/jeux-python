import random

secret = random.randint(1, 100)   
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break
   
# Corrected syntax and error handling
user_input = input("guess the number between 1 and 100: ")

# Option 1: Check for empty string
if user_input.strip():
    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
else:
    print("Input cannot be empty.")   
import random 
