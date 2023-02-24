def solution(n):
    answer = 0
    number = 0
    for i in range(1, n + 1):
        if n % i == 0:
            number += i
            answer = number

    return answer