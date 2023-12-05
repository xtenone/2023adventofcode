# https://adventofcode.com/2023/day/2

import re   # regular expresions, just to practice
import copy # to copu dicts, without pointer

# --- Day 2: Cube Conundrum ---
# You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

# The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

# As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

# For example, the record of a few games might look like this:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 g

print()
print("================================================================================================")
print("day2")
print("================================================================================================")
print()

# gonna make a list like
# v_marbles_drawnlist = {
#   1 : [{red: 24, green:12, blue:2}]
#   2 : [{red: 7, green:3, blue:8},{ green:7, blue:2},{red: 1, green:2, blue:2}]
#   3 : [{red: 2, green:11, blue:6},{red: 24, green:15}]
# }
# loop over the list and see if any number exeects the given data


v_marbles_set = {"red":12, "green":13, "blue":14}


# 1. get data from file
def F_day2_p1(v_filename):
    with open(v_filename, 'r') as file:
        v_data_form_file = [line.strip() for line in file]
        return v_data_form_file


# 2. seperate values in games and draws
def F_day2_p2(v_data_form_file):
    v_marbles_drawnlist = {}
    for v_i, v_line in enumerate(v_data_form_file):

        # 2.1 get game number
        # "Game 27: 10 green, 2 red; 5 blue, 1 red; 6 red, 5 green" --> ["Game 27:","10 green, 2 red; 5 blue, 1 red; 6 red, 5 green"]
        # "Game 27:" --> 27
        v_split = re.split(r'[:]',v_line) 
        v_game = re.search(r'[0-9].*', v_split[0]).group()

        
        # 2.2 seperate draws
        # "10 green, 2 red; 5 blue, 1 red; 6 red, 5 green" --> ["10 green, 2 red","5 blue, 1 red","5 green"]
        v_draws = re.split(r'[;]',v_split[1]) 
        # 2.3 extract colours
        # ["10 green, 2 red","5 blue, 1 red","5 green"] --> [{green:10,red:2},{blue:5,red:1},{green:5}]
        v_seperated_draw_details = {}
        v_seperated_game_details = []
        for v_draw in v_draws:                                              # ["10 green, 2 red","5 blue, 1 red","5 green"] --> "10 green, 2 red"
            v_color_split = re.split(r'[,]',v_draw)                         # "10 green, 2 red" --> ["10 green","2 red"]
            for v_color in v_color_split:                                   # ["10 green","2 red"] --> "10 green"
                v_color_of_marble = re.search(r'[a-z].*', v_color).group()  # "10 green" --> green
                v_nr_of_marmbles = re.search(r'[0-9].* ', v_color).group()  # "10 green" --> 10
                v_seperated_draw_details[v_color_of_marble] = v_nr_of_marmbles # {green:10,red:2},{blue:5,red:1},{green:5}
            v_seperated_game_details.append(v_seperated_draw_details.copy())       # [{'green': '5 ', 'red': '6 ', 'blue': '5 '}, {'green': '5 ', 'red': '6 ', 'blue': '5 '}, {'green': '5 ', 'red': '6 ', 'blue': '5 '}]
        v_marbles_drawnlist[v_game] = v_seperated_game_details
    return v_marbles_drawnlist


# 3. loop over the list and see if any number exeects the given data
def F_possible(v_marbles_drawnlist):
    v_noimposible_drawlist = v_marbles_drawnlist.copy()
    for v_gamenr, v_game_data in v_marbles_drawnlist.items():
        v_stop = 0
        for v_draw_data in v_game_data:                                 #{'green': '5 ', 'red': '6 ', 'blue': '5 '}
            if "red" in v_draw_data:
                if int(v_draw_data["red"]) > int(v_marbles_set["red"]):
                    v_stop=1 
            if "green" in v_draw_data:
                if int(v_draw_data["green"]) > int(v_marbles_set["green"]):
                    v_stop=1 
            if "blue" in v_draw_data:
                if int(v_draw_data["blue"]) > int(v_marbles_set["blue"]):
                    v_stop=1 
            if v_stop==1:
                v_noimposible_drawlist.pop(v_gamenr)
                break
    return v_noimposible_drawlist

# 4. sum game numbers
def F_sum(v_noimposible_drawlist):
    answer = 0
    for v_gamenr, v_game_data in v_noimposible_drawlist.items():
        answer += int(v_gamenr)
    return answer


#===========================================================================
# start here
# code for day 2 part 1
def F_day2():
    v_data_form_file = F_day2_p1('data_dag2.txt')
    v_marbles_drawnlist = F_day2_p2(v_data_form_file)
    v_noimposible_drawlist = F_possible(v_marbles_drawnlist)
    answer = F_sum(v_noimposible_drawlist)
    print (answer)

F_day2()





#===========================================================================#===========================================================================
# part 2
#===========================================================================
# lets use the datastructure again {v_marbles_drawnlist}
# but now loop over it and look for the lowest nr of red, blue and green

#===========================================================================
# start here
def F_day2_part2():
    v_data_form_file = F_day2_p1('data_dag2.txt')
    v_marbles_drawnlist = F_day2_p2(v_data_form_file)
    v_totallist = F_day2_part2_lowest_nr_per_color(v_marbles_drawnlist)
    answer = F_sum_array(v_totallist)
    print(answer)

#===========================================================================

# make a list with lowest nuber of marbles
def F_day2_part2_lowest_nr_per_color(v_marbles_drawnlist):
    v_totallist = []
    for v_gamenr, v_game_data in v_marbles_drawnlist.items():
        v_redcount = 1
        v_greencount = 1
        v_bluecount = 1
        for v_draw_data in v_game_data:                                 #{'green': '5 ', 'red': '6 ', 'blue': '5 '}
            if "red" in v_draw_data:
                if int(v_draw_data["red"]) > v_redcount:
                    v_redcount = int(v_draw_data["red"])
            if "green" in v_draw_data:
                if int(v_draw_data["green"]) > v_greencount:
                    v_greencount = int(v_draw_data["green"])
            if "blue" in v_draw_data:
                if int(v_draw_data["blue"]) > v_bluecount:
                    v_bluecount = int(v_draw_data["blue"])
        v_totallist.append([v_redcount,v_greencount,v_bluecount])
    return v_totallist

# sum array
def F_sum_array(v_array_in_array):       # [[1,2,3],[2,2,2],[3,3,2]]
    v_total = 0
    for v_lowestnrs in v_array_in_array: # [1,2,3]
        v_subtotal = 1
        for v_number in v_lowestnrs:     # 1
            v_subtotal = v_subtotal*v_number
        v_total +=v_subtotal
    return v_total # 2274 is to low
 












#===========================================================================
# this is the real start of part 2
F_day2_part2()