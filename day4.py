
import re
print()


def F_start():
    v_data = F_loadfile('data_dag4.txt')
    F_day4_part1(v_data)



# 1. get data from file
def F_loadfile(v_filename):
    with open(v_filename, 'r') as file:
        v_data_form_file = [line.strip() for line in file]
        return v_data_form_file

def F_day4_part1(v_data):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11


    # ['Card 1', 'Card 2', 'Card 3', 'Card 4', 'Card 5', 'Card 6']
    # [['41', '48', '83', '86', '17'], ['13', '32', '20', '16', '61'], ['1', '21', '53', '59', '44'], ...]
    # [['83', '86', '6', '31', '17', '9', '48', '53'], ['61', '30', '68', '82', '17', '32', '24', '19'], ...]
    v_cards=[]
    v_win  =[]
    v_have =[]
    v_win_string  = []
    v_have_string = []
    for v_line in v_data:
        v_temp1 = re.split(r'[:]',v_line)
        v_temp2 = re.split(r'[|]',v_temp1[1]) 
        v_cards.append(v_temp1[0])
        # v_win_numbers  = re.split(r'[' ']',v_temp2[0].split())
        # v_have_numbers = re.split(r'[' ']',v_temp2[1])
        v_win.append(v_temp2[0].split())
        v_have.append(v_temp2[1].split())
        v_win_string.append(v_temp2[0].lstrip()) #remove leading zero
        v_have_string.append(v_temp2[1].lstrip())
    # print(v_cards)
    # print(v_win)
    # print(v_have)

    ##example
    # text = "aa bb cc dd de e ee"
    # pattern = r'\baa\b|\be\b'
    # matches = re.findall(pattern, text)
    # print(matches)

    # [['48', '83', '86', '17'], ['32', '61'], ['1', '21'], ['84'], [], []]
    v_winning_nr_array = []
    for v_i, v_line in enumerate(v_have_string):
        v_sub_patern = re.sub(r'\s+', r'\\b|\\b', v_line )
        v_pattern = f'\\b{v_sub_patern}\\b'
        # print(v_pattern)
        v_found_numbers = re.findall(v_pattern, v_win_string[v_i])
        v_winning_nr_array.append(v_found_numbers)
        # print(v_win[0])
        # print(v_have[0])
    # print(v_winning_nr_array)



    # 13
    v_points = 0
    for v_line in v_winning_nr_array:
        v_quantity_winningnr = len(v_line)
        if v_quantity_winningnr > 0:
            v_points += pow(2,v_quantity_winningnr-1)
    print(v_points)


F_start()

#=======================================================================================================
# part 2
#=======================================================================================================
print()


def F_start2():
    v_data = F_loadfile('data_dag4.txt')
    F_day4_part2(v_data)


#=======================================================================================================

def F_day4_part2(v_data):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11


    # ['Card 1', 'Card 2', 'Card 3', 'Card 4', 'Card 5', 'Card 6']
    # [['41', '48', '83', '86', '17'], ['13', '32', '20', '16', '61'], ['1', '21', '53', '59', '44'], ...]
    # [['83', '86', '6', '31', '17', '9', '48', '53'], ['61', '30', '68', '82', '17', '32', '24', '19'], ...]
    v_cards=[]
    v_win  =[]
    v_have =[]
    v_win_string  = []
    v_have_string = []
    for v_line in v_data:
        v_temp1 = re.split(r'[:]',v_line)
        v_temp2 = re.split(r'[|]',v_temp1[1]) 
        v_cards.append(v_temp1[0])
        # v_win_numbers  = re.split(r'[' ']',v_temp2[0].split())
        # v_have_numbers = re.split(r'[' ']',v_temp2[1])
        v_win.append(v_temp2[0].split())
        v_have.append(v_temp2[1].split())
        v_win_string.append(v_temp2[0].lstrip()) #remove leading zero
        v_have_string.append(v_temp2[1].lstrip())
    # print(v_cards)
    # print(v_win)
    # print(v_have)

    ##example
    # text = "aa bb cc dd de e ee"
    # pattern = r'\baa\b|\be\b'
    # matches = re.findall(pattern, text)
    # print(matches)

    # [['48', '83', '86', '17'], ['32', '61'], ['1', '21'], ['84'], [], []]
    v_winning_nr_array = []
    for v_i, v_line in enumerate(v_have_string):
        v_sub_patern = re.sub(r'\s+', r'\\b|\\b', v_line )
        v_pattern = f'\\b{v_sub_patern}\\b'
        # print(v_pattern)
        v_found_numbers = re.findall(v_pattern, v_win_string[v_i])
        v_winning_nr_array.append(v_found_numbers)
        # print(v_win[0])
        # print(v_have[0])
    # print(v_winning_nr_array)

    v_duplicator = [1] * len(v_winning_nr_array)
    for v_i, v_line in enumerate(v_winning_nr_array):
        v_points = len(v_line)
        for v_i1 in range(v_points):
            v_duplicator[v_i+v_i1+1] += 1 * v_duplicator[v_i]

    v_answer2 = sum(v_duplicator)
    print(f'anser2 = {v_answer2}')




F_start2()