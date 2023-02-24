import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
   result = []
   N = int(input())
   numbers = list(map(int, input().split()))
   max_value = numbers[-1]
   result = 0
   temp = 0
   for i in range(N-1, -1, -1):
       if max_value > numbers[i]:
           temp = max_value - numbers[i]
           result += temp
       else:
           max_value = numbers[i]


   print(f'#{test_case} {result}')