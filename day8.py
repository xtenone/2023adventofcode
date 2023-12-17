import re

# v_input_file = "data_dag8_test.txt"
# v_input_file = "data_dag8_test2.txt"
v_input_file = "data_dag8.txt"

#======================================================================================
# part 1
#======================================================================================   

# # 1. load file
# v_filename = v_input_file
# print(f'1. loaded file')
# with open(v_filename, 'r') as file:
#     v_data_form_file = [line.strip() for line in file]

# # 2. seperate data
# # v_data = [[],[],[]]
# v_data = []
# print(f'2. seperate data')
# v_secuenceline = ''
# for v_i, v_line in enumerate(v_data_form_file):
#     if v_i == 0:
#         v_secuenceline = re.findall(r'[A-Z]',v_line)
#         continue
#     if v_i > 1:
#         v_temp1 = re.findall(r'[A-Z]+',v_line)
#         # v_data[0].append(v_temp1[0])
#         # v_data[1].append(v_temp1[1])
#         # v_data[2].append(v_temp1[2])
#         v_data.append(v_temp1)

# # print(v_secuenceline)
# # print(len(v_secuenceline))

     
# v_find = 'AAA'
# v_counter = 0
# v_counter_total = 0
# while v_find != 'ZZZ':
#     if v_counter>=len(v_secuenceline):
#         v_counter = 0
#     v_pos = v_secuenceline[v_counter]
#     for v_line in v_data:
#         if v_line[0]==v_find:
#             if v_pos == 'L':
#                 v_find=v_line[1]
#             if v_pos == 'R':
#                 v_find=v_line[2]
#             # print(f'v_pos: {v_pos}')
#             # print(f'found: {v_find}')
#             v_counter+=1
#             v_counter_total+=1
#             break
# v_counter+=1
# print(v_counter_total)

#======================================================================================
# part 2 - too sloww
#======================================================================================

# # 1. load file
# v_filename = v_input_file
# print(f'1. loaded file')
# with open(v_filename, 'r') as file:
#     v_data_form_file = [line.strip() for line in file]

# # 2. seperate data
# # v_data = [[],[],[]]
# v_data = []
# print(f'2. seperate data')
# v_secuenceline = ''
# for v_i, v_line in enumerate(v_data_form_file):
#     if v_i == 0:
#         v_secuenceline = re.findall(r'[A-Z]',v_line)
#         continue
#     if v_i > 1:
#         v_temp1 = re.findall(r'..[A-Z]\b',v_line)
#         # v_data[0].append(v_temp1[0])
#         # v_data[1].append(v_temp1[1])
#         # v_data[2].append(v_temp1[2])
#         v_data.append(v_temp1)

# v_find_multiple = []
# # print(v_data)
# for v_line in v_data:
#     if v_line[0][2] == 'Z':
#         v_find_multiple.append(v_line[0])

# def F_all_z(v_find_multiple):
#     for v_line in v_find_multiple:
#             if v_line[2]!='Z':
#                 return 1
#     return 0

# v_counter_to_z_array = [[],[],[],[],[],[]]
# def F_all_z_print(v_find_multiple, v_counter):
#     global v_counter_to_z_array
#     v_keep = 0
#     for v_i, v_line in enumerate(v_find_multiple):
#             if v_line[2]!='Z':
#                 v_counter_to_z_array[v_i].append(0)
#             if v_line[2]=='Z':
#                 v_keep = 1
#                 v_counter_to_z_array[v_i].append(v_counter)
#                 # print()
#                 # for v_temp in v_counter_to_z_array:
#                 #     print(v_temp)
#     if v_keep == 0:
#         for v_i, v_line in enumerate(v_counter_to_z_array):
#             v_counter_to_z_array[v_i] = v_counter_to_z_array[v_i][::-1]
#     if v_keep == 1:
#         print()
#         v_temp = []
#         for v_i, v_line in enumerate(v_counter_to_z_array):
#             v_temp.append(v_line[-1])
#         print(v_temp)
#     return 0

# v_counter = 0
# v_counter_total = 0
# v_pos = v_secuenceline[v_counter]
# v_start = 1
# while F_all_z(v_find_multiple) or v_start==1:
#     v_start = 0
#     # print(v_find_multiple)
#     if v_counter>=len(v_secuenceline):
#         v_counter = 0
#     v_pos = v_secuenceline[v_counter]
#     # print(v_pos)
#     for v_i, v_multi in enumerate(v_find_multiple):
#         v_find = v_multi
#         for v_line in v_data:
#             if v_line[0]==v_find:
#                 if v_pos == 'L':
#                     v_find=v_line[1]
#                 if v_pos == 'R':
#                     v_find=v_line[2]
#                 # print(f'v_pos: {v_pos}')
#                 # print(f'found: {v_find}')
#                 v_find_multiple[v_i]=v_find
#                 break
#     v_counter+=1
#     v_counter_total+=1
#     # print(v_counter_total) 
#     F_all_z_print(v_find_multiple,v_counter_total)


#     # print(v_find_multiple)
#     # print(v_counter_total)
# print(v_counter_total) #37118/169247 too low

#======================================================================================
# part 2 - try 2
#======================================================================================
# so its quite far away in steps. need  beetter aproach
# going to calculate it on forehand
# so the file:
#---
# LR
# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
#---
# will become:
# 11A = 11B, 11Z
# 11B = XXX, XXX
# 11Z = 11B, 11Z
# 22A = 22B, 22C
# 22B = 22C, 22Z
# 22C = 22Z, 22B
# 22Z = 22B, 22C
# XXX = XXX, XXX
#---
# the are all the worked out options from the beginning
# make it into:
# beginning, end = 0 for no Z and 1 for Z
# --- 
# 11A, 11Z = 0, 1
# 11B, XXX = 0, 0
# 11Z, 11Z = 0, 1
# 22A, 22C = 0, 0
# 22B, 22Z = 0, 1
# 22C, 22B = 1, 0
# 22Z, 22C = 0, 0
# XXX, XXX = 0, 0
# ---
# every loop sum lines if 2 (in this example because 2 A's) then solution found
# every loop gives counter +2, answer is (position of the 6+2*loops)
# think this should be about 270 times faster

# # 1. load file
# v_filename = v_input_file
# print(f'1. loaded file')
# with open(v_filename, 'r') as file:
#     v_data_form_file = [line.strip() for line in file]

# # 2. seperate data
# # v_data = [[],[],[]]
# v_data = []
# print(f'2. seperate data')
# v_secuenceline = ''
# for v_i, v_line in enumerate(v_data_form_file):
#     if v_i == 0:
#         v_secuenceline = re.findall(r'[A-Z]',v_line)
#         continue
#     if v_i > 1:
#         v_temp1 = re.findall(r'..[A-Z]\b',v_line)
#         # v_data[0].append(v_temp1[0])
#         # v_data[1].append(v_temp1[1])
#         # v_data[2].append(v_temp1[2])
#         v_data.append(v_temp1)

# # 3. 
# v_matrix_positions = []
# for v_line1 in v_data:
#     v_find = v_line1[0]
#     v_start = v_find
#     v_allsteps = []
#     for v_pos in v_secuenceline:
#         for v_line in v_data:
#             if v_line[0]==v_find:
#                 if v_pos == 'L':
#                     v_find=v_line[1]
#                     break
#                 if v_pos == 'R':
#                     v_find=v_line[2]
#                     break
#         v_allsteps.append(v_find)
#     v_end = v_find
#     v_matrix_positions.append([[v_start, v_end],v_allsteps])

# # for v_line in v_matrix_positions:
# #     print(v_line)

# # 4. 
# for v_i1, v_line in enumerate(v_matrix_positions):
#     for v_i2, v_position in enumerate(v_line[1]):
#         if v_position[2]=='Z':
#             v_matrix_positions[v_i1][1][v_i2]=1
#         else:
#             v_matrix_positions[v_i1][1][v_i2]=0

# # print(v_line)
# # for v_line in v_matrix_positions:
# #     print(v_line)

# # 5. make startopoint
# v_find_multiple = []
# for v_line in v_matrix_positions:
#     if v_line[0][0][2] == 'A':
#         v_find_multiple.append(v_line[0][0])

# print(v_find_multiple)

# # 6. 
# v_totalsum_expected = len(v_find_multiple)
# v_looperd = 1
# v_counter1 = -1
# v_counter2 = 0
# while v_looperd==1:
#     v_counter2 = 0
#     v_counter1+=1
#     v_sum_vectors = []
#     v_find_multiple_new = []
#     for v_i, v_start_pos in enumerate(v_find_multiple):
#         for v_pos_data in v_matrix_positions:
#             if v_pos_data[0][0]==v_start_pos:
#                 v_find_multiple_new.append(v_pos_data[0][1])
#                 v_sum_vectors.append(v_pos_data[1])
    
#     v_line_total = [0]*len(v_pos_data[1])
#     for v_line in v_sum_vectors:
#         v_line_total = [x + y for x, y in zip(v_line_total, v_line)]
#         # print(v_line_total)
    
    
#     # print(f'{v_line_total}  --  {v_counter1*len(v_pos_data[1])+v_counter2} A')

#     for v_summednumber in v_line_total:
#         v_counter2+=1
#         if v_summednumber > 2:
#             print(f'{v_line_total}  --  {v_counter1*len(v_pos_data[1])+v_counter2}')
#         if v_summednumber == v_totalsum_expected:
#             print(v_counter1*len(v_pos_data[1])+v_counter2) # 146971491 is too low, wouldnt tell about 641675209
#             v_looperd=0                                       
#             break

#     # # still to sloww. A random guess that the Z is always in the end. This will make it faster. 
#     # # But if Z is not in the end it will fail.
#     # v_line_total = 0   
#     # for v_line in v_sum_vectors:
#     #     v_line_total+=v_line[-1]
#     #     v_counter2=len(v_pos_data[1])
    
#     # if v_line_total > 2:
#     #     print(f'{v_counter1*len(v_pos_data[1])+v_counter2} -- {v_line_total}') 

#     # if v_line_total == v_totalsum_expected:
#     #     print(f'{v_counter1*len(v_pos_data[1])+v_counter2} -- {v_line_total}') 
#     #     v_looperd=0
#     #     break


    
#     # v_find_multiple = v_find_multiple_new

# #860981926
# 146971491
        
#======================================================================================
# part 2 - try 3
#======================================================================================
# so even a factor 270 wasnt fast enough. I think it was pretty fast and got till 1631837193 
# and still didnt find anything above 3. So no programming to solve this, Need math...
# dont want to now though... gives pain to the brain.. would have to apply patern recognition
# .. but not today... or maybe.. ok lets find if there is a patern...

# 1. load file
v_filename = v_input_file
print(f'1. loaded file')
with open(v_filename, 'r') as file:
    v_data_form_file = [line.strip() for line in file]

# 2. seperate data
# v_data = [[],[],[]]
v_data = []
print(f'2. seperate data')
v_secuenceline = ''
for v_i, v_line in enumerate(v_data_form_file):
    if v_i == 0:
        v_secuenceline = re.findall(r'[A-Z]',v_line)
        continue
    if v_i > 1:
        v_temp1 = re.findall(r'..[A-Z]\b',v_line)
        # v_data[0].append(v_temp1[0])
        # v_data[1].append(v_temp1[1])
        # v_data[2].append(v_temp1[2])
        v_data.append(v_temp1)

# 5. make startopoint
v_find_multiple = []
for v_line in v_data:
    if v_line[0][2] == 'A':
        v_find_multiple.append(v_line[0])

print(v_find_multiple)



def F_findpath(v_find):
    global v_secuenceline
    v_counter = 0
    v_counter_total = 0
    v_last = ''
    while v_find[2] != 'Z' or v_counter_total==0:
        if v_counter>=len(v_secuenceline):
            v_counter = 0
        v_pos = v_secuenceline[v_counter]
        for v_line in v_data:
            if v_line[0]==v_find:
                if v_pos == 'L':
                    v_find=v_line[1]
                if v_pos == 'R':
                    v_find=v_line[2]
                # print(f'v_pos: {v_pos}')
                # print(f'found: {v_find}')
                v_counter+=1
                v_counter_total+=1
                break
    v_counter+=1
    # print(v_counter_total)
    # print(v_last)
    return [v_find, v_counter_total]

# v_find = v_find_multiple[3]
# print(v_find)

for v_find in v_find_multiple:
    v_find1 = F_findpath(v_find)
    # print(v_find1[1])
    # v_find = v_last

    v_find2 = F_findpath(v_find1[0])
    print(v_find2[1])

# oke something weird is going on. THe loops from Z to Z are exactly as long as the loopst from A to Z... wtf?
# also the loops are all different. which is important, otherwise you would never escape.
# so there are loops, big ones, but loops, as one wants to escape this maze, well dying is probably for the best. even in
# mm's this amount of steps will result in a futile attempt to escape.. so there are loops, big ones, when they get together is what we are looking for
# I found this to be called the LCM and there are tools for it. https://www.calculatorsoup.com/calculators/math/lcm.php
# gives 15,299,095,336,639 ... 