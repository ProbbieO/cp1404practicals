"""
Capitalist and stock simulator
"""

import random

MAX_INCREASE = 0.1 # 10%
MAX_DECREASE = 0.05 # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "conrad.txt"

out_file = open(FILENAME, 'w')
price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}", file=out_file)
number_of_days = 0


while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a pric eof a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = -random.uniform(0, MAX_DECREASE)

    price *= (1 + price_change)
    number_of_days += 1
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()
