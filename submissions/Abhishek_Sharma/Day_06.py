# Function to handle the game scenario
def choose_path():
    choice = input("Which path do you choose? (left/right): ").lower()  # Get the user input and convert it to lowercase

    if choice == "left":
        print("You found a hidden tunnel! You're safe. 🚀")
    elif choice == "right":
        print("Oh no! The Glitch’s trap was here! Try again. 😨")
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")  # Handle invalid input

# Call the function to start the game
choose_path()
