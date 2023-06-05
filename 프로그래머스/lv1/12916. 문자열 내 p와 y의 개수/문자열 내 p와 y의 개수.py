def solution(s):
    return True if s.count('p')+s.count('P')==s.count('y')+s.count('Y') or (s.count('p')+s.count('P') ==0 and s.count('y')+s.count('Y') == 0) else False
