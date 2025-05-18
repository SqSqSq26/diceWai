import random

def roll_dice():
    """Simulate rolling two dice and return their sum."""
    die1 = random.choice([1, 2, 3, 4, 5, 6])
    die2 = random.choice([1, 2, 3, 4, 5, 6])
    print(f"You rolled a {die1} and a {die2}.")
    return die1 + die2 

def dice_game():
    print("Welcome to the Dice Game!")
    print("You will roll two dice and add the results.")  

    while True:
        try:
            num_rolls = int(input("How many times would you like to roll the dice? "))
            if num_rolls <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")  

    for i in range(num_rolls):
        print(f"\nRoll #{i + 1}:")
        total = roll_dice()
        print(f"Total: {total}")

# Run the game
dice_game()