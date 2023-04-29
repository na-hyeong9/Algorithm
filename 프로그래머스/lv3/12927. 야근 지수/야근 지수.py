import heapq

def solution(n, works):
    answer = 0
    if sum(works) > n:
        heap= []
        for num in works:
            heapq.heappush(heap, (-num, num))
        
        count = 0
        while count != n:
            work = heapq.heappop(heap)[1] - 1
            heapq.heappush(heap, (-work, work))
            count += 1
        
        answer = sum([x[1]**2 for x in heap])
    return answer