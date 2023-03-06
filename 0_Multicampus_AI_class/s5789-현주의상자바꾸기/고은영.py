import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
     N, Q = map(int,input().split())
     array = [0 for _ in range(N+1)]


     for i in range(1, Q+1):
          a,b = map(int,input().split())
          for j in range (a-1, b):
               #print(i)
               array[j] = i
     print(array)


