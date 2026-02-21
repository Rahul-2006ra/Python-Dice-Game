import random

# Function to roll dice
def roll_dice():
    return random.randint(1, 6)

# Function to display dice face
def display_dice(number):
    dice_faces = {
        1: ["|     |",
            "|  ●  |",
            "|     |"],

        2: ["| ●   |",
            "|     |",
            "|   ● |"],

        3: ["| ●   |",
            "|  ●  |",
            "|   ● |"],

        4: ["| ● ● |",
            "|     |",
            "| ● ● |"],

        5: ["| ● ● |",
            "|  ●  |",
            "| ● ● |"],

        6: ["| ● ● |",
            "| ● ● |",
            "| ● ● |"]
    }

    print("-------")
    for line in dice_faces[number]:
        print(line)
    print("-------")

# Main game function
def dice_game():
    roll_count = 0

    while True:
        print("\n🎲 DICE ROLLING GAME")
        print("1. Roll One Dice")
        print("2. Roll Two Dice")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                roll_count += 1
                dice = roll_dice()
                print("\nYou rolled:", dice)
                display_dice(dice)

            elif choice == 2:
                roll_count += 1
                dice1 = roll_dice()
                dice2 = roll_dice()
                print(f"\nYou rolled: {dice1} and {dice2}")
                display_dice(dice1)
                display_dice(dice2)

            elif choice == 3:
                print(f"\nTotal rolls: {roll_count}")
                print("Thanks for playing! 😊")
                break

            else:
                print("Please choose a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# Program execution starts here
dice_game()