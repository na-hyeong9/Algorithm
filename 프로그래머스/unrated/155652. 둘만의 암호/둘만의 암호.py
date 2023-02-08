def alphabet_list(skip):
    list = []
    for i in (range(ord('a'), ord('z')+1)):
        if not chr(i) in skip:
            list.append(chr(i))
        continue               
    return list

def solution(s, skip, index):
    result = []
    list = alphabet_list(skip)
    for al in s:
        pass_index = (index + list.index(al)) % len(list)        
        result.append(list[pass_index])
    answer = ''.join(result)
    return answer