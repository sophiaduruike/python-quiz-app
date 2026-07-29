# Quiz App

A command-line Python quiz that asks questions and scores the user's answers.

## What it does
- Stores a set of questions and correct answers in a dictionary
- Loops through each question and asks the user to answer
- Checks the user's answer against the correct one — case-insensitive, so "abuja" and "Abuja" both count as correct
- Keeps a running score
- Prints the final score at the end

## What I learned
- Looping through a dictionary using `.items()` to access both questions and answers
- Comparing user input to a stored value correctly — an early bug had me comparing the question itself to the answer, instead of what the user actually typed
- Using `.lower()` on both sides of a comparison to make answer-checking case-insensitive
- Using functions and the `global` keyword to update a score from inside a function

## Tech
Python — dictionaries, functions, global scope, loops, string comparison
