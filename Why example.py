import random
# play a dice game with 3 lives 6 wins the game
lives = 3
while lives:
    print("You have", lives, "lives left")
    # roll the dice
    dice = random.randint(1,6)
    print("you rolled a", dice)
    # check if you win
    if dice == 6:
        print("you win! ")
        break
    lives -= 1
else:
    print("\n\nYou Lose!\n\n")

print("Thank you for playing, Goodbye.")

