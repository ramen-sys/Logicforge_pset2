def count_payment_combinations(coins,total_sum):

    target = total_sum
    if target==0:
        return 1
    if target<0:
        return 0
    if not coins:
        return 0

    else:
        include=count_payment_combinations(coins,target-(coins[0]))
        exclude=count_payment_combinations(coins[1:],target)
        return include +exclude
print("[2,5,3,6] is coins")
print("10 is total sum")
print(count_payment_combinations([2,5,3,6],10))