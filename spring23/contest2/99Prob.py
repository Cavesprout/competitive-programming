# Input: Price of a product (1 <= N <= 10^4)
# Goal: Find nearest positive integer which ends in 99
# If equal distance between numbers, find bigger one.

# Strategy: Seems extremely easy
# Get last two digits of num.
# Last two digits < 50 then set to 00 and subtract one to get answer
# Last two digits >= 50 then set to 99 to get answer.


price = input()

if (int(price) <= 99):
    # Special case: number too low to round down
    print("99")
else:
    end = price[-2:]

    res = -1

    if (int(end) < 49):
        res = int(price[:-2] + "00") - 1
    else:
        res = int(price[:-2] + "99")
    print(res)


# Stupid mistake = didn't test equal distance between numbers prior to first submission