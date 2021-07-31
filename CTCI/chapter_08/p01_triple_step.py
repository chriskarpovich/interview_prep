"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible
ways the child can run up the stairs.
"""

def triple_hop(num_steps):
    if num_steps == 0:
        return 1
    if num_steps < 0:
        return 0
    # only one way to take 1 step, unnecessary
    if num_steps == 1:
        return 1
    return triple_hop(num_steps-1) + triple_hop(num_steps-2) + triple_hop(num_steps-3)

def triple_hop_memo(num_steps):
    memo = [0] * num_steps 
    def helper(i, memo):
        if i == 0:
            return 1
        if i < 0:
            return 0
        j = i-1
        if memo[j] == 0:
            memo[j] = helper(i-1, memo) + helper(i-2, memo) + helper(i-3, memo)
        return memo[j]
    return helper(num_steps, memo)

def triple_hop_memo_bottom_up(num_steps):
    if num_steps == 0:
        return 0
    if num_steps == 1:
        return 1
    memo = [0] * (num_steps + 1)
    memo[0] = 1 # one way to take zero total steps
    if num_steps >= 1:
        memo[1] = 1 # one way to take one total steps
    if num_steps >= 2:
        memo[2] = 2 # two ways to take two total steps
    for i in range(3, num_steps + 1): # find num ways to get to sums of steps 1 to num_steps
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[num_steps]

    

if __name__ == "__main__":
    print(triple_hop(1))
    print(triple_hop(2))
    print(triple_hop(3))
    print(triple_hop(4))
    print(triple_hop(5))
    print(triple_hop(6))
    print('---')
    print(triple_hop_memo(1))
    print(triple_hop_memo(2))
    print(triple_hop_memo(3))
    print(triple_hop_memo(4))
    print(triple_hop_memo(5))
    print(triple_hop_memo(6))
    print('---')
    print(triple_hop_memo_bottom_up(1))
    print(triple_hop_memo_bottom_up(2))
    print(triple_hop_memo_bottom_up(3))
    print(triple_hop_memo_bottom_up(4))
    print(triple_hop_memo_bottom_up(5))
    print(triple_hop_memo_bottom_up(6))