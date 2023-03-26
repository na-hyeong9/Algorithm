def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    cnt = 0
    total = 0
    
    while truck_weights:
        cnt += 1
        total -= q.pop(0)
        if truck_weights[0] + total <= weight:
            truck = truck_weights.pop(0)
            q.append(truck)
            total += truck
        else:
            q.append(0)  
        
    return cnt + bridge_length
