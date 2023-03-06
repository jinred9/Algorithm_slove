from itertools import permutations

#필요피로도 # 소모 필요도

def solution(k, dungeons):
    result = []
    cnt =0
    def rc(idx,k):
        nonlocal result
        nonlocal cnt

        if idx >= 3:
            return cnt

        if i[idx][0] <= k:
            k -= i[idx][1]
            cnt += 1
            rc(idx + 1,k)



    for i in list(permutations(dungeons,3)):
        rc(0,80)
        result.append(cnt)
        if max(result) == 3:
            break
        cnt= 0
    print(max(result))



print(solution(80,[[80,20],[50,40],[30,10]]))