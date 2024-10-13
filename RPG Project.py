import random

def roll_dice():
    """Simulate rolling a six-sided dice."""
    return random.randint(1, 6)

def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest.")
    first_choice()

def first_choice():
    print("\nYou can go: ")
    print("1. Left (towards a river)")
    print("2. Right (towards a cave)")
    print("3. Roll a dice for luck")

    choice = input("Which way do you want to go? (1/2/3): ")

    if choice == '1':
        river()
    elif choice == '2':
        cave()
    elif choice == '3':
        dice_result = roll_dice()
        print(f"You rolled a {dice_result}!")
        if dice_result >= 4:
            print("You feel lucky! You decide to explore further.")
            first_choice()
        else:
            print("It's not your day. You should head back.")
            first_choice()
    else:
        print("Invalid choice. Try again.")
        first_choice()

def river():
    print("\nYou arrive at a calm river.")
    print("You can: ")
    print("1. Swim across")
    print("2. Go back")
    print("3. Roll a dice for luck")

    choice = input("What do you want to do? (1/2/3): ")

    if choice == '1':
        print("You swam across the river and found treasure! You win!")
    elif choice == '2':
        first_choice()
    elif choice == '3':
        dice_result = roll_dice()
        print(f"You rolled a {dice_result}!")
        if dice_result == 6:
            print("You found a hidden bridge! You can cross safely.")
            print("You win!")
        else:
            print("The current is strong! You fall back!")
            river()
    else:
        print("Invalid choice. Try again.")
        river()

def cave():
    print("\nYou enter a dark cave.")
    print("You can: ")
    print("1. Explore deeper")
    print("2. Go back")
    print("3. Roll a dice for luck")

    choice = input("What do you want to do? (1/2/3): ")

    if choice == '1':
        print("You encountered a dragon! Game over.")
    elif choice == '2':
        first_choice()
    elif choice == '3':
        dice_result = roll_dice()
        print(f"You rolled a {dice_result}!")
        if dice_result <= 2:
            print("You stumbled upon a treasure chest! You win!")
        else:
            print("You barely escape the cave! Go back to safety.")
            cave()
    else:
        print("Invalid choice. Try again.")
        cave()

if __name__ == "__main__":
    start_game()
