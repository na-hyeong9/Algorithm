def solution(clothes):
    category = {}
    answer = 1
    
    for c in clothes:
        if c[1] in category.keys(): # category 딕셔너리에 같은 카테고리(key)가 있으면
            category[c[1]].append(c[0]) # 상품을 추가
        else:
            category[c[1]] = [c[0]] # 없으면 카테고리(key)와 상품(value)을 추가
             
    for v in category.values():
        answer *= len(v) + 1 # ex) headgear : green_turban, yellow_hat, '착용 안함' < 이 경우를 추가
    
    return answer - 1 # 아무것도 착용하지 않는 경우 제외