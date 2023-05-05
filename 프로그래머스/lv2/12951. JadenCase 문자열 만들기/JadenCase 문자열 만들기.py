def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        s[i]=s[i].capitalize() # 첫 문자만 대문자로 출력 (영문자의 경우만)
    answer=' '.join(s)
    return answer