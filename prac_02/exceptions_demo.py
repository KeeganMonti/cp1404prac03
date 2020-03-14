"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When the user enters a letter instead of a number
2. When the user enters the denominator as zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print(" denominator Cannot be zero!")
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
    """
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
    """