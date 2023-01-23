def solution(ingredient):
    answer = 0
    stack = []
    hamburger = [1, 2, 3, 1]
    
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if len(stack) >= 4:
            tmp = stack[-4:]
            if tmp == hamburger:
                answer += 1
                for j in range(4):
                    stack.pop(-1)
    
    return answer