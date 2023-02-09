def solution(denum1, num1, denum2, num2):
    answer = []
    num = denum1*num2 + denum2*num1
    deno = num2*num1

    gcd = 0
    for j in range(min(num,deno), 0, -1):
        if num % j == 0 and deno % j ==0:
            gcd = j
            break
    
    answer = [num//gcd, deno//gcd]
    return answer