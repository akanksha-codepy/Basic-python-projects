import random  # To allow the computer to make a random choice

# Dictionary mapping numbers to choices
n = {1: "Snake", 2: "Water", 3: "Gun"}

# Define the main game function
def game():
    # Computer randomly chooses one option
    computer = random.randint(1, 3)

    try:
        # Ask the user to choose Snake, Water, or Gun
        user = int(input('''Enter your choice: 
                        1: Snake
                        2: Water
                        3: Gun
                        Your choice: '''))

        # Decorative lines for visual separation
        for _ in range(4):
            print("\t\t\t\t\t|")

        # Show both the user's and computer's choice
        print(f"Computer chose: {n[computer]} \t\t\t\t\t You chose: {n[user]}")

        # Decorative lines again
        for _ in range(4):
            print("\t\t\t\t\t|")

        # Print result label
        print(" \t\t\t\t ", end="")

        # Determine the result
        if computer == user:
            print("IT'S A DRAW!")  # Both chose the same

        # Computer wins scenarios
        elif (computer == 1 and user == 2) or \
             (computer == 2 and user == 3) or \
             (computer == 3 and user == 1):
            print("YOU LOST!!")

        # User wins scenarios
        elif (user == 1 and computer == 2) or \
             (user == 2 and computer == 3) or \
             (user == 3 and computer == 1):
            print("YOU WON!!")

        else:
            print("Invalid Input.")  # If user enters a number not in [1, 2, 3]

    except (KeyError, ValueError):  # Handles invalid or non-integer input
        print("Invalid Input. Please enter 1, 2, or 3.")

    # Ask if the user wants to play again
    i = input("Do you want to play again (yes/no)? ").strip().lower()

    if i == "yes":
        game()  # Recursively call the game again
    elif i == "no":
        print("EXIT.")  # Exit the game
    else:
        print("Invalid choice. Exiting.")  # Handle unexpected input

# Start the game
game()
