# Python Question Practice

An interactive command-line application that collects common Python practice questions—covering numbers, strings, and patterns—into a single menu-driven dashboard.

## Features

The dashboard offers 30 practice exercises, grouped roughly as follows:

**Number Operations**
- Even or Odd
- Positive, Negative or Zero
- Find Largest of Two / Three Numbers
- Sum of Natural Numbers
- Multiplication Table
- Factorial (iterative)
- Count Digits
- Reverse a Number
- Prime Number Check

**String Operations**
- Count Characters (without `len()`)
- Count Vowels / Consonants (separately and together)
- Reverse a String
- Check Palindrome
- Count Words (without `split()`)
- Character Frequency (without `count()`)
- Remove Spaces
- Convert to Uppercase
- Count Uppercase, Lowercase, Digits and Spaces
- Find First / Last Character
- Print Each Character
- Print Characters with Position
- Remove Vowels
- Find Longest Word
- Count Occurrence of Each Vowel

**Patterns**
- Star Pattern
- Number Pattern

Each function favors basic loops and conditionals over built-in shortcuts (e.g. avoiding `max()`, `len()`, `split()`, `count()`, `replace()`) to reinforce fundamental logic.

## Project Structure

```
.
├── app.py         # Entry point — launches the dashboard
├── dashboard.py   # Main menu loop and routing logic
└── config.py      # All practice question implementations
```

### How it works

- `app.py` is the entry point. Running it calls `dashboard()` from `dashboard.py`.
- `dashboard.py` displays a numbered menu in a loop, prompts for input based on the selected question, and calls the matching function from `config.py`.
- `config.py` contains each exercise as a standalone function, with a docstring explaining what it does and any constraints (e.g. "loops only, no built-ins").

## Requirements

- Python 3.10+ (uses `match` / `case` statements)

## Usage

1. Make sure `app.py`, `dashboard.py`, and `config.py` are in the same directory.
2. Run the application:

   ```bash
   python app.py
   ```

3. Choose a question by number from the menu:

   ```
   =======================================================
                PYTHON QUESTION PRACTICE
   =======================================================
   1.  Even or Odd
   2.  Positive, Negative or Zero
   ...
   30. Number Pattern
   0.  Exit
   =======================================================
   Enter your choice:
   ```

4. Follow the prompts for that question. After each run, press Enter to return to the dashboard, or enter `0` to exit.

## Notes

- Input is not extensively validated — entering non-numeric text where a number is expected will raise an error.
- Menu choices outside 0–30 print an "Invalid choice" message and redisplay the menu.

## Possible Improvements

- Add input validation with friendly error messages instead of crashing on bad input.
- Add unit tests for each function in `config.py`.
- Group related questions into submenus as the list grows.
- Allow re-running the same question without returning to the main menu each time.
