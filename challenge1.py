def count_to_summit(n):
    assert n>=0
    if n==0 or n==1:
        return 1
    else:
        return count_to_summit(n-1)+count_to_summit(n-2)
print("Steps = 4")
print("answer: ",count_to_summit(4))
