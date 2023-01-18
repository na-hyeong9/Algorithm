import heapq
import sys

heap=[]

n=int(sys.stdin.readline().strip())

for i in range(n) :
    inp=int(sys.stdin.readline())
    if inp!=0:
        heapq.heappush(heap,(-inp, inp))

    else : 
        if heap :    
            print(heapq.heappop(heap)[1])
        else :
            print(0)