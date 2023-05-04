from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    max_cnt, cnt = len(queue1) * 3, 0

    while (queue1 and queue2) and max_cnt != cnt:
        if q1_sum == q2_sum:  # 두 큐 합이 같으면 종료
            return cnt
        elif q1_sum > q2_sum:  # queue1의 합이 더 크면 queue1에서 빼기
            temp = queue1.popleft()
            queue2.append(temp)
            q1_sum -= temp
            q2_sum += temp
        else:  # queue1의 합이 queue2보다 작을 때
            temp = queue2.popleft()
            queue1.append(temp)
            q1_sum += temp
            q2_sum -= temp
        cnt += 1
    return -1  # 두 큐 합이 같아지지 않으면 -1 반환