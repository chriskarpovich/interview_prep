"""
Given an infinite number of quarters, dimes, nickels, and pennies, write code to calculate the number of ways to represent n cents.
"""

def coin_combinations(n_cents, choices=None):
    # base case, reached exactly 0 cents. add way to result
    if n_cents == 0:
        return 1
    # base case, overshot the result. don't add way to result since it's not valid
    if n_cents < 0:
        return 0
    if choices is None:
        choices = [1, 5, 10, 25]
    # base case, ran out of choices. return 0
    if len(choices) == 0:
        return 0

    m = len(choices)
    # first function call is the number of combinations without using a coin of this kind
    # second function call is the number of combinations with using a coin of this kind
    return coin_combinations(n_cents, choices[:m-1]) + coin_combinations(n_cents-choices[m-1], choices)

def coin_combinations_2(n_cents, choices=None, ind=0):
    if choices is None:
        choices = [25, 10, 5, 1]
    if ind >= len(choices) - 1:
        return 1

    amt = choices[ind]
    factor = 0
    ways = 0
    while factor * amt <= n_cents:
        amt_remaining = n_cents - factor * amt
        print(n_cents, ind)
        ways += coin_combinations_2(amt_remaining, choices, ind+1)
        factor += 1
    return ways



if __name__ == "__main__":
    print(coin_combinations(100))
    print(coin_combinations_2(100))