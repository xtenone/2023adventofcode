# https://adventofcode.com/2023

import re





#================================================================================================
# day 1
#================================================================================================
# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

#================================================================================================
# 1. data "data_dag1" is palced in a file. this file is opened. and put into an array "v_data_dag1"
# ---
# aprouch: just going to use regular expressions to find first and last number
# example:
#       stringetje = "pqr3stu8vwx"
#       match = re.search("[0-9]",stringetje)
#       print(match.group())
#       match = re.search("[0-9]",stringetje[::-1])
#       print(match.group())
# ---

print()
print("================================================================================================")
print("day1")
print("================================================================================================")
print()

# part 1: get data from file
def F_day1p1(v_filename):
    with open(v_filename, 'r') as file:
        v_data_dag1 = [line.strip() for line in file]
        return v_data_dag1

# part 2: get first and last number and sum them
def F_day1p2(v_data_dag1):
    v_number_array = []
    for v_i in range(len(v_data_dag1)):
        match1 = re.search("[1-9]",v_data_dag1[v_i])
        match2 = re.search("[1-9]",v_data_dag1[v_i][::-1])
        v_number_array.append(int(str(match1.group())+""+str(match2.group()))) # combine the 2 numbers to a 2 digit number
    return v_number_array

# part 3: a single command, but let put it in an function for consistency
def F_day1p3(v_numberarray):
    v_answer_dag1 = sum(v_numberarray) # sum them with the total
    return v_answer_dag1

# run part 1 ad part 2 for answer
def F_day1():
    v_data_dag1 = F_day1p1('data_dag1.txt')
    v_number_array = F_day1p2(v_data_dag1)
    v_answer = F_day1p3(v_number_array)

    return v_answer

# show answer day 1
print("Answer day 1: " + str(F_day1()))

#================================================================================================
# day 1 part 2
#================================================================================================
# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

#================================================================================================
# 1. change the names of ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] into [1,2,3,4,5,6,7,8,9] and do the same as day 1
# example:
# stringetje = "adsadsadwafafAAAdwdascwe"
# print(stringetje.replace("AAA","3")) # adsadsadwafaf3dwdascwe
# --
# try2.. aproach was too simple... zoneight234 has one and eight overlapping in it. need a new aproach..
# looking for all numbers, digits and letters. first and last. like in 1 is done with numbers.


print()
print("================================================================================================")
print("day 1 part 2")
print("================================================================================================")
print()


# #change words of numbers in digits -- try1 didnt work
# def F_day2p1(v_data):
#     v_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     v_digits = [1,2,3,4,5,6,7,8,9] 
#     v_data_new = []
#     for v_i1, v_dataline in enumerate(v_data):
#         for v_i2 in range(len(v_words)):
#             v_dataline = v_dataline.replace(v_words[v_i2], str(v_digits[v_i2]))
#         v_data_new.append(v_dataline)
#     return v_data_new


#change words of numbers in digits
def F_day1part2_p1(v_data):
    # prepare needed arrays with digits
    v_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    v_search_pattern = r'[1-9]|one|two|three|four|five|six|seven|eight|nine'

    #regular expresion search again, get array with all numbers
    # ex. 4nineeightseven2 --> ['4','nine','eight','seven','2']
    v_number_array = []
    for v_line in v_data:
        v_found_numbers = re.findall(v_search_pattern, v_line)  
        v_number_array.append(v_found_numbers)

    #change all wordt to numbers
    # ex. ['4','nine','eight','seven','2'] --> ['4',9,8,7,'2']
    for v_i1, v_digits in enumerate(v_number_array):
        for v_i2, v_digit in  enumerate(v_digits):
            if v_digit in v_words:
                v_i3 = v_words.index(v_digit) + 1               # this is the coresponding number to the wordt. it starts from 1 not from 0
                v_number_array[v_i1][v_i2]=v_i3                 

    return v_number_array # array with all found numbers



# combine the 2 numbers to a 2 digit number 
# ex. ['4',9,8,7,'2'] --> [42]
def F_day1part2_p2(v_number_array):
    v_new_number_array = []
    for v_number in v_number_array:
        v_new_number = str(v_number[0])+""+str(v_number[-1])    
        v_new_number_array.append(int(v_new_number))            
    return v_new_number_array                                   

# run code for day1 part 2
def F_day1part2():
    v_data = F_day1p1("data_dag1.txt")                # read data
    v_new_data = F_day1part2_p1(v_data)               # transform
    v_new_data_numbers = F_day1part2_p2(v_new_data)   # extract first and last number
    v_answer = F_day1p3(v_new_data_numbers)           # sum the array
    # for v_i in range(len(v_data)):
    #     print(f'{v_data[v_i]}\t{v_new_data[v_i]}\t{v_new_data_numbers[v_i]}')
    return v_answer

print("answer: " + str(F_day1part2())) # 53519 is wrong..




