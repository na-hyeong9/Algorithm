def solution(scoville, K):
   import heapq
   answer = 0
   heapq.heapify(scoville)
   
   while len(scoville) > 1 :
       i = heapq.heappop(scoville)
       j = heapq.heappop(scoville)
       if i < K:
           answer += 1
           mixedK = i + j * 2
           heapq.heappush(scoville, mixedK)
       else:
           return answer
           
   if scoville[0] > K:
       return answer
   else:
       return -1