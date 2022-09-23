T= int(input())

for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)
    QR = []
    for i in S:
        QR.append(i * R)
    print(''.join(QR))
