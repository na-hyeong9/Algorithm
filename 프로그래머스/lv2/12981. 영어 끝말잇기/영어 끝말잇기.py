def solution(n, words):
    current_word = [words[0]]
    pre_word = words[0]
    for i in range(1,len(words)): 
        if pre_word[-1] != words[i][0]:
            return [(i % n)+1, (i//n)+1]
        elif words[i] in current_word:
            return [(i % n)+1, (i//n)+1]
        else:
            current_word.append(words[i])
            pre_word = words[i]
            
    return [0,0]