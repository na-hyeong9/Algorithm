def dfs(numbers, target, depth, value):
    if depth == len(numbers):
        if value == target:
            return 1
        else:
            return 0
    else:
        return dfs(numbers, target, depth+1, value+numbers[depth]) + dfs(numbers, target, depth+1, value-numbers[depth])

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer
