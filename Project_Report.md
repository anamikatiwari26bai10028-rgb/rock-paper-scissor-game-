# PROJECT REPORT
## Rock, Paper, Scissors Game Using Python

### 1. Introduction
Rock, Paper, Scissors is a simple hand game played between two players. In this project, the player competes against the computer through a Python command-line application. The computer randomly chooses rock, paper, or scissors, while the player enters a choice using the keyboard.

The program compares both choices, determines the winner according to the standard rules, and maintains a running score.

### 2. Objectives
The main objectives of this project are:
- To create an interactive Python program.
- To understand and use conditional statements.
- To use loops for repeated gameplay.
- To generate random choices using Python's `random` module.
- To validate user input.
- To maintain and display game statistics.
- To practice basic programming problem-solving skills.

### 3. Technologies Used
| Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| `random` module | Generates the computer's random choice |
| Command Line / Terminal | User interface |

No external packages are required.

### 4. Game Rules
The program follows these rules:
- Rock defeats Scissors.
- Scissors defeats Paper.
- Paper defeats Rock.
- If both players select the same choice, the round is a tie.

### 5. Working of the Program

#### Step 1: Import the Random Module
The program begins by importing Python's built-in `random` module. This allows the computer to select a choice randomly.

```python
import random
```

#### Step 2: Initialize Scores
Three variables are created to store the number of wins, losses, and ties.

```python
w, l, t = 0, 0, 0
```

#### Step 3: Define Valid Choices
The possible choices are stored in a list.

```python
valid = ["rock", "paper", "scissors"]
```

#### Step 4: Display Instructions
The program welcomes the player and explains the available inputs.

#### Step 5: Accept User Input
The program repeatedly asks the player for a choice. The `strip()` method removes unnecessary spaces, while `lower()` makes the input case-insensitive.

```python
p = input("Enter your choice: ").strip().lower()
```

For example, ` Rock ` becomes `rock`.

#### Step 6: Handle Quit and Invalid Input
If the player enters `quit`, the loop ends. If the player enters anything other than rock, paper, or scissors, an error message is displayed and the player is asked again.

#### Step 7: Generate the Computer's Choice
The computer randomly selects one valid choice.

```python
comp = random.choice(valid)
```

#### Step 8: Determine the Winner
The program first checks whether both choices are equal. If they are equal, the result is a tie.

Otherwise, the program checks the winning combinations for the player:
- Rock vs. Scissors
- Paper vs. Rock
- Scissors vs. Paper

If none of these conditions is true, the computer wins.

#### Step 9: Update the Score
The appropriate counter is increased after every valid round:
- `w` for wins
- `l` for losses
- `t` for ties

#### Step 10: Display the Score
After each round, the program displays the current score and then starts another round.

### 6. Algorithm
1. Start the program.
2. Import the `random` module.
3. Set wins, losses, and ties to zero.
4. Create a list containing rock, paper, and scissors.
5. Display the game instructions.
6. Ask the player to enter a choice.
7. If the choice is `quit`, stop the program.
8. Check whether the choice is valid.
9. If invalid, display an error and return to Step 6.
10. Randomly select the computer's choice.
11. Compare the player's choice with the computer's choice.
12. If both choices are the same, increase the tie counter.
13. If the player has a winning combination, increase the win counter.
14. Otherwise, increase the loss counter.
15. Display the result and current score.
16. Repeat until the player chooses `quit`.
17. End the program.

### 7. Flow of the Program

```text
             START
               |
               v
       Initialize scores
               |
               v
       Display instructions
               |
               v
       Get player's choice
               |
        +------+------+
        |             |
      quit?          Valid?
        |             |
       Yes           No | Yes
        |              | 
        v              v
       END       Show error
                       |
                       +----> Ask again
                              |
                              v
                     Computer chooses
                              |
                              v
                       Compare choices
                              |
                 +------------+------------+
                 |            |            |
                Tie       Player wins   Computer wins
                 |            |            |
                 +------------+------------+
                              |
                              v
                       Update score
                              |
                              v
                       Display score
                              |
                              v
                       Ask again
```

### 8. Sample Output

```text
Welcome to Rock, Paper, Scissors!!!
Type 'rock', 'paper', 'scissors', or 'quit' to stop playing

Enter your choice: paper
You chose: paper
Computer chose: rock
You win this round!

Score -> Wins: 1 | Losses: 0 | Ties: 0
-----------------------------------

Enter your choice: scissors
You chose: scissors
Computer chose: scissors
It's a tie!

Score -> Wins: 1 | Losses: 0 | Ties: 1
-----------------------------------

Enter your choice: quit
Thanks for playing!
```

### 9. Advantages
- Simple and easy to understand.
- Provides immediate feedback to the player.
- Demonstrates important Python programming concepts.
- Uses randomness to make the computer's choice unpredictable.
- Validates user input.
- Keeps track of game performance.

### 10. Limitations
- The game is text-based and does not have a graphical interface.
- The score is not saved after the program closes.
- There is no multiplayer mode.
- There are no sound effects or animations.
- The computer does not use strategy; its choice is random.

### 11. Future Enhancements
The project can be improved by:
1. Adding a graphical user interface using Tkinter or another GUI framework.
2. Adding a best-of-3, best-of-5, or tournament mode.
3. Saving scores in a file or database.
4. Adding player names and a leaderboard.
5. Adding sound effects and animations.
6. Adding additional choices such as in Rock, Paper, Scissors, Lizard, Spock.
7. Adding difficulty levels or a computer strategy.

### 12. Conclusion
The Rock, Paper, Scissors project demonstrates how Python can be used to build a small interactive game. The project uses user input, lists, loops, conditional statements, counters, and random number generation.

The program successfully allows the player to play repeated rounds against the computer while tracking wins, losses, and ties. Overall, this project provides practical experience with fundamental Python programming concepts and can serve as a foundation for developing more advanced games and applications.

### 13. Learning Outcomes
After completing this project, the following concepts can be understood:
- How to use Python's `random` module.
- How to accept and process user input.
- How to validate input.
- How to use loops for repeated operations.
- How to apply conditional logic.
- How to maintain counters and display results.
- How to structure a simple command-line application.
