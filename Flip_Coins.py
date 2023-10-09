import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def roll_die():
    return random.randint(1, 6)

def main():
    print("Welcome to the Coin Flip and Dice Roll Simulator!")
    choice = input("Choose 'C' for Coin Flip or 'D' for Dice Roll: ").strip().upper()
    
    if choice == 'C':
        num_coins = int(input("How many times do you want to flip the coin? "))
        for _ in range(num_coins):
            result = flip_coin()
            print(f"Coin flip: {result}")
    elif choice == 'D':
        num_dice = int(input("How many times do you want to roll the dice? "))
        for _ in range(num_dice):
            result = roll_die()
            print(f"Dice roll: {result}")
    else:
        print("Invalid choice. Please enter 'C' for Coin Flip or 'D' for Dice Roll.")

if __name__ == "__main__":
    main()
