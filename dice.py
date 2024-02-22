import random
num_dice = int(input("Enter the number of dice you want to roll: "))
dice_sum = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    dice_sum += roll

print("Sum of the dice rolls:", dice_sum)