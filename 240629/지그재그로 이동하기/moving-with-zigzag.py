def zigzag_distance(A, B):
    distance = 0
    current_position = A
    step = 1
    
    while current_position != B:
        if current_position < B:
            distance += abs(B - current_position)
            break
        else:
            distance += step
            current_position += step
            step *= -2  # 방향을 바꾸기 위해 step에 -2를 곱합니다.
            
    return distance

# 입력 받기
A, B = map(int, input().split())

# 결과 출력
print(zigzag_distance(A, B))