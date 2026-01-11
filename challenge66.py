from collections import defaultdict
import heapq
def make_map(key,values):
    map = defaultdict(list)
    for deadline, profit in zip(key, values):
        map[deadline].append(profit)
    return map

def job(deadlines,profit):
    job_map=make_map(deadlines,profit)
    print(job_map)
    max_heap=[]
    max_deadline=max(deadlines)
    total_profit=0
    job_count=0
    for current_hour in range(max_deadline,0,-1):
        if current_hour in job_map:
            for profit in job_map[current_hour]:

                heapq.heappush(max_heap,-profit)
        if max_heap:
            best=-heapq.heappop(max_heap)
            total_profit+=best

            job_count+=1
    return job_count,total_profit

print(job([4,1,1,1],[20,10,40,30]))






