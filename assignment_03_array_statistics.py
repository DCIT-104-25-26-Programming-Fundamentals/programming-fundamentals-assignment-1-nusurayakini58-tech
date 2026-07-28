# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def single_table():
    """Displays the multiplication table for one number."""
    number = int(input("Enter a number: "))

    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


# -------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -------------------------------------------------------------------------
def tables_to_n():
    """Displays multiplication tables from 1 to N."""

    n = int(input("\nEnter a positive integer (N): "))

    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    for number in range(1, n + 1):
        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
        print("-" * 30)


# -------------------------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------------------------
single_table()
tables_to_n()