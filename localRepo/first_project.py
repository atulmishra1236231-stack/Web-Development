import random

# Computer chooses randomly
computer = random.choice([-1, 0, 1])

# User input
user = int(input("Enter 1 for Snake, -1 for Water, 0 for Gun: "))

print("Computer choice:", computer)
print("Your choice:", user)

# Game logic
if user == computer:
    print("Game Draw")

elif user == 1 and computer == -1:
    print("You Win")

elif user == -1 and computer == 0:
    print("You Win")

elif user == 0 and computer == 1:
    print("You Win")

else:
    print("You Lose")