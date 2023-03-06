from itertools import permutations


def solution(k, dungeons):
    max_count = 0

    for dungeon in permutations(dungeons):
        my_p = k
        count = 0
        for dungeon_idx in range(len(dungeon)):
            if dungeon[dungeon_idx][0] <= my_p:
                my_p -= dungeon[dungeon_idx][1]
                count += 1
        if max_count < count:
            max_count = count

    return max_count


solution(80, [[80,20],[50,40],[30,10]])


