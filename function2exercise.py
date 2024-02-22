import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)

def main():
    max_number = int(input("Enter the maximum number on the dice: "))

    roll = roll_dice(max_number)
    while roll != max_number:
        print("Dice roll:", roll)
        roll = roll_dice(max_number)

    print("Dice roll:", roll)
    print("Reached maximum number!")

if __name__ == "__main__":
    main()