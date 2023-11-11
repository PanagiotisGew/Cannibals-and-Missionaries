Puzzle Solver(Cannibals and Missionaries)

Author: Panagiotis Georgiadis

This Python code is a puzzle solver that is designed to find a sequence of moves to reach a specific target state. The code uses a set of rules and logic to explore possible moves and generate a path to the target state.

Problem Description:

The problem involves a puzzle or game where you have a starting state and a target state. The objective is to find a sequence of valid moves that lead from the starting state to the target state while obeying specific rules.

In this particular code, the problem is described as follows:

You have a starting state start and a target state end.
The puzzle has a set of actions that can be applied to the current state.
The code explores different moves to find a path from the starting state to the target state.
The code also checks for safety conditions and ensures that the moves are valid.

Functions:
The code consists of the following key functions:

kane_kinisi(katastash, kinisi): This function calculates the next state based on the current state and a given move.

an_epitrepete(katastash): This function checks if the current state is within the puzzle's boundaries.

an_einai_asfales(bank): This function checks if a bank is safe according to certain conditions.

is_katastash_safe(katastash): This function checks if the current state is safe by examining both banks.

epomeni_dinati_kinisi(katastash): This function generates a list of possible valid moves from the current state.

solve(epomeni_kinisi, path): This recursive function explores possible moves and paths to reach the target state. It stores valid solutions in the solutions list.

How to Use:

To use this code to find solutions to a puzzle problem, you can follow these steps:

Modify the start and end variables to define your specific puzzle's starting and target states.

Customize the rules and actions for your puzzle by adjusting the actions list and the logic in the functions.

Run the code using a Python interpreter.

The code will generate and display possible solutions to reach the target state from the starting state.

Example
An example puzzle problem and solution can be found in the code. The code includes a sample puzzle problem with a specific set of rules and a target state.
 
