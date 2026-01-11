def koko(pile,k):
    max_speed=max(pile)

    for banana_per_hour in range(1,max_speed+1):
        total_speed=0
        for banana in pile:
            total_speed+= banana/banana_per_hour
        if total_speed<k:
           return banana_per_hour


print(koko([5,10,15,20],7))

