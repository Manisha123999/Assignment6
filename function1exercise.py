import  random

def roll_dice():
    return random.randint(1, 6)

def main():
    roll = roll_dice()
    while roll != 6:
        print("Dice roll:", roll)
        roll = roll_dice()

    print("Dice roll:", roll)
    print("Reached 6!")

if __name__ == "__main__":
    main()