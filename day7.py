import re

# v_input_file = "data_dag7_test1.txt"
v_input_file = "data_dag7.txt"

#=======================================================================================================================
#part 1

# 1. load file
v_filename = v_input_file
print(f'1. loaded file')
with open(v_filename, 'r') as file:
    v_data_form_file = [line.strip() for line in file]

# 2. seperate data
v_data = []
print(f'2. seperate data')
for v_i, v_line in enumerate(v_data_form_file):
    v_temp1 = re.split(r'[ ]+',v_line)
    v_data.append(v_temp1)

# for v_i in v_data:
#     print(v_i)

# 3. improve data
print(f'3. improve data')
for v_i1, v_line in enumerate(v_data):
    v_newline = []
    for v_i in v_line[0]:
        v_append=v_i
        if v_i == 'T':
            v_append=10
        if v_i == 'J':
            v_append=11
        if v_i == 'Q':
            v_append=12
        if v_i == 'K':
            v_append=13
        if v_i == 'A':
            v_append=14
        v_newline.append(int(v_append))
    v_data[v_i1][0] = v_newline
    
# for v_i in v_data:
#     print(v_i)

# 4. add data point 'matches'
print(f'4. add data point matces')
for v_i1, v_line in enumerate(v_data):
    v_data[v_i1].append([0,0,0,0,0])
    for i_v2 in range(2,14+1): #[2-14]
        v_counter = 0
        for v_i in v_line[0]:
            if i_v2 == v_i:
                v_counter+=1
        if v_counter != 0:
            v_data[v_i1][2][v_counter-1]+=1

# for v_i in v_data:
#     print(v_i)

# 5. ordering
print(f'5. ordering')
v_data = sorted(v_data, key=lambda x: x[0])
v_data = sorted(v_data, key=lambda x: x[2][::-1])

# for v_i in v_data:
#     print(v_i)

# 6. counting
print(f'6. counting')
v_points = 0
for v_i1, v_line in enumerate(v_data):
    v_points += (v_i1+1)*int(v_line[1])

print(v_points)

#=======================================================================================================================
#part 2

# 1. load file
v_filename = v_input_file
print(f'1. loaded file')
with open(v_filename, 'r') as file:
    v_data_form_file = [line.strip() for line in file]

# 2. seperate data
v_data = []
print(f'2. seperate data')
for v_i, v_line in enumerate(v_data_form_file):
    v_temp1 = re.split(r'[ ]+',v_line)
    v_data.append(v_temp1)
    
# 3. improve data
print(f'3. improve data')
for v_i1, v_line in enumerate(v_data):
    v_newline = []
    for v_i in v_line[0]:
        v_append=v_i
        if v_i == 'T':
            v_append=10
        if v_i == 'J':
            v_append=1 #!!!!!!!!!! part2 adjustement
        if v_i == 'Q':
            v_append=12
        if v_i == 'K':
            v_append=13
        if v_i == 'A':
            v_append=14
        v_newline.append(int(v_append))
    v_data[v_i1][0] = v_newline
    
# for v_i in v_data:
#     print(v_i)

# 3.2 jokers
print(f'3.2. extra step, use jokers')
for v_i1, v_line in enumerate(v_data):
    v_temp1 = 0
    v_countermax = 0
    v_joker_to = 1
    for i_v2 in range(2,14+1): #[2-14]
        v_counter = 0
        for v_i in v_line[0]:
            if i_v2 == v_i:
                v_counter+=1
        if v_counter > v_countermax:
            v_countermax = v_counter
            v_joker_to=i_v2
    v_temp1 = v_line[0]
    v_data[v_i1].append(v_temp1.copy())
    for i_v2, v_d in enumerate(v_line[0]):
        if v_d == 1:
            v_data[v_i1][2][i_v2]=v_joker_to

# for v_i in v_data:
#     print(v_i)

# 4. add data point 'matches'
print(f'4. add data point matces')
for v_i1, v_line in enumerate(v_data):
    v_data[v_i1].append([0,0,0,0,0])
    for i_v2 in range(1,14+1): #[1-14]
        v_counter = 0
        for v_i in v_line[2]:
            if i_v2 == v_i:
                v_counter+=1
        if v_counter != 0:
            v_data[v_i1][3][v_counter-1]+=1

# for v_i in v_data:
#     print(v_i)

# 5. ordering
print(f'5. ordering')
v_data = sorted(v_data, key=lambda x: x[0])
v_data = sorted(v_data, key=lambda x: x[3][::-1])

for v_i in v_data:
    print(v_i)

# 6. counting
print(f'6. counting')
v_points = 0
for v_i1, v_line in enumerate(v_data):
    v_points += (v_i1+1)*int(v_line[1])

print(v_points) 
# 248140301 is too low.
# 248806028 to high
# its 248747492