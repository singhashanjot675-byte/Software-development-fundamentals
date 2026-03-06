# Guessing Game

secret = 7
guess = -1
tries = 0
last_guess = None

while guess != secret:
    guess = int(input("Guess the secret number: "))

    if guess != last_guess:
        tries = tries + 1

    last_guess = guess

    if guess < secret:
        print("Too small")
    elif guess > secret:
        print("Too large")

print("Correct!")
print("Number of tries:", tries)