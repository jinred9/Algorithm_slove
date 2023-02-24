from collections import deque

def solution(ability, number):
    dq = deque(ability)
    print(dq)
    for _ in range(number):
        ability.sort(reverse=True)
        personA = ability.pop()
        personB = ability.pop()
        personA = personB = personA+personB
        ability.append(personA)
        ability.append(personB)

    return(sum(ability))






print(solution([10, 3, 7, 2], 2))
# print(solution([1, 2, 3, 4], 3))