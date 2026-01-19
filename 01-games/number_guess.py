import random

# The computer picks a secret number
secret = random.randint(1, 10)
guess = 0

print("--- Welcome to the Guessing Game! ---")
print("I'm thinking of a number between 1 and 10.")

while guess != secret:
    guess = int(input("What is your guess? "))
    
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret}.")