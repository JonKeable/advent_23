import re

f = open("input.txt", 'r')
line_list = [line.split() for line in f.read().splitlines()]

data_dict = {}
for line in line_list:
    dict_key = line.pop(0)[0:-1]
    full_time = ''
    for e in line:
        full_time += e
    data_dict.update({dict_key : int(full_time)})


print(data_dict)


# d = vt
def get_dist_for_button(time_pressed, max_time):
    return time_pressed*(max_time-time_pressed)


record = data_dict['Distance']
time = data_dict['Time']
new_records = 0
for press_time  in range(time+1):
    if get_dist_for_button(press_time, time) > record:
        new_records += 1

print(f'time: {time}; new records: {new_records}' )



