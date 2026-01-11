import math

def koko(pile, k):
    left = 1
    right = max(pile)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total_hours = 0

        for banana in pile:
            total_hours += math.ceil(banana / mid)

        if total_hours <= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer



print("pile: [5,10,15,20]")
print("hours: 7")
print(koko([5,10,15,20],7))

