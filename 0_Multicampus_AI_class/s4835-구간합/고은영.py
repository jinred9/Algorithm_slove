import sys
sys.stdin = open('input.txt')


T = int(input()) #테스트케이스 개수

for tc in range(1, T+1):
    N,M = map(int,input().split())
    array = list(map(int, input().split()))

    summation = 0 #초기값
    prefix_sum = [0] #접두사합 리스트
    max = 0

    for i in array:
        summation += i
        prefix_sum.append(summation)
    #print(prefix_sum)

    for num in range(1, N+1): #1부터 10까지
        left = num
        right = num + (M-1)
        if right <= N: #right의 최대가 len(array)
            inter_sum = prefix_sum[right] - prefix_sum[left - 1]
        else:
             if inter_sum > max:
                 max = inter_sum
                 print(f'#{tc} {max}')