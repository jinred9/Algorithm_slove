import math

def solution(fees, records):
    # answer는 계산된 주차요금 list
    answer = []
    basic_time, basic_fee, unit_time, unit_fee = fees
    # 자동차번호 초기화
    car_nums = []
    # 입력된 값을 matrix로 만들기
    records_matrix =[]
    for record in records:
        record = list(map(str, record.split(' ')))
        record[0] = int(record[0].split(':')[0]) * 60 + int(record[0].split(':')[1])
        records_matrix.append(record)

    # 자동차 번호 set으로 유일한 수 오름차순으로 정렬 : car_nums_only
    for record_info in records_matrix:
        car_nums.append(record_info[1])
    car_nums_only = sorted(set(car_nums))

    for car_num in car_nums_only:
        count_in = 0
        count = 0
        # 자동차 주차요금 초기화
        car_num_fee = 0
        # 자동차 출입 시간 초기화
        time_in = 0
        time_out = 0
        parking_time = 0
        for record_info_matrix in records_matrix:
            count += 1
            if car_num == record_info_matrix[1] and 'IN' == record_info_matrix[2] and count_in == 0:
                time_in = record_info_matrix[0]
                count_in = 1

            elif car_num == record_info_matrix[1] and 'OUT' == record_info_matrix[2] and count_in == 1:
                time_out = record_info_matrix[0]
                count_in = 0
                parking_time = time_out - time_in + parking_time

            if count_in == 1 and count == len(records_matrix):
                time_out = 23 * 60 + 59
                count_in = 0
                parking_time = time_out - time_in + parking_time
        if 0 < parking_time <= basic_time:
            car_num_fee += basic_fee
        else:
            car_num_fee += basic_fee + math.ceil((parking_time - basic_time) / unit_time) * unit_fee
        answer.append(car_num_fee)
    return answer












fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
# answer = [14600, 34400, 5000]

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))
# # answer = [0, 591]

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))
# # answer = [14841]
