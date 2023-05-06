from itertools import product

def solution(word):
    w = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            w.append(''.join(list(c)))

    w.sort()
    return w.index(word) + 1