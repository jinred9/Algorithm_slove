from collections import defaultdict


def to_min(hhmm: str):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def solution(fees, records):
    car_dict = defaultdict(int)
    used_time_dict = defaultdict(int)

    base_min, base_fee, per_min, per_fee = fees

    for record in records:
        hhmm, car_num, inout_type = record.split(" ")
        if inout_type == "IN":
            car_dict[car_num] = to_min(hhmm)
        else:
            start_min = car_dict[car_num]
            end_min = to_min(hhmm)

            used_time = end_min - start_min
            used_time_dict[car_num] += used_time
            del car_dict[car_num]

    for car_num, start_min in car_dict.items():
        used_time_dict[car_num] += to_min("23:59") - start_min

    answer = []
    for car_num, used_time in used_time_dict.items():
        v = (used_time - base_min) / per_min
        v = v // 1 + 1 if v % 1 > 0 else v // 1
        fee_time = 0 if used_time < base_min else int(v)
        answer.append((car_num, base_fee + fee_time * per_fee))

    return [f for _, f in sorted(answer)]


f1 =[180, 5000, 10, 600]
r1 = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result1 = [14600, 34400, 5000]
f2 = [120, 0, 60, 591]
r2 = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
result2 = [0, 591]
f3 = [1, 461, 1, 10]
r3 = ["00:00 1234 IN"]
result3 = [14841]


def sol(f, r, result):
    ret = solution(f, r)
    print("ret", ret, ret == result)

sol(f1, r1, result1)
