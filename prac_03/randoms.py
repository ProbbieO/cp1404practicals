"""
Random numbers
"""

import random


print(random.randint(5, 20))  # Line 1
print(random.randrange(3, 10, 2))  # Line 2
print(random.uniform(2.5, 5.5))  # Line 3


# 1. What could each line produce? one number (min/max values)
# 2. Could line 2 produce a 4?
# 3. What are smallest/largest possible uniform values?

# TODO: Write code to generate a random number between 1 and 100 inclusive
number = random.randint(1, 100)
print(f"Random number: {number}")
