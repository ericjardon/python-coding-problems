'''
Given a sorted array of coin denominations, and an amount m
return the minimum amount of coins needed to give remaining change
'''

# Again, reduces to computing every possible combination of taking or not taking the current denomination
# keeping track of the number of coins taken

# Brute Force, O(2^n) time complexity
def make_change(denoms, d, change):
    if d==0:
        # Guaranteed not to have remainder as denoms always contains 1
        return change//denoms[d]
    
    if change==0:
        # No change remaining, so we finish
        return 0
    
    if denoms[d] > change:
        # Current denom is more than we need, move to a smaller denom
        return make_change(denoms, d-1, change)

    use_current_denom = 1 + make_change(denoms, d, change - denoms[d])
    dont_use_current_denom = make_change(denoms, d-1, change)

    return min(use_current_denom, dont_use_current_denom)
    

# Make change but taking as many coins of denom possible

def make_change_faster(denoms, d, change):
    if d==0:
        return change//denoms[d]
    
    if change==0:
        return 0
    
    if denoms[d] > change:
        return make_change(denoms, d-1, change)
    
    coins_of_denom, remainder = divmod(change, denoms[d])
    take = coins_of_denom + make_change(denoms, d-1, remainder)
    not_take = make_change(denoms, d-1, change)

    return min(take, not_take)


def make_change_dp(denoms, d, change, memo=None):
    if memo is None:
        memo = {}

    # Subproblems are identified by the combination d and change remaining
    if (d, change) not in memo:
        # Calculate the result if not cached
        if d==0 and change > 0:  # not possible to make change
            memo[(d, change)] = float('inf')
        
        elif change==0:  # we're done
            return 0
        elif denoms[d] > change:  # pick a smaller denom
            memo[(d, change)] = make_change_dp(denoms, d-1, change, memo)
        else:
            coins_of_denom, remainder = divmod(change, denoms[d])
            take = coins_of_denom + make_change_dp(denoms, d-1, remainder, memo)
            not_take = make_change_dp(denoms, d-1, change, memo)

            memo[(d, change)] = min(take, not_take)
    return memo[(d, change)]


denoms = [.5,1,2,8,10,20,50,100,200,500]
change = 299
print("Denoms:", denoms)
print("Change: $" + str(change))

D = len(denoms) - 1
print("make_change:", make_change(denoms, D, change))  # takes a while
print("make_change_memo:", make_change_dp(denoms, D, change))  # returns almost instantly
