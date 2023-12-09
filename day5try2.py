# try2, didnt see the numbers are quite hight. so need a more elegant and less memory greedy sollution.

import re
print()
# v_input_file = "data_dag5.txt"
v_input_file = "data_dag5.txt"

v_part2 = 1

# 1. load file
v_filename = v_input_file
with open(v_filename, 'r') as file:
    v_data_form_file = [line.strip() for line in file]
    print(f'1. loaded file')

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


# 3. make v_source_dest_list whith all sources and destinations
# 3.1 map values
v_source_dest_list = {}
v_keys_list = list(v_data_dict.keys())
print(f'3.1 make new easier list')
for v_possible_case in v_keys_list:
    # for v_line in v_data_dict[v_possible_case]:
    #     # print(v_line)
    #     for v_i in range(v_line[2]):
    #         try:
    #             v_source_dest_list[v_possible_case]
    #         except:
    #             v_source_dest_list[v_possible_case] = []
    #         v_appendline = [v_line[1] + v_i, v_line[0] + v_i]
    #         v_source_dest_list[v_possible_case].append(v_appendline)
    #         # print(v_appendline)
    # v_source_dest_list[v_possible_case] = sorted(v_source_dest_list[v_possible_case]) # sort it
    v_current_list = v_data_dict[v_possible_case]
    v_current_list = sorted(v_current_list) # sort it
    v_temp_list = []
    for i_line in v_current_list:
        v_temp_list.append([i_line[1],i_line[1]+i_line[2]-1,i_line[0]-i_line[1]])
        
    
    v_data_dict[v_possible_case] = sorted(v_temp_list)
    # print(v_data_dict[v_possible_case])
        # this list is like this [[start],[end],[difference]]
        # so [52 50 48]-->[[50],[97],[2]]
    
# # 4 find location

# #4. find place
def F_find_map(v_find,v_data):
    # print(v_find)
    # print(v_data)
    v_return = v_find
    for v_i, v_line in enumerate(v_data):
        if v_find >= v_line[0] and v_find <= v_line[1]:
            v_return = v_find + v_line[2]
    # print(v_return)
    return v_return

# for v_possible_case in v_keys_list:
v_locationlist = []

print()
if v_part2 != 1:
    for v_seed in v_seeds:
        # print(f'find location for seed: {v_seed}')
        v_found = v_seed
        for v_key in v_keys_list:
            v_find = v_found
            v_data = v_data_dict[v_key]
            v_found = F_find_map(v_find,v_data)
        v_locationlist.append(v_found)

    # # print(v_locationlist)
    print(min(v_locationlist)) # not 512702828

    # PART2
#===================================================================
# too greedy
# print(len(v_seeds)/2)
# v_temp1
# for v_i in range(int(len(v_seeds)/2)):
#     print(v_i)
#     v_start = v_seeds[v_i*2]
#     v_till = v_seeds[v_i*2]+v_seeds[v_i*2+1]
#     print(v_start)
#     print(v_till)
#     # v_temp1 = list(range(v_start, v_till))
# v_seeds = v_temp1
#
# less greedy, find places of ranges, place them in 1 array, 
# calculte the total change in those ranges
# find optimal range then find optimal number in that range for the 
# ranges of seeds
# 
# ... its a puzzle... for fun... this will take to much brain power...
# so new greedy apraoch!! les big chunks a time. so less memory is used!!
# its python thoigh, without pandas of nympy... so it has to be really limitit 
#

# v_part2 = 1
# if v_part2 == 1:
#     for v_i1 in range(int(len(v_seeds)/2)):
#         v_start = v_seeds[v_i1*2]
#         v_till = v_seeds[v_i1*2]+v_seeds[v_i1*2+1]
#         v_splitsize = 10000000
#         v_minlocation = 99999999999 
#         v_start2 = v_start
#         v_counter = 0
#         while 1:
#             # print(f'v_till: {v_till}, \nv_start2: {v_start2}')
#             v_start2 = v_start + v_counter*v_splitsize
#             v_counter += 1
#             v_till2 = v_start2 + v_splitsize
#             print(f'from {v_start2} till {v_till2}')
#             if v_start2 > v_till:
#                 break
#             if v_till2 > v_till:
#                 v_till2 = v_till
            
#             v_seeds = list(range(v_start2, v_till2))
            
#             for v_seed in v_seeds:
#                 # print(f'find location for seed: {v_seed}')
#                 v_found = v_seed
#                 for v_key in v_keys_list:
#                     v_find = v_found
#                     v_data = v_data_dict[v_key]
#                     v_found = F_find_map(v_find,v_data)
#                     if v_found < v_minlocation:
#                         v_minlocation = v_found
#                         print(v_minlocation)

# ok so there seem to be more numbers then i thought. Its not only a memory botlle neck
# but also a processing problem. So need to solve it smarter... no not that smart! its still a puzzle for fun..
# So inverse search!! BRUTE FORCE! and see the first seed it hits!

# #4. find place
def F_find_seed_reversed(v_find,v_data):
    # print(v_find)
    # print(v_data)
    v_return = v_find
    
    v_data = sorted(v_data, key=lambda x: x[1])

    for v_i, v_line in enumerate(v_data):
        v_find2=v_find-v_line[2]
        if v_find2 >= v_line[0] and v_find2 <= v_line[1]:
            v_return = v_find2
    # print(v_return)
    return v_return


if v_part2 == 1:

    #first make ranges of seeds array
    v_seed_ranges_array = []
    for v_i1 in range(int(len(v_seeds)/2)):
        v_seed_ranges_array.append([v_seeds[2*v_i1],v_seeds[2*v_i1]+v_seeds[2*v_i1+1]-1])

    # print(v_seed_ranges_array)
    v_stop2 =0
    # for v_i1 in range(0,10000000000,1000):
    for v_i1 in range(125713000,10000000000,1):
        v_found = v_i1 #46 # 46-46-45-77-84-84-84-82
        print(v_i1)

        for v_key in v_keys_list[::-1]:
            v_data = v_data_dict[v_key]
            # print(v_data)
            v_found = F_find_seed_reversed(v_found,v_data)
            # print(v_found)

        for v_seedline in v_seed_ranges_array:
            if v_found>v_seedline[0] and v_found<v_seedline[1]:
                print(f'I FOUND IT!!! seed: {v_found}')
                print(f'I FOUND IT!!! location: {v_i1}')
                v_stop2 = 1
                break

        if v_stop2 == 1:
            break

    print(v_found) # 125742456

    # v_search_range = 2 # small steps
    # for v_chunknr in range(0,1000,1):
    #     # print(v_chunknr)
    #     chunk = v_chunknr
    #     v_start = v_search_range*chunk
    #     v_stop = v_search_range*(chunk+1)
    #     v_stop2 = 0
    #     for v_i in range(v_start,v_stop):
    #         # print(v_i)
    #         v_found = v_i
    #         for v_key in v_keys_list[::-1]:
    #             v_data = v_data_dict[v_key]
    #             v_found = F_find_seed_reversed(v_found,v_data)
            


    #         print(v_found)
    #         #see if its a seed we have
    #         for v_seedline in v_seed_ranges_array:
    #             if v_found>v_seedline[0] and v_found<v_seedline[1]:
    #                 print(f'I FOUND IT!!! {v_found}')
    #                 v_stop2 = 1
    #                 break
            
    #         if v_stop2 == 1:
    #             break
            
            

#===================================================================
