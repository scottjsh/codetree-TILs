def print_pattern(n):
    pattern = [
        "Hello",
        "#@#@#@#@#@",
        "CodeTree",
        "#@#@#@#@#@",
        "Students!"
    ]
    
    for i in range(n):
        if i > 0:
            print()  # 빈 줄 추가
            
        for line in pattern:
            print(line)

# 입력 받기
n = int(input())

# 함수 호출하여 패턴 출력
print_pattern(n)