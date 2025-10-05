"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when a number is input
2. When will a ZeroDivisionError occur?
when the user closes woth a division of 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?


"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

