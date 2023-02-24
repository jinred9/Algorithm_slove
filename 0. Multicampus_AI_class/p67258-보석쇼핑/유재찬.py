from collections import defaultdict


def solution(gems):
    answer = [1, len(gems)]

    gem_set = set(gems)
    l, r = 0, 0

    gem_dict = defaultdict(int)  # k: gem, v: cnt

    gem_dict[gems[0]] = 1

    while l < len(gems) and r < len(gems):
        if len(gem_set) == len(gem_dict):
            if answer[1] - answer[0] > r - l:
                answer = [l + 1, r + 1]
            gem_dict[gems[l]] -= 1
            if gem_dict[gems[l]] == 0:
                del gem_dict[gems[l]]
            l += 1
        else:
            r += 1
            if r == len(gems):
                break
            gem_dict[gems[r]] += 1

    return answer


gems1 = ['DIA', 'RUBY', 'RUBY', 'DIA', 'DIA', 'EMERALD', 'SAPPHIRE', 'DIA']
r1 = [3, 7]
gems2 = ['AA', 'AB', 'AC', 'AA', 'AC']
r2 = [1, 3]
gems3 = ['XYZ', 'XYZ', 'XYZ']
r3 = [1, 3]
gems4 = ['ZZZ', 'YYY', 'NNNN', 'YYY', 'BBB']
r4 = [1, 5]


def sol(g, r):
    ret = solution(g)
    print("ret", ret, ret == r)


sol(gems1, r1)
