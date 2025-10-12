"""
Practical 04 - Cumulative  total income
"""


# Pseudocode

# 1. Ask the user for the number of months
# 2. Create an empty list called incomes
# 3. For each month in the range of number_of_months:
#       - Ask the user for the income for that month
#       - Append it to the incomes list
# 4. Print the income report
#       - Use a function print_report(incomes)
#       - Inside function:
#             - Create a running total
#             - Loop through incomes with enumerate starting from 1
#             - Print month number, income, and cumulative total formatted nicely


def main():
    """Get incomes and display income report."""
    number_of_months = int(input("How many months? "))

    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report showing monthly income and cumulative total."""
    print("\nIncome Report")
    print("-------------")

    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}  Total: ${total:10.2f}")


main()
