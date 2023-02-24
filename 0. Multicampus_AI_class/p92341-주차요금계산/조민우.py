# 시간 계산
from datetime import datetime as dt
import math
def cal_time(IN_time, out_time):
    time1 = dt.strptime(f"{IN_time}", "%H:%M")
    time2 = dt.strptime(f"{out_time}","%H:%M")
    elapsed_time = time2 - time1
    second = elapsed_time.seconds
    minute = (second // 60)
    return minute
def cal_total_fee(par,total,num):
    if num not in total.keys():
        total[num] = par[num]
    else:
        total[num] = total[num] + par[num]
    return total
def solution(fees, records):
    answer = []
    # 기본 시간, 기본 요금 , 단위 시간, 단위 요금
    default_time = fees[0]
    default_fee = fees[1]
    over_time = fees[2]
    extra_fee = fees[3]
    # 주차장 이용 내역 3차원 리스트 저장
    park = [record.split() for record in records]
    # 주차한 차량 정보 정보 저장 dict
    key_list=[]
    parked = {}
    total_fee = {}
    for col in range(len(park)):
        car_num = park[col][1]
        key_list.append(car_num)
        if park[col][2] == 'IN':
            parked[car_num] = park[col][0]

        else:
            parked[car_num] = cal_time(parked[car_num], park[col][0])
            total_fee=cal_total_fee(parked,total_fee,car_num)
            del(parked[car_num])

    key_list = sorted(set(key_list))
    for key in parked.keys():
        parked[key] = cal_time(parked[key], "23:59")
        total_fee = cal_total_fee(parked, total_fee, key)
    for key in key_list:
        if total_fee[key] - default_time < 0:
            total_fee[key] = default_fee
        else:
            total_fee[key] = math.ceil((total_fee[key] - default_time)/over_time)* extra_fee + default_fee
    for i in key_list:
        answer.append(total_fee[i])
    return answer

# def solution(fees, records):
#     answer = []
#     # 기본 시간, 기본 요금 , 단위 시간, 단위 요금
#     default_time = fees[0]
#     default_fee = fees[1]
#     over_time = fees[2]
#     extra_fee = fees[3]
#     # 주차장 이용 내역 3차원 리스트 저장
#     park = [record.split() for record in records]
#     # 주차한 차량 정보 정보 저장 dict
#     parked = {}
#     time_dict = {}
#     for col in range(len(park)):
#         car_num = park[col][1]
#         if park[col][2] == 'IN':
#             parked[car_num] = park[col][0]
#         elif park[col][2] == 'OUT':
#             if car_num not in time_dict.keys():
#                 time_dict[car_num] = cal_time(parked[car_num], park[col][0])
#                 del(parked[car_num])
#             else:
#                 time_dict[car_num] = time_dict[car_num] + cal_time(parked[car_num], park[col][0])
#                 del(parked[car_num])
#     for keys in parked.keys():
#         if keys not in time_dict.keys():
#             parked[keys] = cal_time(parked[car_num], "23:59")
#             time_dict[keys] = parked[keys]
#         else:
#             time_dict[keys] = time_dict[keys] + cal_time(parked[keys], "23:59")
#     save_key = []
#     for key in time_dict.keys():
#         save_key.append(key)
#         if time_dict[key] - default_time < 0:
#             time_dict[key] = default_fee
#         else:
#             time_dict[key] = math.ceil((time_dict[key] - default_time)/over_time)* extra_fee + default_fee
#     for i in sorted(save_key):
#         answer.append(time_dict[i])
#     return answer

print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))