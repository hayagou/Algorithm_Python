def solution(n):
    answer = 0
    s = str(n)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(0 , len(s)):
        answer += int(s[i])

    return answer

print(f"답은 {solution(123)}")