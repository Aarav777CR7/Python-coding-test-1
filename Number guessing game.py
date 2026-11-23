import random


secret_number = random.randint(1, 50)
attempts = 0


print("Guess the number between 1 and 50")
while attempts <= 5:
    guess = int(input("Enter your guess "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessing it in {attempts} attempts. ")

print(f"Game over! The secret number was {secret_number}.")