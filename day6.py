# ok the tasks seem to be harder then expected. from experience from last task yesterday... 
# so lets solve this one in a clean way
# this seems to be an easy puzzle...
# d=((T-x)*x)=Tx-x² is the forula... wherer T=Time, x=Thold dont mind the units..
# so 0=x²-Tx+d.. 2nd order equation.. (x-½T)(x-½T)-¼T²+d=0.. x= +-sqr(¼T²-d)+½T²
# so the different options are x = +(sqr(¼T²-d)+½T²) - (-sqr(¼T²-d)+½T²)= 2*sqr(¼T²-d)

import re

# v_input_file = "data_dag6_test1.txt"
v_input_file = "data_dag6.txt"


# 1. load file
v_filename = v_input_file
print(f'1. loaded file')
with open(v_filename, 'r') as file:
    v_data_form_file = [line.strip() for line in file]

# 2. seperate data
v_times = []
v_distances = []
print(f'2. seperate data')
for v_i, v_line in enumerate(v_data_form_file):
    v_temp1 = re.split(r'[:]',v_line)
    v_temp2 = re.findall(r'[0-9]+',v_temp1[1].strip(' '))
    if v_i == 0:
        v_times = [int(element) for element in v_temp2]
    if v_i == 1:
        v_distances = [int(element) for element in v_temp2] #make int and put in array 


#==========================================================================================
# PART 2
#==========================================================================================
v_part2 = 1
if v_part2 == 1:
    v_new_time = ''
    v_new_distance = ''
    for v_i, v_line in enumerate(v_times):
        v_new_time = v_new_time + str(v_times[v_i])
        v_new_distance = v_new_distance + str(v_distances[v_i])

    v_new_time = int(v_new_time)
    v_new_distance = int(v_new_distance)

    v_times = [v_new_time]
    v_distances = [v_new_distance]
#==========================================================================================

print(v_times)
print(v_distances)

# 3. formula (x=2*sqr(¼T²-d))
print(f'3. calculate')
import math
v_ways = []
for v_i1, v_time in enumerate(v_times):

    # ok nice, but how to do this with integers? lets do it more stupid.
    # print(2*math.sqrt(v_time*v_time*0.25 - v_distances[v_i1] - 0.01))
    v_needtobebigger = 0.01 # equal times arent good enough. you need to be faster!! 1/100th milisecond faster is enough though..
    v_beattherecord = math.floor(math.sqrt(v_time*v_time*0.25 - v_distances[v_i1] - v_needtobebigger) + 0.25*v_time*v_time) - math.floor(-math.sqrt(v_time*v_time*0.25 - v_distances[v_i1] - v_needtobebigger) + 0.25*v_time*v_time)
    print(v_beattherecord)
    v_ways.append(v_beattherecord)

    # v_beattherecord = 0
    # for v_timecount in range(v_time): #d-(Tx-x²)
    #     v_disntance_compared = v_distances[v_i1]-(v_time*v_timecount-v_timecount*v_timecount)
    #     # print(v_disntance_compared)
    #     if v_disntance_compared < 0:
    #         v_beattherecord += 1
    # v_ways.append(v_beattherecord)

print(v_ways)

print(f'4. multiply for answer')
from functools import reduce
v_answer_part1 = reduce(lambda x, y: x * y, v_ways)
print(v_answer_part1) #
