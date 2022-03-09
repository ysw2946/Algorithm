import sys
import heapq

n = int(sys.stdin.readline())
heap=[]

for i in range(n):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap:
            min = heapq.heappop(heap)
            print(min)
        else:
            print(0)
    else:
        heapq.heappush(heap,n)