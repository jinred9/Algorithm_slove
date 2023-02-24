tc = int(input())
for i in range(1, tc+1):
    N, Q = input().split()
    box_list = ['0'] * N
    for q in range(0,int(Q)):
        L, R = input().split()
        for swap in range(int(L)-1,int(R)):
            box_list[swap] = q+1

    print('#{}'.format(i),' '.join(box_list))

