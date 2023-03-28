def solution(numbers):
    num = list(map(str, numbers))
    num.sort(reverse=True, key=lambda x: x*3)
    answer = int(''.join(num))
    return str(answer)
