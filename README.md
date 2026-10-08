# Rock, Paper, Scissors Game

## Overview
This is a simple command-line Rock, Paper, Scissors game written in Python. The player chooses rock, paper, or scissors, and the computer randomly selects one of the three choices. The program determines the winner and keeps track of wins, losses, and ties.

## Features
- Interactive command-line gameplay
- Random computer choice using Python's `random` module
- Input validation
- Case-insensitive input
- Option to quit the game
- Score tracking for wins, losses, and ties
- Displays the player's and computer's choices after each valid round

## Requirements
- Python 3.x
- No external libraries are required

## How to Run
1. Save the program as `rock_paper_scissors.py`.
2. Open a terminal or command prompt in the folder containing the file.
3. Run:
   ```bash
   python rock_paper_scissors.py
   ```

## How to Play
Enter one of:
- `rock`
- `paper`
- `scissors`

Type `quit` to stop playing.

### Winning Rules
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Matching choices result in a tie

## Program Logic
1. Initialize the score counters for wins, losses, and ties.
2. Store the valid choices in a list.
3. Ask the player for a choice.
4. Convert the input to lowercase and remove extra spaces.
5. If the player enters `quit`, end the program.
6. If the input is invalid, display an error and ask again.
7. Randomly select the computer's choice.
8. Compare the two choices to determine the result.
9. Update the appropriate score counter.
10. Display the current score.
11. Repeat until the player chooses to quit.

## Example
```text
Welcome to Rock, Paper, Scissors!!!
Type 'rock', 'paper', 'scissors', or 'quit' to stop playing

Enter your choice: rock
You chose: rock
Computer chose: scissors
You win this round!

Score -> Wins: 1 | Losses: 0 | Ties: 0
-----------------------------------
```

## Concepts Used
- Variables
- Lists
- `while` loops
- `if`, `elif`, and `else` statements
- User input
- String methods
- The `random` module
- Counters
- Boolean/logical conditions

## Future Improvements
- Add a best-of-5 or best-of-10 game mode
- Add difficulty levels
- Add a graphical user interface
- Save scores to a file
- Add sound effects or animations
