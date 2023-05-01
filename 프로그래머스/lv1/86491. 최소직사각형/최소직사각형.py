def solution(sizes):  
    sizes = [sorted(size, reverse=True) for size in sizes] # sizes의 각 항목(size)을 내림차순으로 정렬
    
    widths = [size[0] for size in sizes] # 가로길이 리스트
    heights = [size[1] for size in sizes] # 세로길이 리스트
    
    width, height = max(widths), max(heights)
    
    return width * height