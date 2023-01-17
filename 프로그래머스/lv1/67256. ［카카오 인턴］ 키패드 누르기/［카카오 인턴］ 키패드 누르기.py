def get_distance(keypad, finger_position, next_number):
    next_number_position = keypad[next_number]
    
    distance = abs(finger_position[0] - next_number_position[0]) + abs(finger_position[1] - next_number_position[1])
    
    return distance

def solution(numbers, hand):
    result = ''
    
    keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        0: [3, 1]
    }
    
    left_finger_numbers = [1, 4, 7]
    right_finger_numbers = [3, 6, 9]
    center_finger_numbers = [2, 5, 8, 0]
    
    left_finger_position = [3, 0]
    right_finger_position = [3, 2]
    
    for number in numbers:
        if number in left_finger_numbers:
            result += 'L'
            left_finger_position = keypad[number]
        elif number in right_finger_numbers:
            result += 'R'
            right_finger_position = keypad[number]
            
        else:
            left_finger_distance = get_distance(keypad, left_finger_position, number)
            right_finger_distance = get_distance(keypad, right_finger_position, number)
            
            if left_finger_distance > right_finger_distance:
                result += 'R'
                right_finger_position = keypad[number]
            elif left_finger_distance < right_finger_distance:
                result += 'L'
                left_finger_position = keypad[number]
            elif left_finger_distance == right_finger_distance:
                result += hand[0].upper()
                if hand == 'right':
                    right_finger_position = keypad[number]
                elif hand == 'left':
                    left_finger_position = keypad[number]      
        
    return result