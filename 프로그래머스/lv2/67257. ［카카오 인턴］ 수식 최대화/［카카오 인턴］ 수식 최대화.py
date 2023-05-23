from itertools import permutations

# 간단한 계산을 해주는 함수
def operator(a, b, p):
    if p == '*':
        return a * b
    if p == '+':
        return a + b
    return a - b
    
def cal(expression, o):
    
    # 연산자 분리하여 리스트로 저장
    tmp = []
    a = '' # 숫자 저장할 변수
    
    for ex in expression:
        if ex in o:
            tmp.append(int(a)) # 연산자가 나오기 전까지 a에 더해진 숫자를 리스트에 추가한다. str으로 입력되었기 때문에 int형으로 변환
            tmp.append(ex)
            a = ""
        else:
            a += ex
    tmp.append(int(a)) # for문을 나온 뒤 a에 남은 마지막 수를 추가로 tmp 완성
    
    for i in range(len(o)):
        stack=[]
        while tmp:
            t = tmp.pop(0)
            if t == o[i]:
                stack.append(operator(stack.pop(), tmp.pop(0), o[i])) # 연산 앞 뒤 숫자와 연산자를 계산한다. 
            else:
                stack.append(t)
        tmp = stack
        
    return int(stack[0])
    
def solution(expression):
    answer = 0
    # 연산자 조합
    li = ['+','-','*']
    operator = list(permutations(li, 3))
    
    # 연산자를 돌며 계산
    for o in operator:
        result = abs(cal(expression, o)) # 절대값
        answer = max(answer, result)
    return answer