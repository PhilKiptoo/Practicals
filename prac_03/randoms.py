"""
CP1404/CP5632 - Practical
Answers to random generation questions and code for 1-100 random number.
"""

import random

# Line 1: print(random.randint(5, 20))
# What did you see on line 1?
# It prints a random integer between 5 and 20 inclusive (e.g., 14).
# Smallest possible number: 5
# Largest possible number: 20

# Line 2: print(random.randrange(3, 10, 2))
# What did you see on line 2?
# It prints a random odd integer between 3 and 9 inclusive (from [3, 5, 7, 9]).
# Smallest possible number: 3
# Largest possible number: 9
# Could line 2 have produced a 4?
# No, because the step size is 2, starting from 3, so only 3, 5, 7, and 9 are possible.

# Line 3: print(random.uniform(2.5, 5.5))
# What did you see on line 3?
# It prints a random floating-point number between 2.5 and 5.5 inclusive.
# Smallest possible number: 2.5
# Largest possible number: 5.5

# Code to produce a random number between 1 and 100 inclusive:
print(random.randint(1, 100))
