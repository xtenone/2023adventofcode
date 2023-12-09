import re

# 1. load file
v_filename = 'data_dag1.txt'
with open(v_filename, 'r') as file:
    v_data_form_file = [line.strip() for line in file]

chars_to_remove = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

removed=[]
for i in v_data_form_file:
    removed.append(re.findall(r'[0-9]',i))
    
removed2=[]
for row in removed:
    removed2.append(int(row[0]+row[-1]))

sum(removed2)