import math  # 올림을 계산하는 math.ceil을 위해 라이브러리 추가


def solution(fees, records):
    d_time = fees[0]  # 기본 이용시간
    d_charge = fees[1]  # 기본 이용요금
    u_time = fees[2]  # 추가 이용시간 단위
    u_charge = fees[3]  # 추가 이용요금
    cars = [record.split() for record in records]  # 자동차들의 입출내역을 리스트로 저장
    park_cars = {}  # 주차되어있는 차량을 dict형태로 저장
    charges = {}  # 차량에 부과된 주차요금을 dict형태로 저장

    for n in range(len(cars)):
        car_name = cars[n][1]  # 차량번호를 car_name으로 저장
        if cars[n][2] == 'IN':  # 입차시
            park_cars[car_name] = cars[n][0]  # 차량 번호를 키값으로 차량의 입차시간 저장
            if car_name not in charges.keys():  # 주차요금 dict에 차량 번호가 없으면
                charges[car_name] = 0  # 주차요금을 0으로 초기화하여 추가한다

        if cars[n][2] == 'OUT':
            hour_out, minute_out = map(int, cars[n][0].split(':'))  # 출차 시간을 :을 기준으로 분리
            hour_in, minute_in = map(int, park_cars[car_name].split(':'))  # 입차 시간을 :을 기준으로 분리
            total = 60 * (hour_out - hour_in) + minute_out - minute_in  # 총 주차시간을 계산하여
            charges[car_name] += total  # 주차요금에 추가
            del park_cars[car_name]  # 주차된 차량 dict에서 제거

    for over_night in park_cars:  # 모든 입,출 기록을 계산 후 남아있는 차량계산
        hour_in, minute_in = map(int, park_cars[over_night].split(':'))  # 입차 시간을 :을 기준으로 분리
        total = 1439 - 60 * hour_in - minute_in  # 23:59의 분 환산값과 차이를 계산하여
        charges[over_night] += total  # 주차요금에 추가

    for charge in charges:  # 주차요금dict별로
        charges[charge] -= d_time  # 기본 이용시간만큼을 제외하고
        if charges[charge] > 0:  # 그보다 더 이용했으면
            # 남은 이용시간을 추가 이용시간 단위로 나눈것을 올림하여 추가 이용요금과 기본 이용요금을 더한다
            charges[charge] = math.ceil(charges[charge] / u_time) * u_charge + d_charge
        else:  # 아닌경우
            charges[charge] = d_charge  # 기본요금을 저장

    answer = []
    for car in sorted(charges):  # charges의 key값을 sort하여 for문 작성
        answer.append(charges[car])  # 주차요금을 정답리스트에 추가
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

# 실수로 입, 출차 마다 요금을 계산한 코드
# import math
#
#
# def solution(fees, records):
#     d_time = fees[0]
#     d_charge = fees[1]
#     u_time = fees[2]
#     u_charge = fees[3]
#     cars = [record.split() for record in records]
#     park_cars = {}
#     charges = {}
#
#     for n in range(len(cars)):
#         car_name = cars[n][1]
#         if cars[n][2] == 'IN':
#             park_cars[car_name] = cars[n][0]
#             if car_name not in charges.keys():
#                 charges[car_name] = 0
#
#         if cars[n][2] == 'OUT':
#             hour_out, minute_out = map(int, cars[n][0].split(':'))
#             hour_in, minute_in = map(int, park_cars[car_name].split(':'))
#             total = (hour_out - hour_in) * 60 + minute_out - minute_in
#             total -= d_time
#             charges[car_name] += d_charge
#             if total > 0:
#                 more = math.ceil(total / u_time)
#                 charges[car_name] += u_charge * more
#             del park_cars[car_name]
#
#     for over_night in park_cars:
#         hour_in, minute_in = map(int, park_cars[over_night].split(':'))
#         total = 1439 - 60 * hour_in - minute_in
#         total -= d_time
#         charges[over_night] += d_charge
#         if total > 0:
#             more = math.ceil(total / u_time)
#             charges[over_night] += u_charge * more
#
#     answer = []
#     for car in sorted(charges):
#         answer.append(charges[car])
#     return answer
