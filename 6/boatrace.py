import re

f = open("input.txt", 'r')
line_list = [line.split() for line in f.read().splitlines()]

data_dict = {}
for line in line_list:
    dict_key = line.pop(0)[0:-1]
    data_dict.update({dict_key : [int(e) for e in line]})

time_dist_dict = {}
for i, time in enumerate(data_dict['Time']):
    time_dist_dict.update({time : data_dict['Distance'][i]})

print(data_dict)
print(time_dist_dict)

V_START = 0

# d = vt
def get_dist_for_button(time_pressed, max_time):
    return time_pressed*(max_time-time_pressed)

all_new_records = []
for time in data_dict['Time']:
    record = time_dist_dict[time]
    new_records = 0
    for press_time  in range(time+1):
        if get_dist_for_button(press_time, time) > record:
            new_records += 1
    print(f'time: {time}; new records: {new_records}' )
    all_new_records.append(new_records)

print(all_new_records)

prod = 1
for rec in all_new_records:
    prod*=rec

print(prod)

