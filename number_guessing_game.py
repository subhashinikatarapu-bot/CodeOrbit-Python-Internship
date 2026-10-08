import random

print("===== NUMBER GUESSING GAME =====")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI picked a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("Congratulations! You guessed the number.")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break