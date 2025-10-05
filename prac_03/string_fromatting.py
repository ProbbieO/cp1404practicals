"""
String formatting
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.999

# output f-string formatting output
print(f"{year} {name} for about ${cost:,.0f}!")

# print the powers of 2 in numbers 0-10
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:5}")
