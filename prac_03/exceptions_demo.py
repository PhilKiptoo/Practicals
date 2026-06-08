"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError will occur when the input entered by the user cannot be successfully converted
   to an integer using the int() function (e.g., entering a decimal, letter, or empty string).
2. When will a ZeroDivisionError occur?
   A ZeroDivisionError will occur when the user enters 0 as the denominator, as division by zero
   is mathematically undefined in Python.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes, we can add a check or input validation loop to ensure the denominator is not zero before
   attempting the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
