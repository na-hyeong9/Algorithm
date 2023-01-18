import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    i = int(sys.stdin.readline())
    if i == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print('0')
    else:        
        heapq.heappush(heap, i)