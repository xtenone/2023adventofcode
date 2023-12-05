#https://adventofcode.com/2023/day/3
import re
print()



def start():
    
    # 1.    read in file
    v_datafile = F_loadfile("data_dag3.txt")
    # 1.2   put in array
    # v_data = F_make_array(v_datafile)

    # 2.1.  replace all numbers by counter  ex....234...2..42.. --> ....000...1..22..
    # 2.2.  place numbers in array with coresponing index
    v_data_obj = F_find_numbers(v_datafile)
    # print(v_data_obj)
    # 3.1   make 2nd array same size as data, 
    # 3.2   change everything ftom 0-9 and . into a 0
    # 3.3   change everything not a 0 into a 1
    # 4.1   delution on 1's, make 0's around 1's to 1's
    # 5.1   multiply both arrays with each other
    # 6.1   put all numbers not 0 in an array
    # 6.2   only keep unique onces
    # 7.1   get real numbers from stored numbers and put them in an other array
    # 8     sum this array



#=======================================================================================================
# 1. get data from file
def F_loadfile(v_filename):
    # ...798...145....
    # ......*.....*...
    # ..459..489.817..
    # ...798...145....
    with open(v_filename, 'r') as file:
        v_data_form_file = [line.strip() for line in file]
        return v_data_form_file

# def F_make_array(v_datafile);

def F_find_numbers(v_data):

    v_copy_array_counters = []
    v_copy_array_numbers = []
    v_counter = 0

    v_search_pattern = r'[0-9]*'
    for v_i, v_line in enumerate(v_data): #ex. '467..114.....*......'

    # [0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 3, 3, 3, 0, 0, 4, 4, 4, 0, 5, 5, 5, 0, 0, 0]
    # [0, 0, 0, 6, 6, 6, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0]

    #[798, 145, 459, 489, 817, 798, 145]
        v_copy_array_counters.append([])
        v_found_numbers = re.findall(v_search_pattern, v_line) # ['467..114..*.'] --> ['467', '', '', '114', '', '', '', '', '']
        for v_nr in v_found_numbers:
            if v_nr == '':
                v_copy_array_counters[v_i].append(0)
            else:
                v_copy_array_numbers.append(int(v_nr))            # ['467', '', '', '114', '', '', '', '', ''] --> [467, 114]]
                v_counter+=1
                for v_char in v_nr:
                    v_copy_array_counters[v_i].append(v_counter)  # ['467', '', '', '114', '', '', '', '', ''] --> [1,1,1, 0, 0, 2,2,2, 0, 0, 0, 0, 0]
        
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v_copy_array_icons_places = []
    v_search_pattern = r'[^0-9.]*'
    for v_i, v_line in enumerate(v_data): #ex. '467..114.....*......'
        # ['467', '', '', '114', '', '', '', '', ''] --> [467, 114]]
        v_copy_array_icons_places.append([])
        v_found_icons = re.findall(v_search_pattern, v_line) # ['467..114..*.'] --> ['467', '', '', '114', '', '', '', '', '']
        for v_nr in v_found_icons:
            if v_nr == '':
                v_copy_array_icons_places[v_i].append(0)
            else:
                v_copy_array_icons_places[v_i].append(2)

    # [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
    # [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
    # [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for v_y, v_line in enumerate(v_copy_array_icons_places):
        for v_x, v_digid in enumerate(v_line):
            if v_digid == 2:
                for v_i1 in [-1,0,1]:
                    for v_i2 in [-1,0,1]:
                        v_copy_array_icons_places[v_y+v_i1][v_x+v_i2] = 1

    # [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 5, 5, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v_copy_array_counters2 = v_copy_array_icons_places
    for v_y, v_line in enumerate(v_copy_array_counters):
        for v_x, v_digid in enumerate(v_line):
            v_copy_array_counters2[v_y][v_x]=v_copy_array_icons_places[v_y][v_x] * v_digid
    
    # [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]
    v_copy_array_numbers2 = []
    for v_y, v_line in enumerate(v_copy_array_icons_places):
        for v_x, v_digid in enumerate(v_line):
            if v_digid != 0:
                v_copy_array_numbers2.append(v_digid)

    #[1, 2, 4, 5]
    v_copy_array_numbers3 = list(set(v_copy_array_numbers2))

    # [145, 459, 817, 798]
    v_copy_array_numbers4 = []
    for v_nr in v_copy_array_numbers3:
        v_nrmin = v_nr -1
        v_copy_array_numbers4.append(v_copy_array_numbers[v_nrmin])

    # 2219
    v_answer1 = sum(v_copy_array_numbers4)
    print(v_answer1)

    v_data_obj = {'array_original':v_data,'array_counter':v_copy_array_counters,'array_numbers':v_copy_array_numbers,'array_icons':v_copy_array_icons_places}, 
    return v_data_obj
    # print(v_line)
    # print(v_copy_array_counters)
    # print(v_copy_array_numbers)
                


           
            





























start()