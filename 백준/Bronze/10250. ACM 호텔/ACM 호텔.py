t = int(input())

for i in range(t):
    H, W, N = map(int, input().split())
    num = N//H + 1 # 호수
    floor = N % H # 층
    if N % H == 0:  # h의 배수이면,
        num = N//H
        floor = H
    print(f'{floor*100+num}')