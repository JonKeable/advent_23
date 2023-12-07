import re
import math

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


# d = vt
# t = max_t - but_time
# v = but_time
# => d = but_time * (max_t - but_time)
# or d = (max_t * but_time) -(but_time^2)
# graph 'n' shaped /\ as -x^2
# we want to find the section of the graph above a given d (our y) and where but_time is >0 and <max_t
# so we want to find x for a given d
# 0 = -b^2 + mb - d 
#m = max_t, b = but_time, d = distance
# x = -b +|- sqrt(b^2 - 4ac) / 2a

# expected ans for input: 28973936
# 

# derivative where max_t is const
# 1 - 2*but_time

def solve_quad(a, b, c):
    assert a != 0
    disc = (b**2) - (4*a*c)
    sqrt_disc = disc**0.5
    s1 = (-b + sqrt_disc) / 2*a
    s2 = (-b - sqrt_disc) / 2*a
    return(s1, s2)


def distance(t_max, b_time):
    return b_time * (t_max - b_time)

       


record = data_dict['Distance']
time = data_dict['Time']
new_records = 0

limits = solve_quad(-1, time, -record)
print(limits)
new_records =math.floor(max(limits)) - math.floor(min(limits))
print(new_records)

#print(f'time: {time}; new records: {new_records}' )



