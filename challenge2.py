def can_balance_scales(arr):
    total=sum(arr)
    if total %2!=0:
        return False
    else:

        target=total/2
        if target==0:
            return
        elif target<0:
            return False
        elif target!=0:

        else:
            include=can_balance_scales()



