def solution(a, b):
    answer = 0
    num1 = 2 * a * b
    a, b = str(a), str(b)
    num2 = int(a+b)
    
    if num1 == num2:
        answer = num2
    else:
        answer = max(num1, num2)
    return answer