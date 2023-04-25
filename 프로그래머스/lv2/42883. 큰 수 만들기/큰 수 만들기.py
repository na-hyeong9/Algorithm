def solution(number, k):
    number = list(number)
    result = [number.pop(0)]
    for n in number:
        if result[-1] < n:
            while result and result[-1] < n and k>0:
                result.pop()
                k -= 1
            result.append(n)
        elif k == 0 or result[-1] >= n:
            result.append(n)
            
    if k : # k의 수가 제거 되지 않은 경우
        result = result[:-k]
    answer = ''.join(result)

    return answer