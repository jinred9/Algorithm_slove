import math

def solution(fees, records):
    #누적 주차 시간 구해봅시다
    #dict로 데이터 가공
    car_record= []
    for record in records:
        time, car_number, in_out = record.split()
        car_record.append(car_number)

    new_record = {number:[] for number in car_record}
    total_time = {number:0 for number in car_record}


    for record in records:
        time, car_number, in_out = record.split()
        Time, Minute = map(int,time.split(':'))
        time = Time*60 + Minute
        new_record[car_number].append([time, in_out])

    # print(new_record)

    #각 차별로 돈 계산 스택 이용
    for k in new_record.keys():
        stack = []
        for record in new_record[k]:
            if record[1] == 'IN':
                stack.append(record)
            elif record[1] == 'OUT':
                past_in = stack.pop()
                accumul_time = record[0] - past_in[0]
                total_time[k] += accumul_time

        # print(total_time)
        if stack:
            left_car = stack.pop()
            accumul_time = (60*23+59) - left_car[0]
            total_time[k] += accumul_time

    #마지막 돈계산
    sorted_total_time= sorted(total_time)
    # print(sorted_total_time)
    pay = []

    for car_number in sorted_total_time:
        if total_time[car_number] <= fees[0]:
            pay.append(fees[1])
        else:
            pay.append(fees[1]+ math.ceil((total_time[car_number]-fees[0])/fees[2])*fees[3])

    return pay








print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                            "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT",
                            "22:59 5961 IN", "23:00 5961 OUT"]))

print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"] ))