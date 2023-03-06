def solution(fees, records):
    answer = []
    base_time, base_fee, add_time, add_fee = fees

    def cal_fee(res_min):
        if res_min - base_time > 0:
            up_time = (res_min - base_time)
            import math
            up_fee = math.ceil(up_time/add_time) * add_fee
        else:
            up_fee = 0
        return base_fee + up_fee

    car_num_dic = {}
    time_dic = {}

    for record in records:
        time, car_num, car_status = record.split()
        if not time_dic.get(car_num):
            time_dic[car_num] = 0
            car_num_dic[car_num] = False
        h, m = map(int, time.split(":"))
        if car_status == 'IN':
            time_dic[car_num] -= h * 60 + m
            car_num_dic[car_num] = True
        else:
            time_dic[car_num] += h * 60 + m
            car_num_dic[car_num] = False

    for car_num, status in car_num_dic.items():
        if status:
            time_dic[car_num] += 23 * 60 + 59
    for car in sorted(time_dic):
        fee = cal_fee(time_dic[car])
        answer.append(fee)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))