import random  # For generating random numbers

count = 0  # To count number of guesses
i = random.randint(1, 101)  # Random number from 1 to 100

print("🎯 Welcome to the Number Guessing Game!")

while True:
    user = int(input("\nGuess the number between 1 to 100: "))  # User input
    print("\t\t\t", end="")

    if user > i:
        print("---- Lower Number please! ----")  # Guess is too high
        count += 1

    elif user < i:
        print("---- Higher number please! ----")  # Guess is too low
        count += 1

    elif user == i:
        print("---- The number is matched. ----")  # Correct guess
        print(f"\t\t\t--- The total no. of guess you take is : \"{count}\" ---")
        print("\t\t\t---- \"Thank you for playing.\" ----")
        break  # Exit the loop

    else:
        print("Invalid input")  # Not needed here, but added for safety

