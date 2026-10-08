import random

w, l, t = 0, 0, 0

valid = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!!!")
print("Type 'rock', 'paper', 'scissors', or 'quit' to stop playing\n")

while True:
    p = input("Enter your choice: ").strip().lower()

    if p == 'quit':
        print("Thanks for playing!")
        break

    if p not in valid:
        print("Invalid choice. Please try again (rock, paper, or scissors)\n")
        continue

    comp = random.choice(valid)
    
    print(f"You chose: {p}")
    print(f"Computer chose: {comp}")

    # check who won
    if p == comp:
        print("It's a tie!\n")
        t += 1
    elif (p == 'rock' and comp == 'scissors') or (p == 'paper' and comp == 'rock') or (p == 'scissors' and comp == 'paper'):
        print("You win this round!\n")
        w += 1
    else:
        print("Computer wins this round!\n")
        l += 1

    print(f"Score -> Wins: {w} | Losses: {l} | Ties: {t}")
    print("-" * 35)