import re
print()
v_input_file = "data_dag5.txt"


# 1. load file
v_filename = v_input_file
with open(v_filename, 'r') as file:
    v_data_form_file = [line.strip() for line in file]
    print(f'1. loaded file')

# v_data_form_file=
# seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4

# 2. seperate file into arrays
v_case = ""
v_seeds = []
v_cases = ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]
v_data_dict = {}
print(f'2. make array')
for v_line in v_data_form_file:
# if 1:
#     v_line = v_data_form_file[0]
    # print(v_line)
    v_continue = 0
        
    if "seeds:" in v_line:
        # print("seeds:")
        v_case = "seeds:"
        v_temp1 = re.split(r'[:]',v_line)
        v_temp2 = re.split(r'[ ]',v_temp1[1].strip(' '))
        v_seeds = [int(element) for element in v_temp2] #make int and put in array
        # print(v_temp2)
        continue

    for v_possible_case in v_cases:
        if v_possible_case in v_line:
            # print(v_possible_case)
            v_case = v_possible_case
            v_continue = 1
            v_data_dict[v_case] = []

    v_temp1 = re.split(r'[ ]',v_line)

    if v_continue == 1:
        continue
    
    # print(v_temp1)
    if v_temp1==['']:
        # print(v_data_dict[v_case])
        continue
    # print(v_temp1)
    v_data_dict[v_case].append([int(element) for element in v_temp1])

# print("v_seeds: " + v_seeds)
# for v_possible_case in v_cases:
#     try:
#         print(v_possible_case + str(v_data_dict[v_possible_case]))
#     except:
#         continue
# print(v_data_dict)

# v_seeds = ['79', '14', '55', '13']
# v_data_dict = 
# {
# 'seed-to-soil map:': [['50', '98', '2'], ['52', '50', '48']], 
# 'soil-to-fertilizer map:': [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
# 'fertilizer-to-water map:': [['49', '53', '8'], ['0', '11', '42'], ['42', '0', '7'], ['57', '7', '4']], 
# 'water-to-light map:': [['88', '18', '7'], ['18', '25', '70']], 
# 'light-to-temperature map:': [['45', '77', '23'], ['81', '45', '19'], ['68', '64', '13']], 
# 'temperature-to-humidity map:': [['0', '69', '1'], ['1', '0', '69']], 
# 'humidity-to-location map:': [['60', '56', '37'], ['56', '93', '4']]
# }

# 3. make v_source_dest_list whith all sources and destinations
# 3.1 map values
v_source_dest_list = {}
v_keys_list = list(v_data_dict.keys())
for v_possible_case in v_keys_list:
    print(f'3.1 {v_possible_case}')
    for v_line in v_data_dict[v_possible_case]:
        # print(v_line)
        for v_i in range(v_line[2]):
            try:
                v_source_dest_list[v_possible_case]
            except:
                v_source_dest_list[v_possible_case] = []
            v_appendline = [v_line[1] + v_i, v_line[0] + v_i]
            v_source_dest_list[v_possible_case].append(v_appendline)
            # print(v_appendline)
    v_source_dest_list[v_possible_case] = sorted(v_source_dest_list[v_possible_case]) # sort it

# print(v_source_dest_list)

# 3.2 find max number
v_maxnumber = 0
for v_possible_case in v_keys_list:
    if v_source_dest_list[v_possible_case][-1][0] > v_maxnumber:
        v_maxnumber = v_source_dest_list[v_possible_case][-1][0]

# 3.3 fill up array from 0 tot maxnumber
for v_possible_case in v_keys_list:
    print(f'3.3 {v_possible_case}')

    # make temp array like [0,0],[1,1],[2,2,],[3,3,] etc
    v_source_dest_list_temp=[]
    for i_v1 in range(v_maxnumber+1):
        v_source_dest_list_temp.append([i_v1, i_v1])

    # fill it with known mappings
    for i_v1 in v_source_dest_list[v_possible_case]:
        for i_v2 in range(v_maxnumber+1):
            if v_source_dest_list_temp[i_v2][0] == i_v1[0]:
                v_source_dest_list_temp[i_v2] = i_v1
    
    v_source_dest_list[v_possible_case] = v_source_dest_list_temp

# print(v_source_dest_list)

# v_source_dest_list['seed-to-soil map:']=
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51

#4. find place
def F_find_map(v_find,v_data):
    for v_line in v_data:
        if v_find == v_line[0]:
            return v_line[1]



# for v_possible_case in v_keys_list:
v_locationlist = []
for v_seed in v_seeds:
    print(f'find location for seed: {v_seed}')
    v_found = v_seed
    for v_key in v_keys_list:
        v_find = v_found
        v_data = v_source_dest_list[v_key]
        v_found = F_find_map(v_find,v_data)
    v_locationlist.append(v_found)

# print(v_locationlist)

print(min(v_locationlist))